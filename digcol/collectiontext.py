"""
Collection module for dealing with multiple newspaper volumes
"""

import pandas

class CollectionText:
    def __init__(self, filenames, filepath, language = "english", min_length = 2):
        self.filenames = filenames
        self.filepath = filepath
        self.language = language
        self.min_length = min_length

    # Function to read each file in, clean it up via CleanText, and store it
    # all as a list|dictionary

    # Function to calculate relative word frequency for each file
