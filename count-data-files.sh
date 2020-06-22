#!/bin/bash
# Count number of files in data directories
# Jeff Oliver
# jcoliver@arizona.edu
# 2020-06-22

cd data
TITLES=($(ls -d */))
TOTALFILES=0
for TITLE in "${TITLES[@]}"
do
    # Each value of TITLE has trailing slash "/"
    # echo "$TITLE"
    PAGEFILES=($(ls "$TITLE/pages" | wc -l))
    # echo "$PAGEFILES"
    VOLFILES=($(ls "$TITLE/volumes" | wc -l))
    # echo "$VOLFILES"
    TITLEFILES=$((PAGEFILES + VOLFILES))
    # echo "$TITLEFILES"
    TOTALFILES=$((TOTALFILES + TITLEFILES))
done

echo "Total number of files: $TOTALFILES"