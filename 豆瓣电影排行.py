import requests
import re
import xlwt

def excel(ranking,movies,score):
    # 存储成excel表
    wb = xlwt.Workbook()  # 创建工作表
    sheet = wb.add_sheet('test') # 创建表名

    for m in range(len(movies)):  # 遍历有几个movie
        # m=0,第一个movie
        sheet.write(m,0,ranking[m])
        sheet.write(m,1, movies[m])
        sheet.write(m,2,score[m])
        wb.save('豆瓣电影排行.xls')

ranking=["电影排名"]
movies = ["电影名称"]
score=['评分']

def html_get(url):  #网页请求
    
    headars={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    rest = requests.get(url,headers=headars)
    res=rest.text
    pat ='<em class="">(.*?)</em>.*?<img.*?alt="(.*?)"'  #电影名
    pat1='property="v:average">(.*?)</span>'  #豆瓣评分
    rst = re.compile(pat, re.S).findall(res)
    rst1=re.compile(pat1, re.S).findall(res)
    file = open('豆瓣电影排行.txt', 'a', encoding='utf-8')   #保存到txt文件中
    for i in range(25):
        run = rst[i]
        run1=rst1[i]
        run2=f'第{run[0]}名：<<{run[1]}>>，评分：{run1}'
        file.write(run2)
        file.write('\n')
        movies.append(run[1])
        ranking.append(run[0])
        score.append(run1)


def main():
    for a in range(0,250,25):
        url=f'https://movie.douban.com/top250?start={a}'
        print(f'——————————————————正在爬取第{a//25+1}页——————————————————————')
        html_get(url)
        excel(ranking, movies,score)


if __name__ == '__main__':
    # 入口
    main()
