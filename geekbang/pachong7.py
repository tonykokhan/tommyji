from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    # "Accept-Encoding": "deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; gauges_unique_day=1; gauges_unique_month=1; gauges_unique_year=1; gauges_unique=1",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

# url = 'http://www.infoq.com/cn/news'      # 链接已失效
# url = 'http://www.infoq.com/news/'

url = 'https://xnews.jin10.com/'
# url = 'https://xnews.jin10.com/page/1'      # 同上


# 取得新闻标题
def craw2(url):
    response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    for title_href in soup.find_all('div', class_='news-i-content'):
        # print(title_href)
        # for title in title_href.find_all('div'):
        #     if title.get('title'):
        #         # print(title)
        #         print(title.get('title'))
        print([title.get('title') for title in title_href.find_all('div') if title.get('title')])     # 列表推导式


craw2(url)


# 翻页
for i in range(2, 20):
    url = 'https://xnews.jin10.com/page/' + str(i)
    # print(url)
    craw2(url)
