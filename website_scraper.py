import pandas as pd
import requests
import os

#Input parameters
location = "london" #If there is a space the secsond locaiton in the url, the space is replaced with the %20
beds_min = "1"
beds_max = "2"
price_min = "1000"
price_max = "2000"
radius = "1"

#URL metadata
url_zoopla="https://www.zoopla.co.uk/to-rent/property/london/?beds_max=2&beds_min=1&price_frequency=per_month&price_max=2000&price_min=1000&q=london&radius=1&results_sort=newest_listings&search_source=to-rent"
zoopla_ordering=[1,3,2,5,4,7,6]
url_rightmove="https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=REGION%5E70371&insId=1&radius=1.0&minPrice=1000&maxPrice=2000&minBedrooms=2&maxBedrooms=3&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare="
rightmove_ordering=[5,6,3,4,2,1]
url_onthemarket="https://www.onthemarket.com/to-rent/property/bounds-green/?max-bedrooms=5&max-price=2750&min-bedrooms=1&min-price=400&radius=1.0&view=grid"
onthemarket=[1,4,2,5,3,6]

def CreateURL(url_base, url_ordering, location, beds_min, beds_max, price_min, price_max, radius, RM_loc_code):
    '''Passes in the url base and the input parameters, builds the url and returns it.
    '''
    loc_d_sep = location.replace(" ", "-")
    loc_20_sep = location.replace(" ", "%20")
    search_parameters = {1:loc_d_sep, 2:beds_min, 3:beds_max, 4:price_min, 5:price_max, 6:radius, 7:loc_20_sep, 8:RM_loc_code}
    url_parameters_ordered = []
    for i in url_ordering:
        url_parameters_ordered.append(search_parameters[i])
    print(url_parameters_ordered)
    return url


if __name__ == '__main__':
    url = CreateURL(url1, location, beds_min, beds_max, price_min, price_max, radius) #Need a function to cycle through search parameters
    web_html = requests.get(url).text
    with open("web_html.txt", "w") as sf:
        f.write(web_html)
    print("done")

