import requests
from bs4 import BeautifulSoup

import pandas as pd
response = requests.get("https://www.iplt20.com/auction/2022")
print(response)
print(response.status_code)


#  use lxml instead of html.paser because lxml is more efficient and faster than html.parser

soup = BeautifulSoup(response.text , "lxml")

#in this file we will learn how to fetch table data
table = soup.find("table", class_="ih-td-tab auction-tbl")
table_head= table.find_all("th")
header=[]
for i in table_head:
    header.append(i.text)


data_frame = pd.DataFrame(columns= header)


rows = table.find_all("tr")
for i in rows[1:]:

    first_td= i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip() # uses text beacause strip function is use for removing extra string spaces

    data=i.find_all("td")[1:]
    row=[tr.text for tr in data]
    row.insert(0,first_td)
    l= len(data_frame)
    data_frame.loc[l]=row

print(data_frame)
data_frame.to_csv("F:/Web_Scraping/ipl_auction_data.csv")