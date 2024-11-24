def main():
        file_path = "books/frankenstein.txt"
        text = get_book_text(file_path)
        num_words = word_count(text)
        char_dict = char_count(text)
        chars_sorted_list = char_dict_to_sorted_list(char_dict)

        print(f"--- Begin report of {file_path} ---")
        print(f"{num_words} words found in the document")
        print()

        for item in chars_sorted_list:
            if not item["char"].isalpha():
                  continue
            print(f"The '{item["char"]}' character was found {item["num"]} times.")
        print("--- End report ---")

def get_book_text(file_path):
     with open(file_path) as f:
        return f.read()
     
def word_count(word_string):
    word_list = word_string.split()
    count = len(word_list)
    return count

def char_count(string):
    char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = {}
    string_lower = string.lower()
    for item in char_list:        
        count = string_lower.count(item)
        result[item] = count
    return result

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict:
          sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()