<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.tutorialsfreak.com/")
print(response)
print(response.status_code)

soup = BeautifulSoup(response.content , "html.parser")


# in this ep we will see how to pull only text from code only text 
# it's too easy we will use text attribute of BeautifulSoup 

print(soup.text)

# we can use this for specific tag also 

print("\n\n\n\n\n")
heading = soup.h1
=======
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.tutorialsfreak.com/")
print(response)
print(response.status_code)

soup = BeautifulSoup(response.content , "html.parser")


# in this ep we will see how to pull only text from code only text 
# it's too easy we will use text attribute of BeautifulSoup 

print(soup.text)

# we can use this for specific tag also 

print("\n\n\n\n\n")
heading = soup.h1
>>>>>>> c834a84429e2884b7d393b60c550d04c027ba19e
print(heading.text)