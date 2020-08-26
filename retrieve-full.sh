#!/bin/bash
# Download and extract newspaper page data from University of Arizona Research
# Data Repository

ZIPFILE="fulldata.zip"
SOURCE="https://arizona.figshare.com/ndownloader/files/24201092"

# Download archive
wget -nv -O $ZIPFILE "$SOURCE"

# Extract data and place in a directory called "complete"
DEST="data/complete"

if [ -d "$DEST" ]
then
    echo "Extracting to $DEST."
else
    echo "Creating $DEST; extracting files to that location."
    mkdir $DEST
fi

# Quiet unzip, overwriting files if they exist without warning
unzip -qq -uo $ZIPFILE -d $DEST
echo "Extraction complete."
rm $ZIPFILE
