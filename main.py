from stats import (
    full_book,
    word_counter,
    letter_counter,
    formatted
        )
import sys

def main(book_path):
    book_contents = full_book(book_path)
    word_count = word_counter(book_contents)
    l_count = letter_counter(book_contents)
    formatted(word_count, l_count)

main()
