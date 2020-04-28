# Methods & classes for digital collections lessons
# Jeff Oliver
# jcoliver@arizona.edu
# 2020-04-27

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

class CleanText:
    def __init__(self, filename, language = "english", min_length = 2):
        self.filename = filename
        self.language = language
        self.min_length = min_length

        # Read data into a single string
        self.issue_text = self.readfile()

        # Do prep work, tokenizing and converting to lower case
        self.word_list = self.lower_tokenize()

        # Drop stop words and words shorter than min_length
        self.clean_list = self.clean_words()

    def readfile(self):
        """
        Reads text from file
        Returns single string object
        """
        file = open(self.filename, "r")
        issue_text = file.read()
        file.close()
        return(issue_text)

    def lower_tokenize(self):
        """
        Converts all letters to lower case and tokenizes
        Returns a list of strings
        """
        # set to all lower case and tokenize

        # convert everything to lower case (otherwise "House" and "house" are
        # considered different words)
        issue_text = self.issue_text.lower()

        # remove punctuation and "tokenize"
        tokenizer = RegexpTokenizer(r'\w+')
        word_list = tokenizer.tokenize(issue_text)
        return(word_list)

    def clean_words(self):
        """
        Removes stopwords and too-small values
        Returns a list of strings
        """
        stop_words = set(stopwords.words(self.language))
        filtered_words = []
        for word in self.word_list:
            if word not in stop_words:
                if len(word) >= self.min_length:
                    filtered_words.append(word)
        return(filtered_words)

# Classes needed?
# One class, cleantext that takes arguments:
# a filename
# a language (default = english) for stopwords
# minimum length of token (default = 2)

