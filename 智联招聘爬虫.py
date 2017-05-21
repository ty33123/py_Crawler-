#-*- coding: UTF-8 -*-
import re
import urllib.request
import csv
import codecs
from bs4 import BeautifulSoup

global url
print('请输入爬取地址：')
url=input()
global html
html=urllib.request.urlopen(url).read()
global soup
soup=BeautifulSoup(html,'html5lib')
global add
add=r"d:\11111.csv"
def dq():
    global add
    #---------------职位--------------------------

    zwmc=soup.findAll(class_='zwmc')

    zhiwei=[];#职位名称
    for i in range(1,len(zwmc)):
        zhiwei.append(zwmc[i].a.string)

    zhiweilj=[];#职位链接
    for i in range(1,len(zwmc)):
        zhiweilj.append(zwmc[i].a.get("href"))

    #-----------------公司------------------------

    gsmc=soup.findAll(class_='gsmc')
    gongsi=[];#公司名称
    for i in range(1,len(gsmc)):
        gongsi.append(gsmc[i].a.string)
    gongsilj=[];#公司链接
    for i in range(1,len(gsmc)):
        gongsilj.append(gsmc[i].a.get("href"))

    #-------------------薪资----------------------

    zwyx=soup.findAll(class_='zwyx')
    yuexin=[];
    for i in range(1,len(zwyx)):
        yuexin.append(zwyx[i].string)

    #-----------------工作地点------------------------
    gzdd=soup.findAll(class_='gzdd')
    didian=[];
    for i in range(1,len(gzdd)):
        didian.append(gzdd[i].string)
    #--------------性质、规模、学历----------------------
    xxjs=soup.findAll(class_="newlist_deatil_two")
    xingzhi=[];


    guimo=[];


    xueli=[];


    for i in range(0,len(xxjs)):
        xingzhi.append(xxjs[i].contents[1].string[5:])
        guimo.append(xxjs[i].contents[2].string[5:])
        xueli.append(xxjs[i].contents[3].string[3:])
            



    #------------------职务描述-----------------------

    zwms=soup.findAll(class_="newlist_deatil_last")
    miaoshu=[];
    for i in range(0,len(gzdd)-1):
        miaoshu.append(zwms[i].string)

    #------------------发布时间-----------------------
    gxsj=soup.findAll(class_="gxsj")
    shijian=[];
    for i in range(1,len(gxsj)):
        shijian.append(gxsj[i].span.string)

    #------------------保存-----------------------
    csvFile = open(add, "a", newline='')
    writer = csv.writer(csvFile)
    for i in range(0,60):
        try:
            
            s=[repr(zhiwei[i]).strip('\''),repr(zhiweilj[i]).strip('\''),repr(gongsi[i]).strip('\''),repr(gongsilj[i]).strip('\''),repr(yuexin[i]).strip('\''),repr(didian[i]).strip('\''),
                repr(xingzhi[i]).strip('\''),repr(guimo[i]).strip('\''),repr(xueli[i]).strip('\''),repr(miaoshu[i]).strip('\''),repr(shijian[i]).strip('\'')]
            writer.writerow(s)
        except UnicodeEncodeError:
                pass

    csvFile.close()
    print("数据追加成功！")


def indx():
    csvFile = open(r"d:\zhilian.csv", "a", newline='')
    writer = csv.writer(csvFile)
    writer.writerow(['职位名称','职位链接','公司名称','公司链接','职位月薪','工作地点','公司性质','公司规模','学历要求','职务描述','发布日期'])
    csvFile.close()
    print("写入标题成功！")

def nxt():
    global soup
    global html
    global url
    next=soup.findAll(class_="next-page")
    url=next[0].get("href")
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html,'html5lib')


    
i=1;
print('请输入总爬取页数：')
n=int(input())
indx()
while(i<=n):
    print("正在爬取第"+str(i)+"页")
    dq()
    nxt()
    i=i+1

print('--------------爬取完毕-------------')
