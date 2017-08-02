import requests
import re
from bs4 import BeautifulSoup
import urllib

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status
        return r.text
    except:
        return ""

def Parse_Head(html_text):  #　解析搞笑吧首页数据提取详情页的url
    soup=BeautifulSoup(html_text,"html.parser")
    v_dic={}
    count=0  #　用于记录主页中总共有多少个包含视频的详情页
    for tag in soup.find_all('div',class_="threadlist_lz clearfix"):
        clawed=0  # 用于标示该url是否已经爬取过( 1=yes )
        child_url=tag.find('a').get('href')
        child_name=tag.find('a').get_text()  #　获得详情页的帖子名称
        result,number=re.subn('【.*】','',child_name)  #使用正则表达式去除名称中的"【ｘｘｘ】"
        child_name=result
        with open('./clawedUrls.txt','r') as f:  # 与clawedUrls.txt文件中保存的原始url进行对比，排除重复以免重复下载文件
                for line in f.readlines():
                    line = line.strip()
                    if line==child_url:
                        print("已爬取过该视频，跳过！")
                        clawed=1  # 代表已经爬取过该url
                        break
                    else:  #与当前行不匹配，不做处理
                        print('Matching clawedUrls.txt...')
        if clawed==0 :  #未爬取过该url的话，则进行访问并爬取
            Parse_child_Download(child_url,child_name,count)  # 对详情页进行访问
            with open('./clawedUrls.txt','a') as f:  # 将该爬取过后的url加入clawedUrls.txt文件中保存
                f.write(child_url+'\n')
            count=count+1
            print(count)
        clawed=0
        
def Parse_child_Download(child_url,child_vname,count):  #　解析详情页的链接并下载视频,传入的参数分别是详情页的ｕｒｌ和视频的名称
    r=requests.get('https://tieba.baidu.com'+child_url)  # 得到详情页源码
    soup=BeautifulSoup(r.text,'html.parser')
    for tag in soup.find_all('div',class_='video_src_wrapper'):
        p=re.compile(r"vhsrc=\".*\" w")  # 以下为利用正则进行视频链接的提取
        m=p.search(r.text)
        #print(m.group(0)) # 打印匹配到的“不完美”的视频链接
        # 进一步处理链接得到真正的视频链接，去除多余的部分
        result,number=re.subn('vhsrc="','',m.group(0))
        result2,number2=re.subn('" w','',result)
        real_url=result2
        print(count)  #　计数变量
        print("开始下载视频...")
        urllib.request.urlretrieve(real_url,'%s.mp4'%(child_vname))

def main():
    url="https://tieba.baidu.com/f?kw=%B8%E3%D0%A6%CA%D3%C6%B5&fr=ala0&tpl=5"
    html_text=getHTMLText(url)
    Parse_Head(html_text)

main()

