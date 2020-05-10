import requests
from bs4 import BeautifulSoup
import re
'''def fate_proxy():
    resp=requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
    #print(resp.text)
    a=((resp.text).split('\n'))
    #print(a)
    p_list=[]
    for i in a:
        try:
            p_list.append(json.loads(i))
        except Exception as e:
            continue
    #print(p_list)
    np_list=[]
    for i in p_list:
        if i['country']=='IN':
            np_list.append(i)
    proxy=[]
    fast_proxy=sorted(np_list,key=lambda k: k['response_time'])
    for p in fast_proxy:
      proxy.append(str(p['host'])+':'+str(p['port']))
    return proxy'''


def present():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    }
    url='https://www.codechef.com/contests'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,"lxml")
    contest = soup.find_all('table',{"class":"dataTable"})
    contest = contest[0].find_all('tbody')
    #contest = contest[0].find_all('tr')
    name = []
    link = []
    code = []
    sdate = []
    edate = []
    stime = []
    etime = []
    j = 0
    for i in contest[0].findAll('a', attrs={'href': re.compile("^/")}):
        link.append('https://www.codechef.com'+i.get('href'))
    for i in contest[0].findAll('a'):
        name.append(i.text)
    for i in contest[0].findAll('td'):
        if(j%4==2):
            sdate.append(i.text[:-10])
            stime.append(i.text[-8:])
        if(j%4==0):
            code.append(i.text)
        if (j % 4 == 3):
            edate.append(i.text[:-10])
            etime.append(i.text[-8:])
        j+=1
    #print(stime)
    out=[]
    for i in range(len(name)):
        d = {}
        d.update({'code':code[i],'name':name[i],'link':link[i],'sdate':sdate[i],'edate':edate[i],'stime':stime[i],'etime':etime[i]})
        out.append(d)
        #print(out)
        #print(d)
#pot()
    return out


def future():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    }
    url='https://www.codechef.com/contests'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,"lxml")
    contest = soup.find_all('table',{"class":"dataTable"})
    contest = contest[1].find_all('tbody')
    #contest = contest[0].find_all('tr')
    name = []
    link = []
    code = []
    sdate = []
    edate = []
    stime = []
    etime = []
    j = 0
    for i in contest[0].findAll('a', attrs={'href': re.compile("^/")}):
        link.append('https://www.codechef.com'+i.get('href'))
    for i in contest[0].findAll('a'):
        name.append(i.text)
    for i in contest[0].findAll('td'):
        if(j%4==2):
            sdate.append(i.text[:-10])
            stime.append(i.text[-8:])
        if(j%4==0):
            code.append(i.text)
        if (j % 4 == 3):
            edate.append(i.text[:-10])
            etime.append(i.text[-8:])
        j+=1
    #print(stime)
    out=[]
    for i in range(len(name)):
        d = {}
        d.update({'code':code[i],'name':name[i],'link':link[i],'sdate':sdate[i],'edate':edate[i],'stime':stime[i],'etime':etime[i]})
        out.append(d)
        #print(out)
        #print(d)
#pot()
    return out

def past():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
    }
    url='https://www.codechef.com/contests'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,"lxml")
    contest = soup.find_all('table',{"class":"dataTable"})
    contest = contest[2].find_all('tbody')
    #contest = contest[0].find_all('tr')
    name = []
    link = []
    code = []
    sdate = []
    edate = []
    stime = []
    etime = []
    j = 0
    for i in contest[0].findAll('a', attrs={'href': re.compile("^/")}):
        link.append('https://www.codechef.com'+i.get('href'))
    for i in contest[0].findAll('a'):
        name.append(i.text)
    for i in contest[0].findAll('td'):
        if(j%4==2):
            sdate.append(i.text[:-10])
            stime.append(i.text[-8:])
        if(j%4==0):
            code.append(i.text)
        if (j % 4 == 3):
            edate.append(i.text[:-10])
            etime.append(i.text[-8:])
        j+=1
    #print(stime)
    out=[]
    for i in range(len(name)):
        d = {}
        d.update({'code':code[i],'name':name[i],'link':link[i],'sdate':sdate[i],'edate':edate[i],'stime':stime[i],'etime':etime[i]})
        out.append(d)
        #print(out)
        #print(d)
#pot()
    return out