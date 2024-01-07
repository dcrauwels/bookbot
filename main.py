def read_book(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    result = {}
    for c in text.lower():
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def book_report(book_path, book_raw, book_letter_dict):
    print(f"--- Begin report of {book_path}")
    print(f"{len(book_raw.split())} words found in the document\n")

    print_letters(book_letter_dict)


def print_letters(l_dict):
    sorted_dict = dict(sorted(l_dict.items(), key= lambda x : x[1], reverse= True))
    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

def count_words(text):
    return "word count: " + str(len(text.split()))

def main():
    frankenstein_path = 'books/frankenstein.txt'
    frankenstein_raw = read_book(frankenstein_path)
    frankenstein_ldict = count_letters(frankenstein_raw)
    book_report(frankenstein_path, frankenstein_raw, frankenstein_ldict)

main()