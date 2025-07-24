import sys
from stats import get_book_text, word_count, char_count, sort_book_report
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(word_count(book_text))
    print("--------- Character Count -------")
    book_char_count = char_count(book_text)
    sorted_book_report = sort_book_report(book_char_count)
    for c in sorted_book_report:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()