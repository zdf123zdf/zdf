from selenium import webdriver
from time import sleep
from lxml import etree

diver=webdriver.Chrome()
url='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA'
diver.get(url)
js = 'document.documentElement.scrollTop=100000'
sleep(3)

diver.execute_script(js)
html=diver.page_source
e=etree.HTML(html)
prices = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')
names = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')
print(len(names))

for name, price in zip(names, prices):
    print(name.xpath('string(.)'), ":", price)
diver.quit()
