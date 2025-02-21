def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_chars(dict):
    for char in dict:
        return dict[char]

def get_list_of_chars(chars):
    list_of_chars = []
    for char in chars:
        list_of_chars.append({char: chars[char]})
    list_of_chars.sort(key=sort_chars, reverse=True)
    return list_of_chars


    
