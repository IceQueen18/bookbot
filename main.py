import sys
from stats import get_text_words
from stats import get_text
from stats import sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) != 2:
          print("Usage: python3 main.py <path_to_book>")
          sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    word_count = get_text_words(book)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    num_text = get_text(book)
    char_count_list = []
    for key, value in num_text.items():
        char_count_list.append({"char": key, "num": value})
    char_count_list.sort(reverse=True, key=sort_on)
    for char in char_count_list:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")

main()
