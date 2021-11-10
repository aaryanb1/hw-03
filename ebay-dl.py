import argparse
import requests
from bs4 import BeautifulSoup
import json

def parse_price(x):
    if 'to' in x:
        x = x.replace(x[0:x.index('o')+2], '')

    taggy = ''
    for char in x:
        if char in '1234567890':
            taggy += char
    if len(taggy) > 0:
         return int(taggy)
    else:
        return None

def parse_items_sold(x):
    items_soldy = ''
    for char in x:
        if char in '1234567890':
            items_soldy += char
    if len(items_soldy) > 0:
         return int(items_soldy)
    else:
        return None

def parse_shipping_cost(x):
    if 'Free' in x:
        shipping_cost = 0

    else:
        shipping_costy = ''
        for char in x:
            if char in '1234567890':
                shipping_costy += char
        if len(shipping_costy) > 0:
            return int(shipping_costy)
        else:
            return None


#get command line arguments
parser = argparse.ArgumentParser(description='Download info from EBay and convert to JSON')
parser.add_argument('search_term')
parser.add_argument('--num_pages', default=10)
args = parser.parse_args()
print('args.search_term=', args.search_term)

#list of all items found in all ebay webpages
items = []

#loop over the ebay webpages
for page_number in range(1, int(args.num_pages)+1):

    # build the url
    url = 'https://www.ebay.com/sch/i.html?_from=R406&_nkw=' + args.search_term + '&_sacat=0&LH_TitleDesc=0&_pgn=' + str(page_number) + '&rt=nc'
    print('url=', url)

    #download the html
    r = requests.get(url)
    status = r.status_code
    print('status=', status)
    html = r.text

    #process the html
    soup = BeautifulSoup(html, 'html.parser')

    #loop over the items in the page
    tags_items = soup.select('.s-item')
    for tag_item in tags_items:    

        tags_name = tag_item.select('.s-item__title')
        name = None
        for tag in tags_name:
            name = tag.text

        tags_price = tag_item.select('.s-item__price')
        price = None
        for tag in tags_price:
            price = parse_price(tag.text)

        tags_items_sold = tag_item.select('.s-item__hotness, .s-item__additionalItemHotness')
        items_sold = None
        for tag in tags_items_sold:
            items_sold = parse_items_sold(tag.text)

        tags_status = tag_item.select('.SECONDARY_INFO')
        status = None
        for tag in tags_status:
            if 'Pre-Owned' in tag.text:
                status = 'Pre-Owned'
            if 'Brand New' in tag.text:
                status = 'Brand New'
            if 'Refurbished' in tag.text:
                status = 'Refurbished'
        
        tags_shipping_cost = tag_item.select('.s-item__shipping, .s-item__dynamic')
        shipping_cost = None
        for tag in tags_shipping_cost:
            shipping_cost = parse_shipping_cost(tag.text)

        freereturns = False
        tags_freereturns = tag_item.select('.s-item__free-returns')
        for tag in tags_freereturns:
            freereturns = True

        item = {
            'name': name,
            'price': price,
            'status': status,
            'shipping cost': shipping_cost,
            'free_returns': freereturns,
            'items_sold': items_sold
        }
        items.append(item)

    print('len(tags_items)=', len(tags_items))
    print('len(items)=', len(items))

filename = args.search_term+'.json'
with open(filename, 'w', encoding='ascii') as f:
    f.write(json.dumps(items))