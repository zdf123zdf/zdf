import requests
from lxml import etree
import os

headars = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

url = "https://www.vmgirls.com/13487.html"
response = requests.get(url, headers=headars)
e = etree.HTML(response.text)
img_urls = e.xpath('//p/a/@href')
# 目录名字
dirs_name=e.xpath('//p/a/@alt')
dir_name=str(dirs_name[1])
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

for url in img_urls[:-3]:
    print(url)
    response= requests.get(url, headers=headars)
    img_name =url.split('/')[-1]
    with open(dir_name + '/' + str(img_name), 'wb') as f:
        f.write(response.content)
