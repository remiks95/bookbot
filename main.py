import sys
from stats import count_words, count_char, sorted_dict
def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    a = count_words(get_book_text(sys.argv[1]))
    characters = get_book_text(sys.argv[1])
    
    new_list = sorted_dict(count_char(characters))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {a} total words")
    print("--------- Character Count -------")
    for i in new_list:
        text = i["char"]
        if text.isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()