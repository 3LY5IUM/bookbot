import sys

def sorted_on(count_tuple):
    return count_tuple[1]

def get_book_words(path:str):
    with open(path) as f:
        text = f.read()
    split = text.split()
    num_words=len(split)
    return num_words

def get_book_chars(path:str):
    with open(path) as f:
        file_content=f.read()
    count = {}
    for char in file_content.lower():
        if not char.isalpha():
            continue
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    count = dict(sorted(count.items(), reverse=True, key=sorted_on))

    return count

def pretty_print(path:str):
    num_word=get_book_words(path)
    print (f"""============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {num_word} total words
    --------- Character Count -------
    """)

    for key, value in get_book_chars(path).items():
        print(f"{key}: {value}")
    print("============= END ===============")


def usage():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(2)



