#!/usr/bin/python
# Testing word counting from Bisbee Daily Review
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2019-10-15

textfile = open("data/bisbee-daily-review/1916-04-05-page-04.txt", "rb")
wordlist = textfile.read().split()
textfile.close()
# print(wordlist)

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
