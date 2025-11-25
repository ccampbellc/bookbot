from stats import get_num_words, get_chars_dict, character_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = character_sorted_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")

    print("============= END ===============")


main()