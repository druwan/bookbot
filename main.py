from stats import get_num_words, get_num_chars


def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(get_num_chars(text))


main()
