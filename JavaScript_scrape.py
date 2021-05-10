import requests
from lxml import html

extracted_data = []

script = '''
    headers = {
        ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        ['cookie'] = 'AKAM_CLIENTID=900310a15c7997a11d2fb87ba96b454b; gb_lang=en; gb_pipeline=GB; _gcl_au=1.1.1586283703.1555317699; _ga=GA1.2.1217688139.1555317699; gb_countryCode=DZ; _fbp=fb.1.1555317699787.334894344; gb_currencyCode=USD; od=gzguxgyfmdgy1555317700622; gb_vid=8153f54a-97b5-a192-9676-c0fd4028b6ae; gb_guid=407704339; _gid=GA1.2.1854099548.1556004946; osr_referrer=originalurl; osr_landing=https%3A%2F%2Fwww.gearbest.com%2Fflash-sale.html; gb_fcm=1; gb_fcmPipeLine=GB; gb_fcmtoken=dk8gh1DHFHA:APA91bGsnmmdgyH2U82muLlxiPo3tCEFk05x_nqrZaTtbDSirtB5jGGuoitpsumxlhakAvBN9ccWznm8ik4vIFIf5GIF7PMoesX-HPsrNdTZur52kL7Jq5BOK78Nw-fbL1yUjMkVG4nE; gb_soa_www_session=eyJpdiI6Ik9JTkdROHRESnZxRWVFa1dQNzNrSVE9PSIsInZhbHVlIjoiYm1DR3RZZXhkUGc5MGV2N21RRnkxMm9FVjBLOTVRanFqYWVnNWVYckJOWWJWc09RNFpTN1JSM0IyRllBYllBTmNMK095YVV1NUoyaG9aWFg3Z1pTQWc9PSIsIm1hYyI6Ijc3ZmYxMmVlMmU3MGJhNWQyOGU0MTc2ZGE4Mzk1ODE1YmIxNDQ2MzNlOTI5NjY0YWM5NWY2MzAxZDE0NDAzZGMifQ%3D%3D; gb_vsign=93468a44ad3a0ff5ea1bad4bcc0c681c286cc872; bgsid=f137b66ca708d0942919; ORIGINDC=3; ak_bmsc=0E3B5DB1C447767B44AC93E06CB8311902142C5D0D580000130DBF5C96B02C05~plCyCo1fqt6FdNWP/8KL5VuaKJ6RDree2aZ0CDdEMqGVv4uts0HH5sWYVOxHdn9bX7lhE6DJQUffLW9nt4l5Ykja4SQ6vncHf39Zknn+3XeYS/vadTnj29We5PNLQO1ug7G9SzmJaxfr3jrVcky9Z+rG+ElOpbxbeqhR8F1dvCP9XgwKQ8I3LVNUBD0WAsauDXy3f4jF6nv6+GslaH5u5NWAPBxrKUrhea4xPzY6uf7jM6w1Fw/zVCTiHGKZQuQrWO; WEBF_guid=900310a15c7997a11d2fb87ba96b454b_1556024598; cdn_countryCode=DZ; gb2019_gb_sid=bed094a9-86fd-a42f-905b-0438cad548cf; gb_categoryAB=D; gb_searchAB=B; landingUrl=https://www.gearbest.com/flash-sale.html; bm_sv=F28171DFBC89207DA42096D894542D45~eCxY/2DAjaNP5o9SmWspZcwk1r5pulFBsV1wohJT68G23oSt9131mB+Zv1uInJPt+3eF2OeOFxcIGgNnftMnPBm5FPLlxGXt67Ui0iu6vWoQ0yxcNlmaSeBLlqdCksblUkYGQCGnWVMQMb6vpbW2xbrZl6YtyyjRMTqvAMAoRFc=; WEBF_predate=1556025612; gb2019_gb_sid_bed094a9-86fd-a42f-905b-0438cad548cf=false; gb_pf=%7B%22rp%22%3A%22originalurl%22%2C%22lp%22%3A%22https%3A%2F%2Fwww.gearbest.com%2Fflash-sale.html%22%2C%22wt%22%3A1556025612705%7D'
    }
    splash:set_custom_headers(headers)
    splash.private_mode_enabled = false
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(1))
    return splash:html()
'''

resp = requests.post(url='http://192.168.99.100:8050/run', json={
    'lua_source': script,
    'url': 'https://www.gearbest.com/flash-sale.html'
})

tree = html.fromstring(html=resp.content)

deals = tree.xpath("//li[contains(@class, 'goodsItem')]/div[@class='goodsItem_content']")
for deal in deals:
    product = {
        'name': deal.xpath(".//div[@class='goodsItem_title']/a/text()")[0].strip(),
        'url': deal.xpath(".//div[@class='goodsItem_title']/a/@href")[0],
        'original_price': deal.xpath(".//div[@class='goodsItem_delete']/del/@data-currency")[0],
        'discounted_price': deal.xpath(".//div[@class='goodsItem_detail']/span/@data-currency")[0],
    }
    extracted_data.append(product)

