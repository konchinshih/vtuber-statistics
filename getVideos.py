import requests, random, re, time, json
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agents_list = open("user-agent.txt", 'r').read().split('\n')[:-1]


baseUrl = 'https://virtual-youtuber.userlocal.jp'


def toInt(x: str):
    match = re.findall("[0-9]", x)
    ret = ""
    for i in match:
        ret += i
    return ret

user_agent = random.choice(user_agents_list)
def get(url: str):
    time.sleep(5)
    print(f"Get {url} user-agent: {user_agent}")
    ret = requests.get(url, headers={'User-Agent': user_agent})
    with open("output", 'w', encoding='utf8') as file:
        file.write(ret.text)
    return ret

def findChannel(text: str):
    return re.search('''<span\ itemprop="author"\ itemscope\ itemtype="http://schema\.org/Person"><link\ itemprop="url"\ href="(http://www\.youtube\.com/@.*?)">''', text)

def findVideo(text: str):
    return re.search('''"videosCountText":\{"runs":\[\{"text":"([0-9]*?)"\}''', text)

with open("result.json", 'r', encoding='utf8') as jfile:
    vtubers = json.load(jfile)

for userid in vtubers:
    if 'video' in vtubers[userid]:
        continue
#   Get the html
    user_agent = random.choice(user_agents_list)
    res = get(f"{baseUrl}{userid}")
    soup = bs(res.text, 'html.parser')

#   Find the data
    yturl = soup.find('a', {'class': "btn btn-youtube btn-raised text-capitalize"})
    if yturl:
        yturl = soup.find('a', {'class': "btn btn-youtube btn-raised text-capitalize"})['href']
        ytres = get(yturl)
    
        churl = findChannel(ytres.text)
        if churl == None:
            print(f"{vtubers[userid]['name']} failed.")
            with open("fail.log", 'a', encoding='utf8') as file:
                file.write(userid+'\n')
            continue
        churl = churl.group(1)
        churl = findChannel(ytres.text).group(1)
        chres = get(churl)


        video = findVideo(chres.text)
        if video == None:
            print(f"{vtubers[userid]['name']} failed.")
            with open("fail.log", 'a', encoding='utf8') as file:
                file.write(userid+'\n')
            continue
        video = video.group(1)

        print(vtubers[userid]['name'], video)
        vtubers[userid]['video'] = video
    

#   Save the data
        with open("result.json", 'w', encoding='utf8') as jfile:
            json.dump(vtubers, jfile, indent=4)

