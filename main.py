from stats import word_counter

def main(book_path = "books/frankenstein.txt"):
    text = get_book_text(book_path)
    num_words = word_counter(text)
    print(f"{num_words} words found in the document")

def get_book_text(book):
    with open(book) as f:
        return f.read()

main()
