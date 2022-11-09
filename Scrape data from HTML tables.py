''' scrape data from IBM and transform it into dataframe '''
# this module helps us scrape the web page, pulling data out of HTML and XML files, we will focus on HTML files
from bs4 import BeautifulSoup

# this module helps us download the web page
import requests

#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# get the contents of the webpage in text format and store in a variable called data
data = requests.get(url).text

# transform the data into a BeautifulSoup Object
soup = BeautifulSoup(data, "html.parser")

# find all the tables in the web page
table_bs = soup.find('table')

for row in table_bs.find_all('tr'): # in html rows are tagged with tr tag
    # Get all columns in each row.
    cols = row.find_all('td') # in html columns are tagged with td tag
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the code in column 4 as color_code
    print("{}----------------------{}".format(color_name, color_code))