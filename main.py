from stats import count_characters, count_words, get_book_text, print_report, get_num_words
import sys
def main ():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = count_characters(text)
    print_report(book_path, num_words, chars_dict)

main()
