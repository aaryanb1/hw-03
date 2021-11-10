# hw-03
HW #3 for CSCI040

# 1. What my ebay-dl.py file does:
My python file ```ebay-dl.py``` utilizes the ```argparse```, ```bs4```, and ```requests``` libraries to scrape 10 pages of data for a certain search term (e.g. laptop). Then, it will insert each of the product's (e.g. differing laptops) name, price, status, shipping, free returns, items sold into a dictionary within a json file.

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```


# 2. How to run my ebay-dl.py file:
1. Open ```ebay-dl.py``` in VSCode
2. Run the following line in terminal 
<code>$ python3 ebay-dl.py 'laptop'<code>


# 3. A link to the course project to see the instructions: 
https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03
