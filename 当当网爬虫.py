import requests
from lxml import etree


def get_html(url):
    headars = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    rest = requests.get(url, headers=headars)
    e = etree.HTML(rest.text)
    names = e.xpath('//p/a/@title')
    jgs = e.xpath('//p/span[@class="search_pre_price"]/text()')
    for name, jg in zip(names, jgs):
        print(name, jg)


def main():
    a = input("请输入搜索的内容：")
    for b in range(1, 10):
        print(f'——————————————————————正在爬取第{b}页内容—————————————————————————————')
        get_html(f'http://search.dangdang.com/?key={a}&page_index={b}')


if __name__ == '__main__':
    # 入口
    main()
