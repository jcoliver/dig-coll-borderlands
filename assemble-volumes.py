#!/usr/bin/python
# Combine pages into single volumes
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2020-03-27

import pandas as pd
import os
import re

# Rationale: files downloaded from Chronicling America are individual pages
# Would like to ultimately analyze these on a volume-by-volume basis, rather
# than a page-by-page basis
# Want to concatenate all pages from the same date into a single file
# Page files are named as YYYYMMDD-<page>.txt
# Volume files will be named YYYYMMDD.txt

titles = pd.read_csv("data/complete/complete-titles.csv")

# Conditional used for debugging; False will skip actual volume assembly
assemble = True

# iterate over each title in the data frame
for index, row in titles.iterrows():
    title = row['name']
    directory = row['directory']
    # Path to folder with individual page files
    page_locations = "data/complete/" + directory + "/pages"
    # Path to folder that will hold volume files
    volume_locations = "data/complete/" + directory + "/volumes"
    if (not(os.path.isdir(volume_locations))):
        os.makedirs(volume_locations)

    filenames = os.listdir(page_locations)
    # Need to restrict to files matching YYYYMMDD pattern (there are log.txt
    # files in the pages directories)
    date_pattern = re.compile("[0-9]{8}-.*")
    filenames = list(filter(date_pattern.match, filenames))

    # Identify unique dates and concatenate page files for each unique date

    # Create a list with all the YYYYMMDD dates, from the filenames list
    # First remove the file extension
    # ['19430706-1', '19430706-2', ...]
    dates_list = [d.replace(".txt", "") for d in filenames]
    # Next create the list of lists, each element is a two-element list:
    # [0:YYYYMMDD, 1:page number]
    # e.g. [ ['19430706', '1'], ['19430706', '2'], ... ]
    dates_list = [d.split("-") for d in dates_list]

    # Use the list of lists to build a dictionary, with YYYYMMDD as the key
    # and each value is a list of page numbers; dates_dict will eventually
    # look like:
    # {'19430706': ['1', '2'], '19430723': ['1', '2', '3'], ...}
    dates_dict = {}
    for page in dates_list:
        date = page[0]
        if (len(page) < 2):
            print("No pages for " + date + " in " + title)
            stop()
        if date in dates_dict.keys():
            dates_dict[date].append(page[1])
        else:
            dates_dict[date] = [page[1]]
    # end iterating over all pages files

    # Status report
    print("= = = = = = = = = = = = = = = = = = = =")
    print("Found data for " + title)
    print("Page files are in " + page_locations)
    print(str(len(filenames)) + " total pages")
    print("Volumes will be written to " + volume_locations)
    print(str(len(dates_dict)) + " total volumes")

    if assemble:
        # Iterate (again?!?) over each element of the dictionary, creating a
        # volume that is a concatenation of each YYYYMMDD and page number for
        # each unique date
        for date, pages in dates_dict.items():
            # Concatenate all pages for a particular date, separated by a
            # single whitespace character
            volume = " "

            # Ideally concatenation does so in appropriate page order, so we
            # need to convert elements in the pages list (which are strings at
            # this point) to integers to ensure appropriate sorting
            pages = [int(p) for p in pages]
            pages.sort()

            # list of strings; each element is text for a single page in a volume
            page_list = []

            # Iterate over all pages and append each page as a string to page_list
            for page in pages:
                page_location = page_locations + "/" + date + "-" + str(page) + ".txt"
                page_file = open(page_location, "r")
                page_text = page_file.read()
                page_file.close()
                page_list.append(page_text)
            # end iteration over all pages for single date

            # concatenate all pages of text into single string
            volume = volume.join(page_list)

            # write the string to a file
            volume_location = volume_locations + "/" + str(date) + ".txt"
            volume_file = open(volume_location, "w")
            volume_file.write(volume)
            volume_file.close()
        # end iteration over dates dictionary

# End iterating over each title