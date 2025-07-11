def full_book(book_path):
    with open(book_path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def letter_counter(text):
    lower = text.lower()
    l_count = {}

    for letter in lower:
        if letter in l_count:
            l_count[letter]["num"] +=1
        else:
            l_count[letter] = {"char": letter, "num": 1}
    sorted_l_count = list(sorted(l_count.values(), key=lambda item: item["num"], reverse=True))
    return sorted_l_count

def formatted(word_count, l_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in l_count:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")
