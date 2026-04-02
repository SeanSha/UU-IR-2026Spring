import glob
import json
import sys
from collections import defaultdict
from nltk.tokenize import word_tokenize
from pathlib import Path

class InvertedIndex:
    
    def __init__(self, file_list):
        # TODO: Initialize data structures for the inverted index
        self.file_list = file_list
        self.index = defaultdict(set)
        self.path_to_id = {}

    def get_inverted_indexes(self):
        # TODO: For each file:
        #   - Assign a unique ID
        for file in self.file_list:
            file_name = Path(file).name
            file_name_to_id = file_name.split('.')[0]

            doc_id = len(self.path_to_id)
            self.path_to_id[file_name] = file_name_to_id
            
            #   - Read file contents        
            raw_text = Path(file).read_text(encoding='utf-8')
            #   - Tokenize the text
            tokens =self.get_tokens(raw_text)
            #   - Add each token (lowercased) to the index with the file ID
            for token in tokens:
                self.index[token.lower()].add(file_name_to_id)


    def get_sorted_ids(self):
        # TODO: Convert sets of document IDs to sorted lists
        # TODO: Return the inverted index as a dictionary
        result = {}
        for token, doc_ids in self.index.items():
            result[token] = sorted(doc_ids, key=lambda x: int(x))

        return result

    @staticmethod
    def get_data(path):
        # TODO: Open and read the contents of the file at 'path'
        pass

    @staticmethod
    def get_tokens(text):
        # TODO: Tokenize the text using nltk.word_tokenize
        tokens = word_tokenize(text)
        return tokens

def main():
    # TODO: Get path from command-line arguments
    file_path = sys.argv[1]
    
    # TODO: Get all files in the directory
    file_list = glob.glob(file_path + '/*.txt')
    
    # TODO: Create an InvertedIndex instance
    inverted_index = InvertedIndex(file_list)

    # TODO: Build the inverted index
    inverted_index.get_inverted_indexes()

    # TODO: Write the result to a JSON file (plain dict of lists, not sets)
    index_for_json = inverted_index.get_sorted_ids()
    SCRIPT_DIR = Path(__file__).resolve().parent

    JSON_OUTPUT_DIR = SCRIPT_DIR.parent / 'index'
    JSON_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT_PATH = JSON_OUTPUT_DIR / 'inverted_index.json'
    with open(JSON_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_for_json, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()

