from stats import get_count_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # print("Arguments: ", sys.argv, len(sys.argv))
    path = sys.argv[1]
    frank_contents = get_contents(path)
    frank_words = get_count_words(frank_contents)
    frank_char_dict = get_char_count(frank_contents)

    # print (frank_contents)
    print (f"--- Begin report of {sys.argv[1]} ---")
    print (f"{frank_words} words were found in the document")
    # print (sorted(frank_char_dict.items(),key=lambda x: x[1], reverse=True))
    sorted_list = sorted(frank_char_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(0,len(sorted_list)):
        print(f"{sorted_list[i][0]}: {sorted_list[i][1]}")
    
    print("--- End report ---")


def get_contents(path):
    with open(path) as f:
        return f.read()

def get_char_count(content):
    dict = {}
    lowered_content = content.lower()
    for letter in lowered_content:
        if letter.isalpha():
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
 
    return dict





main()