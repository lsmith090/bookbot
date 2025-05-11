from stats import get_word_count, get_character_count, generate_report

def get_book_text(path):
    with open(path) as book:
        book_contents = book.read()
    return book_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    generate_report(book_text, book_path)

main()