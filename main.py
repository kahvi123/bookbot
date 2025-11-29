from stats import count_words, count_characters, sort_by_character, check_args
import sys


def main():
    check_args()
    path = sys.argv[1]
    content = get_book_text(path)
    word_count = count_words(content)
    char_counts = count_characters(content)
    sortbycount = sort_by_character(char_counts)
    print(f"Found {word_count} total words")
    for count in sortbycount:
        print(f"{count["char"]}: {count["num"]}")



def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content


main()