def bigger_price(limit, data):
    tops = {}
    for i in range(len(data)):
        tops[i] = data[i]['price']
    
    sorted_values = sorted(tops.values(), reverse=True)
    new_sorted_dictionary = {}
    for i in sorted_values:
        for k in tops.keys():
            if tops[k] == i:
                new_sorted_dictionary[k] = tops[k]
                break

    mems = []
    for el in new_sorted_dictionary.keys():
        mems.append(el)

    
    output = []
    for i in range(limit):
        x=mems[i]
        output.append(data[x])
    return output


assert bigger_price(
    2,
    [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1},
    ],
) == [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}]
assert bigger_price(
    1, [{"name": "pen", "price": 5}, {"name": "whiteboard", "price": 170}]
) == [{"name": "whiteboard", "price": 170}]

print("The mission is done! Click 'Check Solution' to earn rewards!")
