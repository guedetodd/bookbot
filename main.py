from stats import (
    full_book,
    word_counter,
    letter_counter,
    formatted
        )
import sys

args = sys.argv

def main(arguments):
    if len(arguments) == 2:
        book_contents = full_book(arguments[1])
        word_count = word_counter(book_contents)
        l_count = letter_counter(book_contents)
        formatted(word_count, l_count)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main(args)
