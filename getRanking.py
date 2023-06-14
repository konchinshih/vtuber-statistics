import requests, random, re, time, json
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd

user_agents_list = open("user-agent.txt", 'r').read().split('\n')


baseUrl = 'https://virtual-youtuber.userlocal.jp/document/ranking?page='

def toInt(x: str):
    match = re.findall("[0-9]", x)
    ret = ""
    for i in match:
        ret += i
    return ret

def get(url: str):
    time.sleep(5)
    return requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})

vtubers = {}

for i in range(1, 40+1):
#   Get the html
    res = get(f"{baseUrl}{i}")
    soup = bs(res.text, 'html.parser')

#   Find the data
    data = soup.find(
        'div', {'class': "container container-noamp my-3 px-0"}
    ).find('table').tbody.find_all('tr')

#   Convert to JSON
    for element in data:
        userid = element['data-href'].replace('\n', '').replace(' ', '')

        vtubers[userid] = {}

        vtubers[userid]['name'] = element.find(
            'td', {'class': "col-name"}
        ).find(
            'a', {'href': userid, 'class': "no-propagation"}
        ).getText().replace('\n', '').replace(' ', '')

        if element.find('div', {'class': "box-office"}) != None:
            vtubers[userid]['office'] = element.find('div', {'class': "box-office"}).find('a').getText()

        vtubers[userid]['fan'] = toInt(element.find('span', {'class': "text-success font-weight-bold"}).getText())

        vtubers[userid]['view'] = toInt(element.find('span', {'class': "text-danger font-weight-bold"}).getText())

        print(vtubers[userid]['name'])


with open("result.json", 'w', encoding='utf8') as jfile:
        json.dump(vtubers, jfile, indent=4)

