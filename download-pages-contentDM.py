#!/usr/bin/python
# Download individual pages from contentDM
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2020-11-03

# Need to download individual pages from contentDM
# Use a separate script for volume assembly (like was done for Chronicling
# America texts)

import urllib
import json
import pandas as pd
import time
import os

# URL for use with contentDM's API
base_url = "https://content.library.arizona.edu/digital/bl/dmwebservices/index.php"
# Maximu records to return with a single request
num_records = 100

# Start with a query to get all items. Use dmQuery with maxrecs = 1, so we can
# get a count of the records. We will need to do multiple queries as we can
# only get a maximum of 1024 records at a time, and there are > 3000.
# This query tells us how many records there are:
# https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmQuery/p16127coll3/0/identi!title/identi/1/1/1//0/0/0/1/json
# Look at total element inside pager
# pager
#   start	"1"
#   maxrecs	"1"
#   total	3679
# records
#   0
#     collection	"/p16127coll3"
#     pointer	6237
#     filetype	"cpd"
#     parentobject	-1
#     identi	"sn95060694"
#     title	"El Tucsonense, 1952-08-08"
#     find	"6238.cpd"

item_count_query = base_url + "?q=dmQuery/p16127coll3/0/identi!title/identi/1/1/1//0/0/0/1/json"
item_count_response = urllib.urlopen(item_count_query)
dmQuery_dict = json.loads(item_count_response.read())
total_items = dmQuery_dict["pager"]["total"]
print("Found " + str(total_items) + " items")

# TODO: delete these three lines when done testing
total_items = 2
num_records = 2
print("But only testing with " + str(total_items) + " items")

# Now we will iterate over all 3679 records, and look at the pointer field
# within an individual record
if (total_items > 0):
    # The item on which to start, because the url isn't indexed by page
    start = 1

    while (start + num_records - 1) <= total_items:
        if (start > 1):
            time.sleep(0.5) # be nice to contentDM server

        print("Looking at items " + str(start) + " through " + str(start + num_records - 1))

        # Query to get the records for that page
        records_query = base_url + "?q=dmQuery/p16127coll3/0/identi!title/identi/" + str(num_records) + "/" + str(start) + "/1//0/0/0/1/json"
        records_response = urllib.urlopen(records_query)
        records_dict = json.loads(records_response.read())

        # records are returned as a list, not a dictionary?
        records_list = records_dict["records"]
        for record in records_list:
            pointer = record["pointer"]
            print("\nPointer value: " + str(pointer))

            # Start by checking to see if we already have data for this title &
            # date. title element has what we need, but we need some text
            # manipulation
            # Title: El Tucsonsense -> el-tucsonense
            # Date: 1952-08-08 -> 19520808

            title = record["title"]
            title_list = title.split(",")
            title_str = title_list[0].strip().lower().replace(" ", "-")
            date_str = title_list[1].strip().replace("-", "")
            print("Title field: " + title)
            print("Title string: " + title_str)
            print("Date string: " + date_str)

            filename = date_str + ".txt"
            filepath = "data/complete/" + title_str + "/volumes/" + filename


            if (not(os.path.isfile(filepath))):
                print("File " + filename + " does not exist")
                # Here is where download of individual pages will need to happen
            else:
                print("File " + filename + " exists")


            # End iterating over each record

        # End iterating over page results
        start = start * num_records + 1
        # page = page + 1
    # End of while loop over multiple pages
