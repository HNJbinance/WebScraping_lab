import requests
import pandas as pd

# get the data with the api key
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=x5862pdibrYRsFkpRgFWdzIEVVFhehst"
data_api = requests.get(url).json()


# Turn the data into a dataframe
data = pd.DataFrame(data_api)
# Drop unnescessary columns
dataframe = data[['rates']]
# Save the Dataframe
dataframe.to_csv("exchange_rates_1.csv")