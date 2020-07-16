#!/usr/bin/env python
# coding: utf-8

# In[95]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get(r"http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")
page_nr = int(soup.find_all("a", {"class":"Page"})[-1].text)
pag_lm = soup.find_all("div",{"class":"PaginationLimit"})
for line in pag_lm:
    n_prop = int(line.find_all("span")[1].text)   

base_url = r"http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
l = []

for page in range (0,(page_nr * n_prop), n_prop):
    print(base_url + str(page)+".html")
    r = requests.get(base_url + str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class":"propertyRow"})
    for item in all:
        d = {}
        d["Address"] = item.find_all("span", {"class", "propAddressCollapse"})[0].text.strip()
        try:
            d["Locality"] = item.find_all("span", {"class", "propAddressCollapse"})[1].text.strip()
        except:
            d["Locality"] = None
        d["Price"] = item.find("h4", {"class", "propPrice"}).text.strip()
        try:
            d["Beds"] = item.find("span", {"class", "infoBed"}).find("b").text.strip()
        except:
            d["Beds"] = None

        try:
            d["Area"] = item.find("span", {"class", "infoSqFt"}).find("b").text.strip()
        except:
            d["Area"] = None

        try:
            d["Full Baths"] = item.find("span", {"class", "infoValueFullBath"}).find("b").text.strip()
        except:
            d["Full Baths"] = None

        try:
            d["Half Baths"] = item.find("span", {"class", "infoValueHalfBath"}).find("b").text.strip()
        except:
            d["Half Baths"] = None

        for column_group in item.find_all("div", {"class", "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class":"featureGroup"}), column_group.find_all("span", {"class":"featureName"})):
                if "Lot Size".lower().strip() in feature_group.text.lower().strip():
                    d["Lot Size"] = feature_name.text.strip()
                    
        l.append(d)

df = pd.DataFrame(l)
df.to_csv("output.csv")

