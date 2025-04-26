def count_words(book_text):
    words = book_text.split()
    number_of_words = len(words)

    return number_of_words

def count_char(book_text):
    d = {}
    book_txt = book_text.lower()

    for char in book_txt:
        if (char in d) == False:
            d[char] = 1
        else:
            d[char] += 1

    return d

def sort_on(dict):
    return dict["num"]

def sorted_dict(dictionary):
    list = []
    
    for key, value in dictionary.items():
        temp = {}
        temp["char"] = key
        temp["num"] = value
        list.append(temp)

    list.sort(reverse=True,key=sort_on)
    return list
