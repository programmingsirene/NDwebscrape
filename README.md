# NDwebscrape
<b>Description:</b>Collects data from Steam Search for 'Nancy Drew', creates csv file and imports collected data in format of four columns: TITLE, DISCOUNT, OLD PRICE, NEW PRICE.<br>
<b>Language:</b> Python<br>
<b>Modules:</b> BeautifulSoup, Pandas, csv, urllib.request<br>
<b>Notes:</b> Required web scraping of data which was heavily nested. This led to parsing data by first stripping the html and creating three lists for titles, discount, and prices. The prices were written in the HTML together and did not have separate identifiers. This required then string splitting the prices and saving the old and new into separate lists. All 4 lists were concatenated and imported to a newly created csv file via pandas.
