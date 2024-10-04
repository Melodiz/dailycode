from itertools import product


def f(x, y):
    if x == 1 and y == 0: return 1
    return 0


def h(x, y):
    return (x or y)


def g(x, y, z):
    if (x, y, z) in [(0, 0, 0), (0, 1, 0),
        (0, 1, 1), (1, 0, 1), (1, 1, 0)]:
        return 1
    return 0


def tasks():
    print('\nTask A:')
    for x, y, z in product([0, 1], repeat=3):
        print(f"{x} {y} {z} -> {f(z, y), g(x, z, y), h(f(z, y), g(x, z, y))}")
    print('\nTask B:')
    for x, y, z in product([0, 1], repeat=3):
        print(f"{x} {y} {z} -> {g(y, z, x), h(x, x), f(g(y, z, x), h(x, x))}")

# def truthtables():
#     print("x, y -> f(x, y)")
#     for x, y in product([0, 1], repeat=2):
#         print(f"{x} {y} -> {f(x, y)}")
#     print("x, y -> h(x, y)")
#     for x, y in product([0, 1], repeat=2):
#         print(f"{x} {y} -> {h(x, y)}")
#     print("x, y, z -> g(x, y, z)")
#     for x, y, z in product([0, 1], repeat=3):
#         print(f"{x} {y} {z} -> {g(x, y, z)}")


if __name__ == "__main__":
    # truthtables()
    tasks()
