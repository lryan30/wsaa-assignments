# Assignment 03:
# This program retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
# and stores it into a file called "cso.json". 
# Author: LR

import requests  
import json

# URL to retrieve the Exchequer Account Historical Series dataset in JSON-stat format
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Send GET request to retrieve the data from the URL. 
response = requests.get(url)
    
data = response.json()   
 
with open('cso.json', "w") as json_file: # open the file in write mode which creates the file.
        json.dump(data, json_file, indent=4)  # json dump is used to write the data to the file in json format

print(f"Data has been saved in cso.json")

    



# References: 
# https://data.cso.ie/
# https://data.gov.ie/dataset/fiq02-exchequer-account-historical-series
# https://www.w3schools.com/python/python_json.asp







