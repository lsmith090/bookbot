def get_word_count(book):
    word_list = book.split()
    word_count = len(word_list)
    print(f"Found {word_count} total words")

def get_character_count(book):
    book = book.lower()
    character_analysis = {}

    for char in book:
        if char in character_analysis:
            character_analysis[char] += 1
        else:
            character_analysis[char] = 1
    return character_analysis

def get_sorted_characters(book):
    sorted_char_list = []
    char_dict = get_character_count(book)

    for char, count in char_dict.items():
        if char.isalpha():
            item = {
                "char": char,
                "num": count
            }
            sorted_char_list.append(item)
    sorted_char_list.sort(key=sort_char_on, reverse=True)
    for item in sorted_char_list:
        print(f"{item['char']}: {item['num']}")

def sort_char_on(dict):
    return dict["num"]

def generate_report(book, path):
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}")
    print("=================================")
    print("------Word Count------")
    get_word_count(book)
    print("------Character Count------")
    get_sorted_characters(book)