def get_num_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item["num"]

def character_sorted_list(chars_dict):
    character_sorted_list = []
    for ch in chars_dict:
        character_sorted_list.append({"char": ch, "num": chars_dict[ch]})
    character_sorted_list.sort(reverse=True, key=sort_on)
    return character_sorted_list
