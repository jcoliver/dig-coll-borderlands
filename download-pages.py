#!/usr/bin/python
# Testing download approach for Chronicling America OCR text
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2020-03-24

import urllib
import json
import pandas as pd
import time
import os

# The url for a query to Library of Congress; excludes two key-value pairs:
#      the library of congress call number lccn=XXXX
#      the number of results to return per page rows=XX
base_url = "https://chroniclingamerica.loc.gov/search/pages/results/?dateFilterType=yearRange&date1=1789&date2=1963&proxdistance=5&searchType=advanced&sort=date&format=json"

# number of records to return when downloading text; will use this with the
# page key in the query URL
num_records = 100

# iterate over titles for downloads
titles = pd.read_csv("data/titles.csv")
for index, row in titles.iterrows():
    title = row['name']
    lccn = row['lccn']
    directory = row['directory']
    # Page files are going to end up in a folder called "pages" within each
    # title's directory. Check to see if data/<directory>/pages exists; if not,
    # create it
    destination_dir = "data/" + directory + "/pages"
    if (not(os.path.isdir(destination_dir))):
        os.makedirs(destination_dir)
    download_log = destination_dir + "/log.txt"

    language = row['language']
    # The name of the element in the returned JSON obejct where OCR text is
    # stored is based on the language; ocr_eng for English, ocr_spa for Spanish
    ocr_lang = "ocr_" + language[0:3].lower()

    print("Querying " + title + "...")

    # Will want to do two queries. One to find out how many total items are
    # available, and a second (set) to download all the items

    # For first query, only need one result
    query_url = base_url + "&lccn=" + lccn + "&rows=1"
    response = urllib.urlopen(query_url)
    data = json.loads(response.read())
    total_items = data['totalItems']
    print("\t...found " + str(total_items) + " items.")

    # To actually download text files, will need to send multiple queries, up
    # to the point where we reach total_items
    if (total_items > 0):
    # if (title == "Arizona Post"):
        page = 1
        while ((page - 1) * num_records) <= total_items:
            if (page > 1):
                time.sleep(0.5) # be nice to LoC

            # Some bookeeping for status outputs
            end_item = page * num_records
            start_item = end_item - num_records + 1
            if end_item > total_items:
                end_item = total_items
            print("\tDownloading items " + str(start_item) + " through " + str(end_item))

            # Build the URL for the page of records
            download_url = base_url + "&lccn=" + lccn
            download_url = download_url + "&rows=" + str(num_records)
            download_url = download_url + "&page=" + str(page)

            # Retrieve a page's worth of records
            download_response = urllib.urlopen(download_url)
            download_data = json.loads(download_response.read())

            # Iterate over each item in items element and save the OCR text in a
            # file using the data/<directory>/<date>-<sequence>.txt file naming
            # convention
            for item in download_data['items']:
                date = item['date']
                sequence = item['sequence']
                # Some pages do not have corresponding text available; check to
                # see if OCR text exists first before trying to access
                if ocr_lang in item.keys():
                    ocr_text = item[ocr_lang].encode("utf-8")
                    filename = destination_dir + "/" + str(date)
                    filename = filename + "-" + str(sequence) + ".txt"
                    text_file = open(filename, "w")
                    text_file.write(ocr_text)
                    text_file.close()
                else:
                    log_message = "Missing lanuage key '" + ocr_lang + "' in " + str(date) + ", page " + str(sequence)
                    print("\t" + log_message)
                    log_file = open(download_log, "a+")
                    log_file.write(log_message + "\n")
                    log_file.close()
            # End iterating over page results
            page = page + 1
        # End while loop iterating over pagenation
    # end conditional for non-zero results
# end iteration over titles