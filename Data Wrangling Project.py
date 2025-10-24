100 largest companies by revenue in 2025 (mostly for fiscal year 2024) / Data Wrangling Project

# install packages [BeautifulSoup: parse + extract data from hmtl content]
from bs4 import BeautifulSoup
# [requests: used to send HTTP requests to websites]
import requests

# Define the target URL to scrape data
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

# Wikipedia Thinks im a Robot ... Time for Copilot
import requests
from bs4 import BeautifulSoup

# Define the target URL
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Use a more complete headers dictionary
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# Send the request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Page loaded successfully!")
else:
    print(f"Failed to load page. Status code: {response.status_code}")
    
# "Great success" - Borat
print(soup) 

# Filter to find the Table
soup.find_all('table')

# Rank to further Filter, Where Rank Describes Order it Appears / Class = 'wikitable sortable '
soup.find_all('table')[0]

table = soup.find_all('table')[0]
print(table)

# Soup = Entirety , Table = Relevant
# Lets get rid of the <th> Tags attached to or Headings
table.find_all('th')

world_titles = table.find_all('th')
print(world_titles)

world_table_titles = [title.text for title in world_titles]
print(world_table_titles)

# Lets get rid of /n 
world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)

# Titles ready for Dataframe
import pandas as pd

df = pd.DataFrame(columns = world_table_titles)
df

column_data = table.find_all('tr')

for row in column_data:
    print(row.find_all('td'))
   
for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    
# Note Position of List Had to Change 
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    
    length = len(df)
    df.loc[length] = individual_row_data
    
 # Dataframe to Csv example :
df.to_csv(r'C:\Users\Tashenkanaye\Downloads\Companies.csv', index = False)
    







