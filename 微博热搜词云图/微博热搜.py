import requests
import jieba
from lxml import etree
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

url = 'https://s.weibo.com/top/summary'
headars = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

rest = requests.get(url, headers=headars)
e = etree.HTML(rest.text)
hotspots = e.xpath('//td/a/text()')
with open('1.txt', 'w', encoding='utf-8') as f:
    for i in hotspots:
        f.write(i)
        f.write('\n')
text=open('1.txt','r',encoding='utf-8').read()
cut_text=jieba.cut(text)
result=' '.join(cut_text)
bg_img=np.array(Image.open('tg.jpg'))
wc=WordCloud(
    # 字体
    font_path='zt.ttf',
    # 背景颜色
    background_color='white',
    mask=bg_img,
    # 图片的宽
    width=700,
    # 图片的高
    height=500,
    # 字体大小
    max_font_size=50,
    min_font_size=10,
)
wc.generate(result)
wc.to_file('2.png')
plt.figure('11')
plt.imshow(wc)
plt.axis('off')
plt.show()