import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.tutorialsfreak.com/")
print(response)
print(response.status_code)

soup = BeautifulSoup(response.content , "html.parser")


"""
Now we will show you how pull  only specific code like tag, class, div
(a, p, img, h1,h2..........)

"""
#if we use this we will get first ancher as output similary others tag
print(soup.a)

print("\n\n\n")

#we can easily understand that if we use find_all attribute we will get all that specific code 
paragraphs=soup.find_all("p")
#hence there will be may p tag so there we need a loop to print all these
for i in paragraphs:
    print(i.prettify())

#now we will learn how to pull specific class name
ancher = soup.find("class", class_="row test-site")
print(ancher)