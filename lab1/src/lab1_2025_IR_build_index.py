import glob
import json
import sys
from collections import defaultdict
from nltk.tokenize import word_tokenize

class InvertedIndex:
    
    def __init__(self, file_list):
        # TODO: Initialize data structures for the inverted index
        pass

    def get_inverted_indexes(self):
        # TODO: For each file:
        #   - Assign a unique ID
        #   - Read file contents
        #   - Tokenize the text
        #   - Add each token (lowercased) to the index with the file ID
        pass

    def get_sorted_ids(self):
        # TODO: Convert sets of document IDs to sorted lists
        # TODO: Return the inverted index as a dictionary
        pass

    @staticmethod
    def get_data(path):
        # TODO: Open and read the contents of the file at 'path'
        pass

    @staticmethod
    def get_tokens(text):
        # TODO: Tokenize the text using nltk.word_tokenize
        pass

def main():
    # TODO: Get path from command-line arguments
    # TODO: Get all files in the directory
    # TODO: Create an InvertedIndex instance
    # TODO: Build the inverted index
    # TODO: Write the result to a JSON file
    pass

if __name__ == '__main__':
    main()

