from stats import count_words
from stats import count_characters


def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content



def main():


    frankenstein = get_book_text("books/frankenstein.txt") 
    content = frankenstein
    word_count = count_words(content)
    char_counts = count_characters(content)
    print(f"Found {word_count} total words")
    print( char_counts)
    



main()