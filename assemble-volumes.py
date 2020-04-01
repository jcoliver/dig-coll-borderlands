#!/usr/bin/python
# Combine pages into single volumes
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2020-03-27

import pandas as pd
import os
# from glob import glob

# Rationale: files downloaded from Chronicling America are individual pages
# Would like to ultimately analyze these on a volume-by-volume basis, rather
# than a page-by-page basis
# Want to concatenate all pages from the same date into a single file
# Page files are named as YYYYMMDD-<page>.txt

titles = pd.read_csv("data/titles.csv")
# Do this for each of the titles of interest
for index, row in titles.iterrows():
    title = row['name']
    directory = row['directory']
    # for now, only looking at the one title for which we have data
    if (title == "Apache Sentinel"):
        # Path to folder with individual page files
        page_locations = "data/" + directory + "/pages"
        # Path to folder that will hold volume files
        volume_locations = "data/" + directory + "/volumes"
        if (not(os.path.isdir(volume_locations))):
            os.makedirs(volume_locations)

        filenames = os.listdir(page_locations)
        # Want to identify unique dates and concatenate files for each unique
        # date

        # Create a list with all the YYYYMMDD dates, from the filenames list
        # First remove the file extension
        dates_list = [d.replace(".txt", "") for d in filenames]
        # Next create the list of lists, each element is a YYYYMMDD and a page
        # number
        dates_list = [d.split("-") for d in dates_list]

        # Take the list of lists and convert to a dictionary, which uses
        # YYYYMMDD as the key and each element is a list of page numbers
        # dates_dict will eventually look like:
        # {'19430706': ['1', '2'], '19430723': ['1', '2', '3'], ...}
        dates_dict = {}
        for page in dates_list:
            date = page[0]
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

            page_list = []
            for page in pages:
                page_location = page_locations + "/" + date + "-" + str(page) + ".txt"
                page_file = open(page_location, "r")
                page_text = page_file.read()
                page_file.close()
                page_list.append(page_text)

            volume = volume.join(page_list)

            # Write the string to a file
            volume_location = volume_locations + "/" + str(date) + ".txt"

            # volume_file = open(volume_location, "w")
            # volume_file.write(volume)
            # volume_file.close()
        # end iteration over dates dictionary

# End iterating over each title