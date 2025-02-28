
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
def count_words(str):
    return len(str.split())

def count_characters(str):
    chars = {}
    for char in str:
        lower_char = char.lower()
        if not lower_char in chars:
            chars[lower_char] = 0
        chars[lower_char] += 1
    return chars
def print_report(book_path, num_words, chars_dict):
    print(f'--- Begin report of {book_path} ---')
    print(f'Found {num_words} total words')
    for char in chars_dict:
        if ord(char) >= 97 and ord(char) <= 122:
            print(f"'{char}: {chars_dict[char]}'")
    print('--- End report ---')

def get_num_words(text):
    words = text.split()
    return len(words)