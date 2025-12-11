def get_num_words(text):
    word_list = text.split()
    return len(word_list)


def get_char_count(text):
    char_dict = {}
    word_list = text.split()
    for word in word_list:
        characters = list(word)
        for character in characters:
            character = character.lower()
            value = char_dict.get(character, 0)
            if value == 0:
                char_dict[character] = 0
            char_dict[character] = value + 1
    return char_dict


def sort_on(items):
    return items["num"]


def sort_dict(char_dict):
    new_dict = []
    for key in char_dict:
        new_dict.append({"char": key, "num": char_dict[key]})
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict
