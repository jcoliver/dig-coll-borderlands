#!/usr/bin/python3
# Download individual pages from contentDM
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2020-11-03

# Need to download individual pages from contentDM
# Use a separate script for volume assembly (like was done for Chronicling
# America texts)

# Variation among scripts in urllib vs. urllib3 (and shebang, for that matter)
import urllib.request
import xmltodict
import json
import pandas as pd
import time
import os

# URL for use with contentDM's API
base_url = "https://content.library.arizona.edu/digital/bl/dmwebservices/index.php"
# Maximum records to return with a single request
num_records = 100

# Whether or not to print message for each volume
verbose = False

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

item_count_response = urllib.request.urlopen(item_count_query)
dmQuery_dict = json.loads(item_count_response.read())
total_items = dmQuery_dict["pager"]["total"]
print("Found " + str(total_items) + " items")

# TODO: delete these three lines when done testing
total_items = 10
num_records = 10
print("But only testing with " + str(total_items) + " items")

# Now we will iterate over all 3679 records, and look at the pointer field
# within an individual record
volumes_downloaded = 0
pages_downloaded = 0
volumes_skipped = 0
dot_frequency = 10

if (total_items > 0):
    # The item on which to start, because the url isn't indexed by page
    start = 1

    while (start + num_records - 1) <= total_items:
        if (start > 1):
            time.sleep(0.5) # be nice to contentDM server

        print("\nLooking at items " + str(start) + " through " + str(start + num_records - 1), end = "")

        # Query to get the records for that page
        records_query = base_url + "?q=dmQuery/p16127coll3/0/identi!title/identi/" + str(num_records) + "/" + str(start) + "/1//0/0/0/1/json"
        records_response = urllib.request.urlopen(records_query)
        records_dict = json.loads(records_response.read())

        # records are returned as a list, not a dictionary?
        records_list = records_dict["records"]
        for record in records_list:
            pointer = record["pointer"]

            if (volumes_downloaded + volumes_skipped) % dot_frequency == 0:
                print(".", end = "")

            # Start by checking to see if we already have data for this title &
            # date. The title element has what we need, but we need some text
            # manipulation. The value in title is returned as
            # "El Tucsonense, 1952-08-08"
            # Title: El Tucsonsense -> el-tucsonense
            # Date: 1952-08-08 -> 19520808

            title = record["title"]
            title_list = title.split(",")
            title_str = title_list[0].strip().lower().replace(" ", "-")
            date_str = title_list[1].strip().replace("-", "")

            filename = date_str + ".txt"
            filepath = "data/complete/" + title_str + "/volumes/" + filename
            pagespath = "data/complete/" + title_str + "/pages/"

            if (not(os.path.isfile(filepath))):
                if verbose:
                    print("Volume " + filename + " does not exist, downloading.")
                # Here is where download of individual pages will need to happen

                # Use value in pointer with the getfile utility
                # The getfile utility provides a list of all pages:
                # https://content.library.arizona.edu/utils/getfile/collection/p16127coll3/id/6237/filename/testpage.xml

                # Query to get pointers for individual pages for a single day's
                # paper
                one_day_query = "https://content.library.arizona.edu/utils/getfile/collection/p16127coll3/id/" + str(pointer) + "/filename/testpage.xml"
                file = urllib.request.urlopen(one_day_query)
                data = file.read()
                file.close()
                data_dict = xmltodict.parse(data)
                # Iterate over each "page" element in returned object
                for page in data_dict["cpd"]["page"]:
                    # Want the values in the pageptr element so we can grab
                    # the file.
                    page_ptr = page["pageptr"]
                    # Retrieve the page in json
                    one_page_query = "https://content.library.arizona.edu/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16127coll3/" + page_ptr + "/json"
                    # The fullte element has the OCR text
                    page_response = urllib.request.urlopen(one_page_query)
                    page_dict = json.loads(page_response.read())
                    ocr_text = page_dict["fullte"]

                    # Will also want to extract page number, as that will be
                    # part of the filename <date>-<page number>.txt. In the
                    # Chronicling America script, the same file naming
                    # convention is used, although it is described as
                    # <date>-<sequence>.txt because "sequence" is the name of
                    # the element with page number info
                    page_title = page["pagetitle"]
                    # Cross fingers that page number is always last token in
                    # the split string
                    page_number = page_title.split(" ")[-1].strip()
                    page_filename = date_str + "-" + page_number + ".txt"
                    page_filepath = pagespath + page_filename
                    # Write the text to the file and move on
                    text_file = open(page_filepath, "w")
                    text_file.write(ocr_text)
                    text_file.close()
                    pages_downloaded = pages_downloaded + 1
                # End iterating over all pages in a volume
                volumes_downloaded = volumes_downloaded + 1
            else:
                if verbose:
                    print("Volume " + filename + " exists; skipping.")
                volumes_skipped = volumes_skipped + 1
            # End iterating over each record (a single day's paper)

        # End iterating over page results
        start = start * num_records + 1
        # page = page + 1
    # End of while loop over multiple pages
# End conditional for more than 0 items
print("\n*  *  *  *  *")
print("Process complete")
print("Total new volumes: " + str(volumes_downloaded))
print("Total pages downloaded: " + str(pages_downloaded))
print("Total volumes skipped: " + str(volumes_skipped))