#!/usr/bin/python
# Testing word counting from Bisbee Daily Review
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2019-10-15
import pandas

# Much of this comes from the Programming Historian python lessons
# See https://programminghistorian.org/en/lessons/counting-frequencies

# Open the text file and read it into wordlist, splitting into a list
textfile = open("data/bisbee-daily-review/1916-04-05-page-04.txt", "rb")
wordlist = textfile.read().split()
textfile.close()
# print(wordlist)

# TODO: removal of stopwords will happen here

# TODO: need to remove commas and potentially other puncutation

# Make dataframe with words, will use to group by word and count
worddf = pandas.DataFrame({"words" : wordlist})
print(worddf.head())
# Count frequencies of each word (first approach)
# wordfreq = []
# for w in wordlist:
#     wordcount = wordlist.count(w)
#     wordfreq.append(wordcount)

# Put into a dictionary
# worddict = dict(zip(wordlist, wordcount))