import re
import json
import requests
from pathlib import Path
import datetime
now = datetime.datetime.now()

for year in range(1950,now.year+1):
    url = "https://ikeacatalogues.ikea.com/sv-{}/page/1".format(year)
    text = requests.get(url).text
    data = re.search(r"var data = (\{.*\});", text)
    data = json.loads(data.group(1))
    # uncomment this to print all data:
    # #print(json.dumps(data, indent=4))
    url = data['config']['downloadPdfUrl']
    r = requests.get(url, stream=True)
    filename = Path(('IKEA-{}.pdf').format(year))
    response = requests.get(url)
    filename.write_bytes(response.content)