from urllib.request import urlopen,Request
from urllib.parse import urlencode

def get_html(url):
    headars={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
    request=Request(url,headers=headars)
    response=urlopen(request)
    return response.read()


def save_html(fname,html_bytes):
    with open(fname,'wb') as f:
        f.write(html_bytes)

def main():
    content=input("请输入下载内容：")
    num=input("请输入下载页数：")
    for pn in range(int(num)):
        base_url = 'https://tieba.baidu.com/f?ie=utf-8&{}'
        args={
            'pn':pn*50,
            'kw':content
        }
        fname = "第" + str(pn+1) + '页.html'
        args=urlencode(args)
        print('正在下载'+fname)
        html_bytes=get_html(base_url.format(args))
        save_html(fname,html_bytes)

main()
