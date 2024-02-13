#Web Scrap all the link H1B Visa Sponsor link 

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.myvisajobs.com/reports/h1b-4/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
urls = []
for link in soup.find_all('a'):
    new_link=str(link.get('href'))
    if new_link.startswith("/Visa-Sponsor"):
        new_link2="https://www.myvisajobs.com"+new_link
        urls.append(new_link2)

#Testing: check the url for Amazon urls
u_test = urls[0]
page = requests.get(u_test)
soup2 = BeautifulSoup(page.text, 'html.parser')
for index, td in enumerate(soup2.find_all('td')):
    
    if str(td.text) == "Hot H1B Visa Jobs:":
        location = soup2.find_all('td')[index+1]
        #print(str(location.text))

    
#Get all the **Hot H1B Visa Jobs** from all urls in Top 200 visa sponsor

collect_location=[]
for single_url in urls:
    location=None
    page_uni = requests.get(single_url)
    soup_uni = BeautifulSoup(page_uni.text, 'html.parser')


    for index, td in enumerate(soup_uni.find_all('td')):
        
        if str(td.text) == "Hot H1B Visa Jobs:":
            location = soup_uni.find_all('td')[index+1]
            collect_location.append(location.text)
            

    #Deal with the page with "Page Not Exist or Removed" or no location information
    if location is None:
        collect_location.append("Cannot find the location")



