import sys
from stats import word_count, char_counts, char_srtd

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print(f"path to book: {filepath}")

    text = get_book_text(filepath)
    num_words = word_count(text)
    char_frequency = char_counts(text)
    sorted_list = char_srtd(char_frequency)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for each_word in sorted_list:
        char = each_word["char"]
        count = each_word["count"]
        
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")
    
def get_book_text(filepath):

    with open(filepath) as f:
        return f.read()

if __name__ == "__main__":
    main()



    
