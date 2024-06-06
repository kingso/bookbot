
def text_count(text):
    return len(text.split())

def main():
    text_content = ""
    with open('books/frankenstein.txt') as f:
#        print(f.read())
        text_content += f.read()

    char_dict = {}

    for c in text_content.lower():
        if not c.isalpha():
            continue
        if c not in char_dict:
            char_dict[c] = 1
        else:
            char_dict[c] += 1
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{text_count(text_content)} words found in the document")
    for k, v in char_dict.items():

        print(f"The '{k}' character was found {v} times")



    #print(char_dict)



main()
