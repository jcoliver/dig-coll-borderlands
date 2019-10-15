#!/usr/bin/python
# Testing word counting from Bisbee Daily Review
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2019-10-15
import pandas
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# Much of this comes from the Programming Historian python lessons
# See https://programminghistorian.org/en/lessons/counting-frequencies

# Open the text file
textfile = open("data/bisbee-daily-review/1916-04-05-page-04.txt", "rb")
# Read text file into single string
wordstring = textfile.read()
# Close the input file
textfile.close()

# Make all letters lower case
wordstring = wordstring.lower()

# Remove puncutation AND convert to list
tokenizer = RegexpTokenizer(r'\w+')
wordlist = tokenizer.tokenize(wordstring)

# Removal of stopwords
stop_words = set(stopwords.words('english'))
filtered_words = []
for w in wordlist:
    if w not in stop_words:
        # Still some odd, single-length words; drop those too
        if len(w) > 1:
            filtered_words.append(w)

# Make dataframe with words
worddf = pandas.DataFrame({"words" : filtered_words})

# Count words for frequency table
wordcount = worddf['words'].value_counts()
print(wordcount.head(n = 10))
