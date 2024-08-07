import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.tutorialsfreak.com/")
print(response)
print(response.status_code)

soup = BeautifulSoup(response.content , "html.parser")


# in this episode we will show you how to pull link 

img = soup.find_all("img")
# hence there can many images that's why will will terminate a loop


for i in img:
    #we know that in img tag there is a src where the link provide
    print(i.get("src"))


# as well as we can pull link from ancher(a) 
# in ancher tag link privide in href 
print("\n\n\n\n")
ancher= soup.find_all("a")
for a in ancher:
    print(a.get("href"))