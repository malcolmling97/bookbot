from stats import get_count_words

def main():
    path = "books/frankenstein.txt"
    frank_contents = get_contents(path)
    frank_words = get_count_words(frank_contents)
    frank_char_dict = get_char_count(frank_contents)

    # print (frank_contents)
    print ("--- Begin report of books/frankenstein.txt ---")
    print (f"{frank_words} words were found in the document")
    # print (sorted(frank_char_dict.items(),key=lambda x: x[1], reverse=True))
    sorted_list = sorted(frank_char_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(0,len(sorted_list)):
        print(f"The '{sorted_list[i][0]}' character was found {sorted_list[i][1]} times")
    
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