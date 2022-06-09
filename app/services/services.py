import requests
import untangle
from bs4 import BeautifulSoup


def rss(url, limit=999, detail=False):
    return_list = []
    res = requests.get(url)
    items = untangle.parse(res.text).rss.channel.item
    for idx, item in enumerate(items):
        if limit < idx:
            return return_list
        tmp = {}
        tmp['title'] = item.title.cdata
        tmp['link'] = item.guid.cdata
        if detail:
            link = item.guid.cdata
            if 'bbc' in url:
                tmp['content'] = bbc(link)
            elif 'cnn' in url:
                tmp['content'] = cnn(link)
        return_list.append(tmp)
    return return_list


def cnn(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    paras = soup.select('.zn-body__paragraph')
    t = ''
    for p in paras:
        t+=p.getText()
    return t

def bbc(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    paras = soup.select('.ssrcss-uf6wea-RichTextComponentWrapper')
    t = ''
    for p in paras:
        t+=p.getText()
    return t