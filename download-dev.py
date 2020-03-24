#!/usr/bin/python
# Testing download approach for Chronicling America OCR text
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2020-03-24

import urllib, json

# define url to try
query = "https://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn95060694&dateFilterType=yearRange&date1=1789&date2=1963&proxdistance=5&rows=10&searchType=advanced&sort=date&format=json"
response = urllib.urlopen(query)
data = json.loads(response.read())
print data.keys()
print data['items'][2]['ocr_spa']

# import urllib, json
# url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
# response = urllib.urlopen(url)
# data = json.loads(response.read())
# print data