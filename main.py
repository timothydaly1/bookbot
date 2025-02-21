import sys
from stats import count_words, count_chars, get_list_of_chars

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    text = get_book_text(path)
    num_words = count_words(text)
    chars = count_chars(text)
    list_of_chars = get_list_of_chars(chars)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in list_of_chars:
        for char in dict:
            if char.isalpha():
                print(f"{char}: {dict[char]}")
    
    print("============= END ===============")



main()