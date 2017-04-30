from bs4 import BeautifulSoup
import requests
import json
url='http://www.91porn.com/v.php'

for i in range(1):

    payloads={'next':'watch','page':i}
    r=requests.get(url,data=json.dump(payloads))
    print r.text


