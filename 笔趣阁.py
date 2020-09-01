import requests
from lxml import etree

def html_get(url):
        headars = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
        response = requests.get(url, headers=headars)
        res = response.text
        e = etree.HTML(res)
        name=e.xpath('//div[@class="bookname"]/h1/text()')
        print(f'——————————————————————{name}——————————————————————————')
        articles=e.xpath('//div[@id="content"]/p/text()')
        article = [x.strip() for x in articles if x.strip() != '']
        print(article)

def main():
    headars = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
    response = requests.get('https://www.biquge5200.com/52_52542/', headers=headars)
    res = response.text
    e = etree.HTML(res)
    urls = e.xpath('//dd/a/@href')
    for url in urls[9::]:
        html_get(url)

if __name__ == '__main__':
    # 入口
    main()
