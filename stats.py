def get_book_text(book_file_path):
    with open(book_file_path) as book:
        book_contents = book.read()
        return book_contents

def word_count(book_string):
    words = book_string.split()
    num_words = len(words)
    word_count_str = f"Found {num_words} total words"
    return word_count_str

def char_count(book_string):
    book_chars = list(book_string)
    book_dict = {}
    for c in book_chars:
        if c.lower() in book_dict:
            book_dict[c.lower()] += 1
        else:
            book_dict[c.lower()] = 1
    return book_dict

def sort_book_report(book_dict):
    sorted_book_list = []
    for c in book_dict:
        if c.isalpha():
            char_dict = {}
            char_dict["char"] = c
            char_dict["num"] = book_dict[c]
            sorted_book_list.append(char_dict)
    sorted_book_list.sort(reverse=True, key=sort_by)
    return sorted_book_list

def sort_by(dict):
    return dict["num"]