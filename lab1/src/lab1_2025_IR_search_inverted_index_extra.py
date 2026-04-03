import json
import sys
import math

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

def get_total_docs(index):
    
    all_docs = set()
    for posings in index.values():
        all_docs.update(posings)
    return len(all_docs)

def count_term(index, term, total_docs):

    # TF is term frequency. It is the number of times the term appears in one of the documents.
    # IDF is inverse document frequency. It is the number of documents that contain the term.
    # DF is document frequency. It is the number of documents that contain the term.

    term = term.lower()
    postings = index.get(term, [])

    if not postings:
        return []
    
    df = len(postings)
    idf = math.log(total_docs / df) if df > 0 else 0.0
    scored = []
    for doc_id in postings:
        tf = 1
        score = tf * idf
        scored.append((doc_id, tf, score))
    scored.sort(key=lambda x: x[2], reverse=True)

    return scored



def main():
    # TODO: Check that a file path was given as a command-line argument
    # TODO: Load the inverted index using the given path
    if len(sys.argv) < 2:
        print("Usage: python lab1_2025_IR_search_inverted_index.py <json_path>. Please provide the path to the inverted index JSON file.")
        sys.exit(1)

    index_dict = load_index(sys.argv[1])
    total_docs =get_total_docs(index_dict)
    print(f"Total documents: {total_docs}")

    while True:
        # TODO: Prompt the user for a search term
        term = input('Enter a search term (or type "exit" to quit):')

        # TODO: Break the loop if the user types 'exit'
        if term.lower() == 'exit':
            break

        # TODO: Multiple search terms
        terms = term.lower().split()

        # TODO: Search for the term in the index
        
        doc_ids_list = []

        for term in terms:


            doc_ids = search_term(index_dict, term)
            doc_ids_list.append(doc_ids)

            # TODO: Print which documents (if any) contain the term
            if doc_ids:
                print(f"Term {term.lower()} found in document(s): {doc_ids}")
            else:
                print(f"Term {term.lower()} not found")

            ranked = count_term(index_dict, term, total_docs)

            if not ranked:
                print(f"Term {term.lower()} not found")
                continue
            
            print(f"Top results for '{term.lower()}' (doc_id, tf, tf-idf)")
            for doc_id, tf, score in ranked[:10]:
                print(f"{doc_id}\tTF={tf}\tTF-IDF={score:.4f}")
        

        doc_ids_set = [set(ids) for ids in doc_ids_list]

        operator = input('Enter an operator (AND/OR):')
        if operator == 'AND':
            doc_ids = set.intersection(*doc_ids_set)
        elif operator == 'OR':
            doc_ids = set.union(*doc_ids_set)
        else:
            print("Invalid operator")
            continue

        print(f"Documents containing all terms: {doc_ids}")



            
if __name__ == '__main__':
    main()

