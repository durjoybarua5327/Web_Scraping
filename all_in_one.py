import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.tutorialsfreak.com/")
print(response)
print(response.status_code)

soup = BeautifulSoup(response.content , "html.parser")

"""
#tag
tag= soup.HTML


#nevigablestring
print(soup.p.string)

#comment
print(soup.prettify())

print("\n\n\n\n")

#all specific tag
paragraphs=soup.find_all("p")
for p in paragraphs:
    print(p.prettify())


print("\n\n\n\n")

#finding using class

print()
paragraph = soup.find('p', class_='fs-16 fw-400 lh-24 label-color-1 card-text')
for l in paragraph:
    print(l.text)


#link fetching
for i in soup.find_all("a"):
    print(i.get("href"))

"""
# image fetching
img = soup.find_all("img")
for i in img:
    print(i.get('src'))