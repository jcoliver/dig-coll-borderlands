#!/usr/bin/python
# Combine pages into single volumes
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2020-03-27

import pandas as pd
import os
from glob import glob

# Rationale: files downloaded from Chronicling America are individual pages
# Would like to ultimately analyze these on an issue-by-issue basis
# Want to concatenate all pages from the same date into a single file
# Page files are named as YYYYMMDD-<page>.txt
# After

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

        # Maybe want a dictionary, where key is date and each element is a list
        # of page numbers. Iterate over keys, pulling out the list of pages to
        # build file names for reading and concatenating
        # Yes. See scratch.py and work from there

        # First road of development. Abandoned in favor of dictionary approach
        # Create list of two-element lists, where first element is date
        dates = [d.split("-") for d in filenames]
        # Extract first element of each sub-list
        dates = [d[0] for d in dates]
        # Convert to a set to retain only unique values
        dates = set(dates)
        print("Number of files: " + str(len(filenames)))
        print("Number of dates: " + str(len(dates)))
        first = True
        # Iterate over each unique date
        for date in dates:
            # The file to write to
            datefile = date + ".txt"
            # Identify all files that are pages from date
            pagefiles = glob(page_locations + "/" + date + "-*")
            if first:
                print(pagefiles)
                first = False
