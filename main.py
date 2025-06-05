from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
import sys


def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")


def main():
    book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        chars_dict = get_chars_dict(text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
        print_report(book_path, num_words, chars_sorted_list)


main()
