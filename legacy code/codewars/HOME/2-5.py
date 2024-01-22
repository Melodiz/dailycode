def first_word(text: str) -> str:
    alf = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    kh = "., "

    text = text.split()
    for el in text:
        if el[0] in alf:
            output_word = el
            break

    for i in range(len(output_word)):
        if output_word[i] in kh:
            return output_word[:i]
    return output_word


print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
