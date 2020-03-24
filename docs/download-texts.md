# Downloading content from Chronicling America

See development script called download-dev.py

## 2020-03-24
In conversations with LoC folks, there is an API for all records for a particular title:

https://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn95060694&dateFilterType=yearRange&date1=1789&date2=1963&language=&ortext=&andtext=&phrasetext=&proxtext=&proxdistance=5&rows=10&searchType=advanced&sort=date&format=json

https://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn95060694&dateFilterType=yearRange&date1=1789&date2=1963&proxdistance=5&rows=10&searchType=advanced&sort=date&format=json

Taking this apart:
base url: https://chroniclingamerica.loc.gov/search/pages/results/
lccn: sn95060694
dateFilterType=yearRange
date1=1789
date2=1963
proxdistance=5
rows=10
searchType=advanced
sort=date
format=json

This returns a json object with 10 records (rows=10). Each record contains the actual ocr in an element named ocr_spa (for spanish language texts) and ocr_eng (for english language texts). We could download things this way, grabbing the ocr_[spa|eng] element from the json object. There are 11116 records for this title, so would need to pagenate through records with the `page` key. i.e. the URL above returns the first 10 records in the json object (`rows=10`); to get rows 11-20, add `&page=2`.

Using
```
query = "https://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn95060694&dateFilterType=yearRange&date1=1789&date2=1963&proxdistance=5&rows=10&searchType=advanced&sort=date&format=json"
response = urllib.urlopen(query)
data = json.loads(response.read())
```
The returned `data` is a dictionary with the following top elements:

+ totalItems
+ endIndex
+ startIndex
+ itemsPerPage
+ items

The good stuff is in the items element. We can extract the OCR text of the _second_ item in the list via:
```
print data['items'][2]['ocr_spa']
```


