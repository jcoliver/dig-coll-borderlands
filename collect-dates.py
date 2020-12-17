#!/usr/bin/python3
# Extract information about downloaded text files
# Jeff Oliver
# jcoliver@arizona.edu
# 2020-04-02

import pandas as pd
import os

titles_file = "data/complete/complete-titles.csv"

if os.path.isfile(titles_file):
    titles = pd.read_csv(titles_file)

    # iterate over each title in the data frame to extract the earliest and latest
    # date that we have text for. Dates can be found in volume file names, which
    # have the form YYYYMMDD.txt
    for index, row in titles.iterrows():
        title = row['name']
        directory = row['directory']
        volume_locations = "data/complete/" + directory + "/volumes"
        if os.path.isdir(volume_locations):
            volume_names = os.listdir(volume_locations)
            dates = [d.replace(".txt", "") for d in volume_names]
            # for integer math, convert them to integers
            dates = [int(d) for d in dates]
            # will be printing slices, so convert to string
            start = str(min(dates))
            end = str(max(dates))
            # format for nice ISO printing
            start = start[0:4] + "-" + start[4:6] + "-" + start[6:]
            end = end[0:4] + "-" + end[4:6] + "-" + end[6:]
            print("Title: " + title)
            print("\t" + start + " through " + end)
        else:
            print("No volumes available for " + title)
else:
    print(titles_file + " file not found; perhaps the complete data set unavailable.")