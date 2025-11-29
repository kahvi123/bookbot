from stats import count_words, count_characters, sort_by_character


def main():
    frankenstein = get_book_text("books/frankenstein.txt") 
    content = frankenstein
    word_count = count_words(content)
    char_counts = count_characters(content)
    sortbycount = sort_by_character(char_counts)
    #print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\n\n--------- Character Count -------")
    print(f"Found {word_count} total words")
    for count in sortbycount:
        print(f"{count["char"]}: {count["num"]}")
    #print(*sortbycount, sep="\n")
    #print("============= END ===============")





def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        return content


    

main()