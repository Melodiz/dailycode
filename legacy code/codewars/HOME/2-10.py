def second_index(text: str, symbol: str) -> [int, None]:
    x=0
    for el in range(len(text)):
        if text[el] == symbol:
            if x == 1:
                return el
            x+=1
    return None


print("Example:")
print(second_index("sims", "s"))

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
