# hw-03
HW #3 for CSCI040

# 1. What my ebay-dl.py file does:
My python file ```ebay-dl.py``` utilizes the ```argparse```, ```bs4```, and ```requests``` libraries to scrape 10 pages of data for a certain search term (e.g. laptop). Then, it will insert each of the product's (e.g. differing laptops) name, price, status, shipping, free returns, items sold into a dictionary within a json file.




# 2. How to run my ebay-dl.py file:
1. Open ```ebay-dl.py``` in VSCode
2. Run the following command in terminal in order to create a json file called iphone.json that has scraped iphone products details off of ebay
```
$ python3 ebay-dl.py 'iphone'
```
3. Keep the same command as above, but replace 'iphone' with 'toys' in the terminal. This will create a json file called toys.json
```
$ python3 ebay-dl.py 'toys'
```
4. Keep the same command as above, but replace 'toys' with 'drill press' in the terminal. This will create a json file called drill press.json
```
$ python3 ebay-dl.py 'drill press'
```

# 3. A link to the course project to see the instructions: 
https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03
