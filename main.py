import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime


def voyager_date(): #https://science.nasa.gov/mission/voyager/voyager-1/
    url = "https://science.nasa.gov/mission/voyager/voyager-1/"
    req = requests.get(url)
    src = req.text
    soup = bs(src, "html.parser")
    date = soup.find(string="launch").parent.parent.next_sibling.next_sibling.text
    date = date.replace(".", "").replace(",", "").split(" ")
    date = f"{date[0][:3]} {date[1].zfill(2)} {date[2]}" 
    return datetime.strptime(date, "%b %d %Y").strftime("%Y%m%d")


def rfc1149_date(): #https://datatracker.ietf.org/doc/rfc1149/
    url = "https://datatracker.ietf.org/doc/rfc1149/"
    req = requests.get(url)
    src = req.text
    soup = bs(src, "html.parser")
    date = soup.find("div", class_ = "card-body").pre.text
    date = date.split("\n")[2].split()
    date = f"{date[0].zfill(2)} {date[1]} {date[2]}" 
    return datetime.strptime(date, "%d %B %Y").strftime("%Y%m%d")


def brain_codepoint(): #https://unicode.org/Public/emoji/latest/emoji-test.txt
    url = "https://unicode.org/Public/emoji/latest/emoji-test.txt"
    req = requests.get(url)
    src = req.text
    s = src[:src.index("brain")]
    return s[s.rfind("\n") + 1:s.rfind("\n") + 6]


def btc_genesis_date(): #https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp
    url = "https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp"
    req = requests.get(url)
    src = req.text
    CMainParams = src[src.index("class CMainParams"):]
    genesis = CMainParams[CMainParams.index("genesis"):]
    date = genesis[genesis.index("(") + 1:genesis.index(",")]
    return datetime.fromtimestamp(int(date)).strftime("%Y%m%d")


def kr2_isbn10(): #https://search.catalog.loc.gov/instances/9acb1e70-9ea7-5ec1-9e9e-4d1e8b6d865e?option=lccn&query=88005934
    url = "https://search.catalog.loc.gov/instances/9acb1e70-9ea7-5ec1-9e9e-4d1e8b6d865e?option=lccn&query=88005934"
    req = requests.get(url)
    src = req.text
    return src

# print(voyager_date())
# print(rfc1149_date())
# print(brain_codepoint())
# print(btc_genesis_date())
print(kr2_isbn10())
