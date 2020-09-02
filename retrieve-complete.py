#!/usr/bin/python3
# Download complete data set from UArizona Data Repository and extract
# Jeff Oliver
# jcoliver@arizona.edu
# 2020-07-29

# import the libraries necessary for download & extraction
import requests
import zipfile
import os
import pandas

# Download the data from arizona.figshare.com
# Location of the file on the UA Data Repository
url = "https://arizona.figshare.com/ndownloader/files/24201092"

# Download the file & write it to disk
zip_filename = "fulldata.zip"
download = requests.get(url, allow_redirects = True)
with open(zip_filename, "wb") as z:
    z.write(download.content)

# Set the destination for the data files
destination = "data/complete/"

# Make sure data folder exists. If not, create it.
if(not(os.path.isdir("data"))):
    os.makedirs("data")

# Make sure the destination directory exists. If not, create it.
if(not(os.path.isdir(destination))):
    os.makedirs(destination)

# Extract files to destination directory
with zipfile.ZipFile(zip_filename, "r") as zipdata:
    zipdata.extractall(destination)

# No need for that zipfile, so we can remove it
os.remove(zip_filename)
