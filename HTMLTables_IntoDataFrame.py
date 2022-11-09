''' scrape data from wikipedia and transform it into dataframe '''
# this module helps us scrape the web page, pulling data out of HTML and XML files, we will focus on HTML files
from bs4 import BeautifulSoup

# this module helps us download the web page
import requests

#transfom data into dataframe
import pandas as pd

#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"

# get the contents of the webpage in text format and store in a variable called data
data = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>
# we can see how many tables were found by checking the length of the tables list
len(tables)

# we are looking for the 10 most populated countries tab
for index, table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        index_table = index
print(index_table)
#rint(tables[index_table].prettify())

population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[index_table].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

print(population_data)
