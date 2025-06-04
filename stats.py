def get_num_words(input_text):
    num_words = len(input_text.split())
    return num_words


def get_chars_dict(input_text):
    chars = {}
    words_list = input_text.split()
    for word in words_list:
        for ch in word.lower():
            if ch in chars:
                chars[ch] += 1
            else:
                chars[ch] = 1
    return chars


def sort_on(d):
    return d["count"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "count": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
