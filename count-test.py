#!/usr/bin/python3
# Testing word counting from Bisbee Daily Review
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2019-10-15
import pandas
# import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# Much of this comes from the Programming Historian python lessons
# See https://programminghistorian.org/en/lessons/counting-frequencies

# Open the text file (do not had "b" to read options; breaks tokenizer)
textfile = open('data/bisbee-daily-review/1916-04-05-page-04.txt', 'r')
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
worddf = pandas.DataFrame({'words' : filtered_words})

# Count words for frequency table
wordcount = worddf['words'].value_counts()
# TODO: Seems a bit convoluted to get this back into a dataframe...
# wordcount appears to be a Series, and may be able to get it into a data frame
# via wordcount.to_frame()
# https://pandas.pydata.org/pandas-docs/version/0.24.2/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame
wordcount = pandas.DataFrame({"words": wordcount.index, "count": wordcount.values})

# Is sort necessary? Series.value_counts() should return values in descending
# order...
# Sort data frame, descending
wordcount.sort_values(by = 'count', ascending = False, inplace = True)
print(wordcount.head(n = 10))

# Plot top 20 words
top_20 = wordcount.head(20)
top_plot = top_20.plot.barh(x = 'words', y = 'count', rot = 0)

# Reverse the order of y axis, so high count shows at top
top_plot.invert_yaxis()
figure = top_plot.get_figure()
figure.savefig("wordplot.pdf")