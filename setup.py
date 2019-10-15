#!/usr/bin/python
# Set up script, primarily for stopwords
# Jeff Oliver
# jcoliver@email.arizona.edu
# 2019-10-15

# Will download and install stopwords into ~/nltk_data (creating this directory
# if it does not already exist)
import nltk
nltk.download('stopwords')