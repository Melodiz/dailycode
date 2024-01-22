from collections import Counter
import operator


def most_frequent(data: list[str]) -> str:
    ans = Counter(data)

    x = max(ans.items(), key=operator.itemgetter(1))

    return x[0]


assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
