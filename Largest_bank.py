'''this script will scrape the largest world bank capitalisation in the world from wiki and load into a dataframe the a json file '''

import bs4
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
import requests

def find_the_table(title:str, tables: list):
    for index, table in enumerate(tables):
        if title in str(tables):
            index_table = index
    return index

url = " https://en.wikipedia.org/wiki/List_of_largest_banks"
html_data = requests.get(url)

soup = BeautifulSoup(html_data.content, "html.parser")

tables = soup.find_all('table')

index_table = find_the_table("By market capitalization", tables)

dataframe = pd.DataFrame(columns=[ "Bank_name", "Market_cap"])

for row in tables[index_table].tbody.find_all("tr"):
    columns = row.find_all('td')
    if (columns != []) :
        Bank_name = columns[1].text.strip()
        Market_cap = columns[2].text.strip()
        dataframe = dataframe.append({"Bank_name": Bank_name, "Market_cap": Market_cap}, ignore_index=True)

data_json = dataframe.to_json("data_json")









