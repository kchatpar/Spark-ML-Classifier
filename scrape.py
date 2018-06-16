#This script was designed by Krishna Chatpar
#This script uses the keywords Obama, Bonds, Amazon, and Warriors
#to gather articles in the respective categories of: Politics, Finance, Business, and Sportsself.
#Each article is written to a text file in it's respective folder
#

from bs4 import BeautifulSoup
#import urllib.request
#import os.path
from nytimesarticle import articleAPI
from time import sleep


categories = ['Sports','Business','Technology','Politics']

#Loop through each of the four categories and scrape the articles
#Each article is stored in it's own labeled sub folder in a respective file

for i in range(4):
    cat = categories[i]
    sleep(5)
    if cat == 'Politics':
        api = articleAPI('4ca755df21fd4011a1e98f306cd2adef')
        path = '/Users/krishnachatpar/Desktop/Github/Articles/'+categories[i]
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
        path = '/Users/krishnachatpar/Desktop/Github/Articles/'+categories[i]
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

        path = '/Users/krishnachatpar/Desktop/Github/Articles/'+categories[i]
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
        path = '/Users/krishnachatpar/Desktop/Github/Articles/'+categories[i]
        articles = api.search(q="Warriors")
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
