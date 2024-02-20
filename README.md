# web-scrap-top200-visasponsor

## The project goal:
Understand the practice of web scrapping for table

## Introduction:
Using BeautifulSoup and requests, the package from Python, to get the dataframe for Top 200 H-1B Visa Sponsors 2024. </br>
After getting this table with 200 rows, I am planning to make further analysis based on this result.

Resource: myvisajobs.com

## Problem-Solving:
1. Found that one of the urls return error due to the error message of  **page not exist or remove**
#Deal with the page with "Page Not Exist or Removed" or no location information
if jobs is None:
    collect_jobs.append("Cannot find the location")
