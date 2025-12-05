import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import hashlib


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
    cService = webdriver.ChromeService(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service = cService)
    driver.get(url)
    sleep(10)
    elements = driver.find_elements(By.CLASS_NAME, "_metadataDetailsList_10sc3_653")
    for element in elements:
        # print(element.text)
        lis = element.find_elements(By.TAG_NAME, "li")
        for li in lis:
            if len(li.text) == 10 and all([lambda x: x.is_digit() for x in li.text]):
                return li.text
    return ""

parts = []

parts.append(voyager_date())
parts.append(rfc1149_date())
parts.append(brain_codepoint())
parts.append(btc_genesis_date())
parts.append(kr2_isbn10())

answer = f"FLAG{{{"-".join(parts)}}}"
print("Flag:  ", answer)
h = hashlib.new('sha256')
h.update(answer.encode('ascii'))
print("Hash:  ", h.hexdigest())
print("Is hash == d311f26ea1a995af669a62758ad5e0ce2583331059fbfc5c04cc84b2d41f4aed")
print(h.hexdigest() == "d311f26ea1a995af669a62758ad5e0ce2583331059fbfc5c04cc84b2d41f4aed")