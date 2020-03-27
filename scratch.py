#!/usr/bin/python
# Scratch
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2020-03-27

dlist = ['20-1.txt', '20-2.txt', '22-1.txt', '22-2.txt', '22-3.txt']
dlist = [d.replace(".txt", "") for d in dlist]
dlist = [d.split("-") for d in dlist]
ddict = {}
for page in dlist:
    date = page[0]
    if date in ddict.keys():
        ddict[date].append(page[1])
    else:
        ddict[date] = list(page[1])
print(ddict)