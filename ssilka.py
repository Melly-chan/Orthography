
import requests
import json
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

enterurl = link
domain = urlparse(enterurl).netloc
if (int(domain.find("www."))!=-1):
    domain = domain[4:]

url = enterurl.split("//")[-1].split("/")[0].split('?')[0]
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

    print(YELLOW + " - There Is A Problem" + CEND)
    print(YELLOW + " - Checking The Connection " + CEND)
    print(YELLOW + " - Enter Website Without HTTP/HTTPS/WWW " + CEND)
    print(YELLOW + " - Check If Website Working " + CEND)
