
from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urlparse

link = str(input())
req = requests.get(link).text
soup = BeautifulSoup(req, "lxml")
head = soup.find('head')
zagolovok = head.find('title').text
textp = soup.find_all('div', attrs={'class':"article__text"})
if (len(textp))==0:
    textp = soup.find_all('span', attrs={'class':'intro'})
if (len(textp))==0:
    text = soup.find_all('span', attrs={'class': 'intro'})
if(len(textp))==0:
    textp = soup.find_all('p')
data = soup.find_all('time')
if len(data)==0:
    data = soup.find_all('span', attrs={'class': 'article__info-date-modified'})

print(zagolovok)

for i in range(len(textp)):
    print(textp[i].text)
if len(data)!=0:
    for i in range(len(data)):
        print(data[i].text)
else:
    print("дата публикации на новстоном ресусре не указана")

domain = urlparse(link).netloc
if (int(domain.find("www."))!=-1):
    domain = domain[4:]

url = link.split("//")[-1].split("/")[0].split('?')[0]
show = "https://input.payapi.io/v1/api/fraud/domain/age/" + domain

r = requests.get(show)
soupp = BeautifulSoup(r.text, "lxml")

if r.status_code == 200:

    age = soupp.find('body').text
    str = int(age.find("Reg"))
    end= int(age.find("}"))
    print (age[str:(end-1)])

    data = r.text
    jsonToPython = json.loads(data)
else:

    print(" - There Is A Problem")
    print(" - Checking The Connection")
    print(" - Check If Website Working ")
textpp=""
for i in range(len(textp)):

    a = textp[i].text
    textpp = textpp + a
words = 0
for i in range(len(textpp)):
    if (textpp[i]==" "):
        words =float(words + 1)
from spellchecker import SpellChecker
import pandas as pd

spell = SpellChecker()
data = textpp

count=0
misspelled = spell.unknown(data)

for word in misspelled:
    a=(spell.correction(word))
    count = count + 1
misspelled = spell.unknown(textpp)
for word in misspelled:

    print(spell.correction(word))


count=float(count)
proc = count/words*100
print(proc, '%')





