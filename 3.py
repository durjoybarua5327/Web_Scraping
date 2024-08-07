
import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites"
response= requests.get(url)
print(response.status_code,"\n\n")


soup=BeautifulSoup(response.content,"html.parser")
print(soup)
"""
if we terminate only the upper code we will get html code in mess up / mismanage way
there is a attribute of Beautiful soup that is prettify which will decorate our pulled html code
which look really in which way they supposed to

"""
#just run the code you will be able to see the differences
print("\n\n\n\n")
print(soup.prettify)
