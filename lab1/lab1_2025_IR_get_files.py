import os
from nltk.corpus import reuters
# nltk.download('reuters')  # TODO: Uncomment if needed

def main():
    os.makedirs('./reuters', exist_ok=True)  # This creates a directory unless you already have one.
    # Make sure the path is correct (i.e., is in accordance with the structure of directories and files under Section 8 
    #in the lab instructions

    # TODO: Get the list of Reuters file IDs
    # TODO: For each file ID:
    #   - Get the raw text
    #   - Create a filename based on the file ID
    #   - Write the text to a .txt file in './reuters'
    #   - Optionally: print the filename
    pass

if __name__ == '__main__':
    main()

