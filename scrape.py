import bs4 as bs
import urllib.request
import os.path
from nytimesarticle import articleAPI
from time import sleep


        # print(url_list)
# Add your API key over here.

#apis = ['4ca755df21fd4011a1e98f306cd2adef','ec36494e9e844996b49623f677fe683e','50f17c8215ba4113986c28bcc8f39bac','20f453825bfa4fadbfbf5cbc007dabab']
# The query word is used to get the type of data you want.
# In this particular case we get articles that contain Obama.
# Refer http://dlab.berkeley.edu/blog/scraping-new-york-times-articles-python-tutorial for more details.

categories = ['Sports','Business','Technology','Politics']


# Append all web_urls from the data received.


# print(url_list)
for i in range(4):
    cat = categories[i]
    sleep(5)
    if cat == 'Politics':
        api = articleAPI('4ca755df21fd4011a1e98f306cd2adef')
        path = '/Users/adityakishanankaraboyana/CSE487Spring2018/lab3/'+categories[i]
        articles = api.search(q="Obama")
        url_list=[]
        for data in articles['response']['docs']:
            url_list.append(data['web_url'])
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(0,len(url_list)):
            file_name = 'data'+str(i)+'.txt'
            completeName = os.path.join(path,file_name)
            f = open(completeName,'w')
            sauce = urllib.request.urlopen(url_list[i]).read()
            soup = bs.BeautifulSoup(sauce,'lxml')
            for paragraph in soup.find_all('p'):
                f.write(paragraph.text)
            f.close()
    if cat == 'Business':
        api = articleAPI('4ca755df21fd4011a1e98f306cd2adef')
        path = '/Users/adityakishanankaraboyana/CSE487Spring2018/lab3/'+categories[i]
        articles = api.search(q="Bonds")
        url_list=[]
        for data in articles['response']['docs']:
            url_list.append(data['web_url'])
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(0,len(url_list)):
            file_name = 'data'+str(i)+'.txt'
            completeName = os.path.join(path,file_name)
            f = open(completeName,'w')
            sauce = urllib.request.urlopen(url_list[i]).read()
            soup = bs.BeautifulSoup(sauce,'lxml')
            for paragraph in soup.find_all('p'):
                f.write(paragraph.text)
            f.close()
    if cat == 'Technology':
        api = articleAPI('4ca755df21fd4011a1e98f306cd2adef')
        path = '/Users/adityakishanankaraboyana/CSE487Spring2018/lab3/'+categories[i]
        articles = api.search(q="Amazon")
        url_list=[]
        for data in articles['response']['docs']:
            url_list.append(data['web_url'])
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(0,len(url_list)):
            file_name = 'data'+str(i)+'.txt'
            completeName = os.path.join(path,file_name)
            f = open(completeName,'w')
            sauce = urllib.request.urlopen(url_list[i]).read()
            soup = bs.BeautifulSoup(sauce,'lxml')
            for paragraph in soup.find_all('p'):
                f.write(paragraph.text)
            f.close()
    if cat == 'Sports':
        api = articleAPI('4ca755df21fd4011a1e98f306cd2adef')
        path = '/Users/adityakishanankaraboyana/CSE487Spring2018/lab3/'+categories[i]
        articles = api.search(q="Trump")
        url_list=[]
        for data in articles['response']['docs']:
            url_list.append(data['web_url'])
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(0,len(url_list)):
            file_name = 'data'+str(i)+'.txt'
            completeName = os.path.join(path,file_name)
            f = open(completeName,'w')
            sauce = urllib.request.urlopen(url_list[i]).read()
            soup = bs.BeautifulSoup(sauce,'lxml')
            for paragraph in soup.find_all('p'):
                f.write(paragraph.text)
            f.close()
