import requests
from bs4 import BeautifulSoup
import time
import lxml
import random
SLEEP_TIME = random.randint(1,2)
url = "https://mp.weixin.qq.com/s/llefEk5xSUp4z-cXDT549A"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
first = requests.get(url,headers=header)
if first.status_code == 200 :
    print("访问正常。")
    soup = BeautifulSoup(first.text,"lxml")
    #文章标题和Url在section data-role="outer"下
    #分在四个部分。我打算前三个部分有手动复制，后面的几百部分，有爬虫
    #section data-role="paragraph" > section data-tools="135编辑器" > a href 和标题
    #大部分文章的Url
    new_title = soup.select('section > p > a')
    num = 1
    for n in new_title:
        title = n.get_text()
        link = n.get("href")
        print('--------'+title,link+'----------')
        #time.sleep(SLEEP_TIME)
        second = requests.get(link,headers= header).text
        soup2 = BeautifulSoup(second,'lxml')
        content = soup2.select("div #js_content > p[class]")
        file_id = "E:/test/%d %s.txt"%(num,title.strip('讲故事 | '))
        num += 1
        print('创建', file_id)
        with open(file_id,'w') as fd:
            for c in content:
                try:
                    fd.write(c.get_text().strip()+"\n")
                except:
                    print("!!!! "+link)
                    continue
else:
    print("访问异常")
    raise Exception