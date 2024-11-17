path_to_file = "books/frankenstein.txt"

def count_words(string):
    return len(string.split())
    

def count_chars(string):
    char_count = {}
    for char in string.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) +1
    return char_count

def dict_chopper(dict):
    list_of_dicts = []
    for k,v in dict.items():
        list_of_dicts.append({"letter":k, "value": v})
    return list_of_dicts

def sort_on(dict):
    return dict["value"]

def sort_list(letter_list):
    letter_list.sort(reverse=True, key=sort_on)

def print_report(wordcount, charcount):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document\n")
    for item in charcount:
        print(f"The '{item["letter"]}' character was found '{item["value"]}' times")
    print("\n--- End report ---")

with open(path_to_file) as f:
    file_contents = f.read()
    total_words = count_words(file_contents)
    list_of_dicts = dict_chopper(count_chars(file_contents))
    sort_list(list_of_dicts)
    print_report(total_words, list_of_dicts)
    