print(extracted_data)
import requests
from lxml import html

extracted_data = []

script = '''
    headers = {
        ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        ['cookie'] = 'AKAM_CLIENTID=900310a15c7997a11d2fb87ba96b454b; gb_lang=en; gb_pipeline=GB; _gcl_au=1.1.1586283703.1555317699; _ga=GA1.2.1217688139.1555317699; gb_countryCode=DZ; _fbp=fb.1.1555317699787.334894344; gb_currencyCode=USD; od=gzguxgyfmdgy1555317700622; gb_vid=8153f54a-97b5-a192-9676-c0fd4028b6ae; gb_guid=407704339; _gid=GA1.2.1854099548.1556004946; osr_referrer=originalurl; osr_landing=https%3A%2F%2Fwww.gearbest.com%2Fflash-sale.html; gb_fcm=1; gb_fcmPipeLine=GB; gb_fcmtoken=dk8gh1DHFHA:APA91bGsnmmdgyH2U82muLlxiPo3tCEFk05x_nqrZaTtbDSirtB5jGGuoitpsumxlhakAvBN9ccWznm8ik4vIFIf5GIF7PMoesX-HPsrNdTZur52kL7Jq5BOK78Nw-fbL1yUjMkVG4nE; gb_soa_www_session=eyJpdiI6Ik9JTkdROHRESnZxRWVFa1dQNzNrSVE9PSIsInZhbHVlIjoiYm1DR3RZZXhkUGc5MGV2N21RRnkxMm9FVjBLOTVRanFqYWVnNWVYckJOWWJWc09RNFpTN1JSM0IyRllBYllBTmNMK095YVV1NUoyaG9aWFg3Z1pTQWc9PSIsIm1hYyI6Ijc3ZmYxMmVlMmU3MGJhNWQyOGU0MTc2ZGE4Mzk1ODE1YmIxNDQ2MzNlOTI5NjY0YWM5NWY2MzAxZDE0NDAzZGMifQ%3D%3D; gb_vsign=93468a44ad3a0ff5ea1bad4bcc0c681c286cc872; bgsid=f137b66ca708d0942919; ORIGINDC=3; ak_bmsc=0E3B5DB1C447767B44AC93E06CB8311902142C5D0D580000130DBF5C96B02C05~plCyCo1fqt6FdNWP/8KL5VuaKJ6RDree2aZ0CDdEMqGVv4uts0HH5sWYVOxHdn9bX7lhE6DJQUffLW9nt4l5Ykja4SQ6vncHf39Zknn+3XeYS/vadTnj29We5PNLQO1ug7G9SzmJaxfr3jrVcky9Z+rG+ElOpbxbeqhR8F1dvCP9XgwKQ8I3LVNUBD0WAsauDXy3f4jF6nv6+GslaH5u5NWAPBxrKUrhea4xPzY6uf7jM6w1Fw/zVCTiHGKZQuQrWO; WEBF_guid=900310a15c7997a11d2fb87ba96b454b_1556024598; cdn_countryCode=DZ; gb2019_gb_sid=bed094a9-86fd-a42f-905b-0438cad548cf; gb_categoryAB=D; gb_searchAB=B; landingUrl=https://www.gearbest.com/flash-sale.html; bm_sv=F28171DFBC89207DA42096D894542D45~eCxY/2DAjaNP5o9SmWspZcwk1r5pulFBsV1wohJT68G23oSt9131mB+Zv1uInJPt+3eF2OeOFxcIGgNnftMnPBm5FPLlxGXt67Ui0iu6vWoQ0yxcNlmaSeBLlqdCksblUkYGQCGnWVMQMb6vpbW2xbrZl6YtyyjRMTqvAMAoRFc=; WEBF_predate=1556025612; gb2019_gb_sid_bed094a9-86fd-a42f-905b-0438cad548cf=false; gb_pf=%7B%22rp%22%3A%22originalurl%22%2C%22lp%22%3A%22https%3A%2F%2Fwww.gearbest.com%2Fflash-sale.html%22%2C%22wt%22%3A1556025612705%7D'
    }
    splash:set_custom_headers(headers)
    splash.private_mode_enabled = false
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(1))
    return splash:html()
'''

resp = requests.post(url='http://192.168.99.100:8050/run', json={
    'lua_source': script,
    'url': 'https://www.gearbest.com/flash-sale.html'
})

tree = html.fromstring(html=resp.content)

deals = tree.xpath("//li[contains(@class, 'goodsItem')]/div[@class='goodsItem_content']")
for deal in deals:
    product = {
        'name': deal.xpath(".//div[@class='goodsItem_title']/a/text()")[0].strip(),
        'url': deal.xpath(".//div[@class='goodsItem_title']/a/@href")[0],
        'original_price': deal.xpath(".//div[@class='goodsItem_delete']/del/@data-currency")[0],
        'discounted_price': deal.xpath(".//div[@class='goodsItem_detail']/span/@data-currency")[0],
    }
    extracted_data.append(product)

print(extracted_data)
