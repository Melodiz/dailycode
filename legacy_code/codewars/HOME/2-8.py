def backward_string_by_word(text):
    cur_text = ''
    all_text = ''
    for el in text:
        if el != ' ':
            cur_text += el
        else:
            cur_text = list(cur_text); cur_text.reverse();cur_text=''.join(cur_text)
            all_text += cur_text
            cur_text = ''
            all_text += el
    
    cur_text = list(cur_text); cur_text.reverse();cur_text=''.join(cur_text)
    all_text += cur_text
    cur_text = ''

    return all_text


# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
