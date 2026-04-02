import os
import nltk
from nltk.corpus import reuters
# nltk.download('reuters')  # TODO: Uncomment if needed

from pathlib import Path

def main():
    os.makedirs('../reuters', exist_ok=True)  # This creates a directory unless you already have one.
    os.makedirs('../reuters_small', exist_ok=True)  # This creates a directory unless you already have one.
    
    # Make sure the path is correct (i.e., is in accordance with the structure of directories and files under Section 8 
    #in the lab instructions
    out_path = Path('../reuters')
    small_set_path = Path('../reuters_small')

    # TODO: Get the list of Reuters file IDs
    # TODO: For each file ID:
    #   - Get the raw text
    #   - Create a filename based on the file ID
    #   - Write the text to a .txt file in './reuters'
    #   - Optionally: print the filename
    
    file_list = reuters.fileids()

    for file in file_list:
        raw_text = reuters.raw(file)

        file_name = file.split('/')[1]

        out_file = out_path / f'{file_name}.txt'
        with out_file.open('w', encoding='utf-8') as f:
            f.write(raw_text)
        
        _, doc_name = file.split('/', 1)
        if doc_name.startswith('1111'):
            out_file = small_set_path / f'{doc_name}.txt'
            with out_file.open('w', encoding='utf-8') as f:
                f.write(raw_text)



if __name__ == '__main__':
    main()

