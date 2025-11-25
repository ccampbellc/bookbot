from stats import get_num_words, get_chars_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {word_count} total words")
    print(chars_dict)


main()