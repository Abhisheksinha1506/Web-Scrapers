#!/usr/bin/python

import json
import logging
import os
import re
import urllib
import urllib2

from subprocess import call

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

MAIN_URL = 'https://www.lego.com/en-us/service/buildinginstructions/'
THEME_URL = 'https://www.lego.com//service/biservice/searchbytheme?fromIndex={idx}&onlyAlternatives=false&theme={theme}'
THEME_REGEX = "data-search-themes='(.*?)'"
PATH_TEMPLATE = 'download/{theme}/{productId} - {productName}/{description} - {pdf}'


def download_file(url, save_to):
    path = os.path.join(os.path.split(save_to)[:-1])[0]
    mkdir = ["mkdir", "-p", path]
    call(mkdir)

    wget = ["wget", "-T20", "--tries=3", "--retry-connrefused",
            "--continue", "-O", save_to, url]
    return call(wget)


def get(url):
    logger.debug('Downloading {0}'.format(urllib.unquote(url)))

    class context:
        retries = 0

    def err(e):
        logger.error(e)
        context.retries = context.retries + 1
        if context.retries == 3:
            raise e

    while True:
        try:
            opener = urllib2.build_opener()
            opener.addheaders = [('User-Agent', 'Lego Scrape 1.0')]
            response = opener.open(url)
            break
        except urllib2.HTTPError as e:
            if e.code == 404:
                raise e
            else:
                err(e)
        except urllib2.URLError as e:
            err(e)

    data = response.read()
    return data


def get_themes():
    page = get(MAIN_URL)
    themes_json = re.findall(THEME_REGEX, page)[0]
    return json.loads(themes_json)


def get_theme_products(theme):
    theme_filename = 'data/{}.json'.format(theme)
    if os.path.exists(theme_filename):
        with open(theme_filename) as fin:
            return json.load(fin)

    last_data = {'moreData': True}
    products = []
    idx = 0
    while last_data['moreData']:
        theme_json = get(THEME_URL.format(idx=idx, theme=theme))
        last_data = json.loads(theme_json)
        products.extend(last_data['products'])
        idx += 10

    with open(theme_filename, 'w') as fout:
        json.dump(products, fout)

    return products


def get_all_products():
    themes = get_themes()
    all_products = []
    for theme in themes:
        all_products.extend(get_theme_products(theme['Key']))
    return all_products


def safe_name(file_name):
    file_name = file_name.replace('+', 'plus')
    file_name = file_name.replace(':', '-')
    return re.sub('[^-a-zA-Z0-9_.() ]', '_', file_name)


def get_all_urls_and_paths():
    for product in get_all_products():
        for download in product['buildingInstructions']:
            path = PATH_TEMPLATE.format(theme=safe_name(product['themeName']),
                                        productId=safe_name(
                                            product['productId']),
                                        productName=safe_name(
                                            product['productName']),
                                        description=safe_name(
                                            download['description']),
                                        pdf=safe_name(download['pdfLocation'].split('/')[-1]))
            url = download['pdfLocation']
            yield url, path


def main():
    for url, path in get_all_urls_and_paths():
        download_file(url, path)


if __name__ == '__main__':
    main()
