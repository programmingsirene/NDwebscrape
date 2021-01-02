#### WEB SCRAPE FROM STEAM SEARCH FOR NANCY DREW GAMES TO CSV ####
import urllib.request
from bs4 import BeautifulSoup
import csv
import pandas as pd

# GREETING
print("Conducting Steam Search for Nancy Drew...")

# SETUP WEB SCRAPE
# open connection, grab page
my_url = urllib.request.urlopen('https://store.steampowered.com/search/?term=nancy+drew').read()

# parse html page & make beautifulsoup object
soup = BeautifulSoup(my_url, 'html.parser')

# FIND ALL ROWS WITH DATA
rows = (soup.find_all('div', {'class': 'col search_name ellipsis'})) 

# COLLECT DATA
print("Collecting data...")
for row in rows:
	titles = soup.find_all('span', {'class': 'title'})
	discount = soup.find_all('div', {'class': 'col search_discount responsive_secondrow'})
	prices = soup.find_all('div', {'class': 'col search_price discounted responsive_secondrow'})

# DECLARATIONS
titles_list = []
discount_list = []
prices_list = []
old_prices = []
new_prices = []

# STRIP TO TEXT INTO LISTS
print("Parsing data...")
for item in titles:
	titles_list.append(str(item.text.strip())) 
for item in discount:
	discount_list.append(str(item.text.strip()))
for item in prices:
	prices_list.append(str(item.text.strip()))

#print (titles_list, discount_list, prices_list)

# BREAK UP PRICES - split strings to have old and new price separated
for item in prices_list:
#	old_prices.append(item.split("$",2))
	j, o, n = item.split("$",2)
	old_prices.append(o)
	new_prices.append(n)
	
# TRUNCATE
del titles_list[40:]
del discount_list[40:]
del old_prices[40:]
del new_prices[40:]

# LOAD INTO CSV
print("Creating csv file...")

# combine 4 lists to csv via pandas
df = pd.DataFrame({'TITLES':titles_list, 'DISCOUNT':discount_list, 'OLD PRICE':old_prices, 'NEW PRICE': new_prices}).to_csv('NDsearch.csv', index=False)

print("CSV created.")

#end
