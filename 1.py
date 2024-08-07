#Now i will show you how to get reponse from a web 
# if you get 200 as response that't mean you can use that web addresses data without ant interection
"""
Informational responses (100-199)
Successful responses (200-299)
Redirects (300-399)
Client errors (400 - 499)
Server errors (500-599)

"""
#for sending the request to the respective web we need a module which is requests
import requests

url="https://www.aljazeera.com/news/liveblog/2024/8/6/bangladesh-protests-live-news-students-leaders-to-meet-army-chief"

response= requests.get(url)

print(response)
#print(response.status_code)
