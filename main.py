import sys
from stats import get_num_words, get_char_count, sort_dict
if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    book = get_book_text(sys.argv[1])
    word_count = get_num_words(book)
    print(f"Found {word_count} total words")
    char_dict = get_char_count(book)
    print("----------- Character Count ----------")
    sorted_dict = sort_dict(char_dict)
    for entry in sorted_dict:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============ END ============")
    
main()