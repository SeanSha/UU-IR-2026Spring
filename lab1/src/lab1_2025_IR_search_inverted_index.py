import json
import sys

def load_index(json_path):
    # TODO: Open the file at 'json_path' and load the JSON data
    index_dict = json.load(open(json_path, 'r', encoding='utf-8'))
    return index_dict

def search_term(index, term):
    # TODO: Convert the search term to lowercase
    # TODO: Return the list of document IDs if the term is in the index
    # TODO: Otherwise return an empty list
    doc_ids = index.get(term.lower(), [])
    return doc_ids

def main():
    # TODO: Check that a file path was given as a command-line argument
    # TODO: Load the inverted index using the given path
    if len(sys.argv) < 2:
        print("Usage: python lab1_2025_IR_search_inverted_index.py <json_path>. Please provide the path to the inverted index JSON file.")
        sys.exit()

    index_dict = load_index(sys.argv[1])

    while True:
        # TODO: Prompt the user for a search term
        term = input('Enter a search term (or type "exit" to quit):')

        # TODO: Break the loop if the user types 'exit'
        if term.lower() == 'exit':
            break
        # TODO: Search for the term in the index
        doc_ids = search_term(index_dict, term)
        
        # TODO: Print which documents (if any) contain the term
        if doc_ids:
            print(f"Term found in document(s): {doc_ids}")
        else:
            print("Term not found")
            
if __name__ == '__main__':
    main()

