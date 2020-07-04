import requests
from bs4 import BeautifulSoup


def html_get(url):  # 网页请求

    headars = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    rest = requests.get(url, headers=headars)
    res = rest.text
    soup = BeautifulSoup(res, 'lxml')
    pat1 = soup.find_all('div',class_="content")
    names = [div.text.split() for div in pat1]
    file = open('糗事百科.txt', 'a', encoding='utf-8')
    for i in range(len(names)):
        jg=names[i]
        print(jg)
        file.write(str(jg))
        file.write('\n')

def main():
    for a in range(1,14):
        url=f'https://www.qiushibaike.com/text/page/{a}'
        print(f'——————————————————正在爬取第{a}页——————————————————————')
        html_get(url)

if __name__ == '__main__':
    # 入口
    main()
