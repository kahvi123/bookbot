


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    textlower = text.lower()
    count_characters = {}
    for char in textlower:
        if char.isalpha():
            if char in count_characters:
                count_characters[char] += 1
            else:
                count_characters[char] = 1
    return count_characters


#def sort_by_character(count_dict):