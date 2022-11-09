''' scrape data from IBM and transform it into dataframe '''
# this module helps us scrape the web page, pulling data out of HTML and XML files, we will focus on HTML files
from bs4 import BeautifulSoup

# this module helps us download the web page
import requests

url = "http://www.ibm.com"

# get the web data into a text format and store it into data variable
data = requests.get(url).text


# transform the data into a BeautifulSoup Object
data_bs = BeautifulSoup(data, "html.parser")

# scrape all the links in the url giver, in html anchor/link is represented by a tag

for link in data_bs.find_all('a', href=True):
    print(link.get('href'))

#scrape all the img tags

for link in data_bs.find_all('img'):
    print(link)
    print(link.get('img'))