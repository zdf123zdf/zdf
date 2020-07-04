import requests
from bs4 import BeautifulSoup


def html_get(url):  # 网页请求

    headars = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    rest = requests.get(url, headers=headars)
    res = rest.text
    soup=BeautifulSoup(res,'lxml')
    #书名
    pat1=soup.find_all('div', class_='pl2')
    names = [div.find('a')['title'] for div in pat1]
    # 作者
    pat2 = soup.find_all('p', class_='pl')
    authors=[p.text.split('/')[0] for p in pat2]
    #评分
    pat3=soup.find_all('span',class_='rating_nums')
    scores = [s.get_text() for s in pat3]

    for i in range(len(authors)):
        print(f'<<{names[i]}>>，作者：{authors[i]}，评分：{scores[i]}')

def main():
    for a in range(0,250,25):
        url=f'https://book.douban.com/top250?start={a}'
        print(f'——————————————————正在爬取第{a//25+1}页——————————————————————')
        html_get(url)

if __name__ == '__main__':
    # 入口
    main()
