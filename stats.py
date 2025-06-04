def get_num_words(input_text):
    num_words = len(input_text.split())
    return num_words


def get_num_chars(input_text):
    chars = {}
    words_list = input_text.split()
    for word in words_list:
        for ch in word.lower():
            if ch in chars:
                chars[ch] += 1
            else:
                chars[ch] = 1
    return chars
