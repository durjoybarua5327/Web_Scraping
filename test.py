import requests
from bs4 import BeautifulSoup

response= requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers")

soup= BeautifulSoup(response.content,"html.parser")

