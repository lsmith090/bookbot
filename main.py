from stats import generate_report
import sys

def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    generate_report(book_text, book_path)

main()