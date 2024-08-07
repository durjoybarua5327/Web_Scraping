# in first file we have already learn how to get response
# now we will learn how to fetch all these html code from that particular web page
# for fetching/pulling html code we need a module which is BeautifulSoup

import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites"
response= requests.get(url)
print(response.status_code,"\n\n")

#if we use one of the attribute of requests content
#if we run this we will see that all code have been fetch but we need only html code
#that time we use BeautifulSoup module
print(response.content)
print("\n\n\n\n\n")
#Now, we will pull all the HTML code according to the URL
soup=BeautifulSoup(response.content,"html.parser")
print(soup)
