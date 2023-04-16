# Professor Dr.Calderon
# Eulalia Rivera
# CIS 3330 CLASS

import requests
import urllib.parse
import json
import pandas as pd
import nltk
from nltk.corpus import stopwords 
from yelpapi import YelpAPI

# Searching for 20 restaurants
api_key = "PFNsxOwTQm9eiZ3kXvIBhIQFDwz9fR-tjqFxdc7MPCGporbAG9GXPya9uOLOITQkYz60CIZmn0N3zIevQyglFHIoubWmxfBP85h8XNmcWLtrEHYOpo2HbaB4CRg2ZHYx"
yelp_api =YelpAPI(api_key)
search_term = "Barbacoa"
location_term = "Los Angeles, CA"

search_results = yelp_api.search_query(
    term=search_term, location=location_term, 
    sort_by='rating',limit=20, offset=20 
    )
print(search_results)   # List the results in search_results['businesses']

# 
search_term = "Barbacoa"
seasch_term = urllib.parse.quote_plus(search_term)  # parameter
location = "Los Angeles, CA"
location = urllib.parse.quote_plus(location)
sort_by = "rating"
limit = 20  # Searching for 20 restaurants
url = f"https://api.yelp.com/v3/businesses/search?location={location}&term={search_term}&sort_by={sort_by}&limit={limit}"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer PFNsxOwTQm9eiZ3kXvIBhIQFDwz9fR-tjqFxdc7MPCGporbAG9GXPya9uOLOITQkYz60CIZmn0N3zIevQyglFHIoubWmxfBP85h8XNmcWLtrEHYOpo2HbaB4CRg2ZHYx"
}
response = requests.get(url, headers=headers)
response_json = json.loads(response.text)
print(response_json['businesses']) # List of results in response_json variable

#  
print(search_results)   # list of results in search_result['businesses']
result_df = pd.DataFrame.from_dict(search_results['businesses'])    # Converting list of json objects to Pandas Data Frame
print(result_df)    
result_df.to_csv("yelpapi_businesses_results.csv")

#
response = requests.get(url, headers=headers)
response_json = json.loads(response.text)
print(response_json['businesses'])  # List of results in response_json variable
result_df = pd.DataFrame.from_dict(response_json['businesses']) # Converting list of json objects to Pandas Data Frame
print(result_df)
result_df.to_csv("request_businesses_results.csv")

# 
id_for_reviews = "barbacoa-los-angeles" # use alias from data
review_response = yelp_api.reviews_query(id=id_for_reviews)
print(review_response)  # list of reviews in review_response variable 
for review in review_response['reviews']:   # Text is an element (review) text
    print(review['text'])  
 
#
id_for_reviews ="barbacoa-los-angeles"
limit = 20
sort_by ="newest"   # newest or yelp_sort
url= f"https://api.yelp.com/v3/businesses/{id_for_reviews}/reviews?limit={limit}&sort_by={sort_by}"
headers = {
    "accepr": "application/json",
    "Authorization": "Bearer PFNsxOwTQm9eiZ3kXvIBhIQFDwz9fR-tjqFxdc7MPCGporbAG9GXPya9uOLOITQkYz60CIZmn0N3zIevQyglFHIoubWmxfBP85h8XNmcWLtrEHYOpo2HbaB4CRg2ZHYx"
}
response = requests.get(url, headers=headers)
response_json = json.loads(response.text)
print(response_json)   

#
id_for_reviews = "barbacoa-los-angeles" # use alias from data
review_response = yelp_api.reviews_query(id=id_for_reviews)
print(review_response)  # List of reviews in reviews_response ['reviews']  
for review in review_response['reviews']:   # Text is an element (review) text
    print(review['text'])  
result_df = pd.DataFrame.from_dict(review_response['reviews'])  # Converting list of json objects to Pandas Data Frame 
print(result_df)   
result_df.to_csv(f"{id_for_reviews}_yelpapi_businessses_results.csv")

# 
response = requests.get(url, headers=headers)
response_json =json.loads(response.text)
print(response_json)   
result_df = pd.DataFrame.from_dict(response_json['reviews'])     # Converting list of json objects to Pandas Data Frame
print(result_df)    
result_df.to_csv(f"{id_for_reviews}_request_reviews_results.csv")

'''
stop_words = set(stopwords.words('english'))
reviews = open('request_businessess_results.csv')

for review in reviews:
    #print review
    tokens = nltk.word_tokenize(review)
    pos_tags = nltk.pos_tag(tokens)
    new_text = []
    for tag in pos_tags:
        if tag[0] not in stop_words:
            print(tag[0])
            new_text.append(tag[0])
    print("\original")
    print(review)
    print("\nNew")
    print(" ".join(new_text))
'''



