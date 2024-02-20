from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#get all the information from url
def get_sponsor_url(url):
    page = requests.get(url)
    #pulling the information
    soup = BeautifulSoup(page.text, 'html')
    return soup

#get "visa sponsor name" from the page
def get_visa_sponsors(soup):
    
    table = soup.find_all('table')[0]

    #Column name
    df_columns = [name.text.strip("* ") for name in table.find_all('td')[0:4]]

    #Value
    individual = [name.text.strip("* ") for name in table.find_all('td')[4:]]
    individual.remove("")   
    reshape_individual = [individual[i:i+4] for i in range(0, len(individual),4)]

    return df_columns, reshape_individual

#get Top200 visa from 4 urls
job_list = []
collect_jobs=[]
for index,u in enumerate(['','-2','-3','-4']):
    url = 'https://www.myvisajobs.com/reports/h1b'+ u +'/'
    soup=get_sponsor_url(url)
    col,individual_val=get_visa_sponsors(soup)

    # only create dataframe once in the first url
    if index==0:
        df2 = pd.DataFrame(columns=col)
    
    # except the first url, add other urls into the dataframe 
    for val in individual_val:   
        length = len(df2)
        df2.loc[length]=val

    # import the result from "web_scraping_details.py"
    # find all the urls in the main page
    urls = []
    for link in soup.find_all('a'):
        new_link=str(link.get('href'))
        if new_link.startswith("/Visa-Sponsor"):
            #create new link to get the complete website address
            new_link2="https://www.myvisajobs.com"+new_link
            urls.append(new_link2)
    
    #focus on a singel company, and get the certain information
    for single_url in urls:
        jobs=None
        page_uni = requests.get(single_url)
        soup_uni = BeautifulSoup(page_uni.text, 'html.parser')


        for index, td in enumerate(soup_uni.find_all('td')):
            
            if str(td.text) == "Hot H1B Visa Jobs:":
                jobs = soup_uni.find_all('td')[index+1]
                jobs_str=jobs.text
                jobs_str='), '.join(jobs_str.split(") "))
                collect_jobs.append(jobs_str)
                

        #Deal with the page with "Page Not Exist or Removed" or no location information
        if jobs is None:
            collect_jobs.append("Cannot find the location")

df2["Hot H1B Visa Jobs"]=collect_jobs


print(df2)

#Create the dataframe for customization
df_cus=df2.copy()

x=input("what is the position")
filtered_df = df_cus[df_cus["Hot H1B Visa Jobs"].str.contains(x)]
print(filtered_df)
