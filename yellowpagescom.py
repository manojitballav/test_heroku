import requests
from bs4 import BeautifulSoup
url = raw_input("Enter the url of the website: ")
r = requests.get(url)
soup = BeautifulSoup(r.content,"html5lib")
links = soup.find_all("a")
g_data = soup.find_all("div",{"class":"info"})
for item in g_data:
    print item.contents[0].find_all("a",{"class":"business-name"})[0].text
    try:
        print item.contents[1].find_all("span",{"itemprop":"streetAddress"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span",{"itemprop":"addressLocality"})[0].text.replace(',','')
    except:
        pass
    try:
        print item.contents[1].find_all("span",{"itemprop":"addressRegion"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("span",{"itemprop":"postalCode"})[0].text
    except:
        pass
    try:
        print item.contents[1].find_all("li",{"class":"primary"})[0].text
    except:
        pass
    print ""
    