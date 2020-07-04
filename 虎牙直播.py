from selenium import webdriver
from time import sleep

diver=webdriver.Chrome()
url='https://www.huya.com/g/2168'
diver.get(url)
num=1
while True:
    print('第'+str(num)+'页————————————————————')
    num+=1
    sleep(4)
    html=diver.page_source
    names=diver.find_elements_by_xpath('//i[@class="nick"]')
    counts=diver.find_elements_by_xpath('//span[@class="num"]')
    for name,count in zip(names,counts):
        print(name.text, ":", count.text)
    if diver.page_source.find('laypage_next')!=-1:
        diver.find_element_by_xpath('//a[@class="laypage_next"]').click()
    else:
        break

diver.quit()
