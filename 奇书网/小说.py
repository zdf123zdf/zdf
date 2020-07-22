import requests
from lxml import etree
import re

def get_html(url):

    headars = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    rest = requests.get(url, headers=headars)
    rest.encoding = 'utf-8'
    e=etree.HTML(rest.text)
    novel=e.xpath('//div/text()')
    nmae=e.xpath('//h1/text()')
    with open(f'{nmae[0]}.txt', 'a+', encoding='utf-8') as f:
        for x in novel:
            if x.strip() != '':
                novels=x.strip()
                if novels != '|':
                    s = re.compile('（本章未完，请点击下一页继续阅读）|第.+章 .+|')
                    message = re.sub(s, '', novels)
                    if message!='':
                        #print(message)
                        f.write(message)
                        f.write('\n')



def main():
    for a in range(193,1000):
        for i in range(1,4):
            url=f'http://m.iqishu.la/du/23/23544/1726{a}_{i}.html'
            get_html(url)


if __name__ == '__main__':
    # 入口
    main()