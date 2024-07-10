def correct_sentence(text: str) -> str:
    """
    returns a corrected sentence which starts with a capital letter
    and ends with a dot.
    """
    # your code here

    """ 
   if text[0] == text[0].upper():
        if text[-1] == '.':
            return text
        else:
            text = list(text)[-1] = '.'
            text = ''.join(text)
            return text
    else:
        text = list(text)[0] = text[0].upper()
        text = ''.join(text)
        if text[-1] == '.':
            return text
        else:
            text = list(text)[-1] = '.'
            text = ''.join(text)
            return text
    """
    text = text[0].upper() + text[1:]
    if text[-1]!= '.':
        text+='.'
        return text
    return text




print("Example:")
print(correct_sentence("greetings, friends"))

assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")
