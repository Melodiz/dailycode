from itertools import product

def f(x, y, z):
    return (not (x or y)) or x

def g(x, y, z, t):
    return ((z or y) <= ((not x) ^ y)) <= (t and y)

def vector_representation_f():
    result = []
    for x, y, z in product([0, 1], repeat=3):
        result.append(f(x, y, z))
    return result

def vector_representation_g():
    result = []
    for x, y, z, t in product([0, 1], repeat=4):
        result.append(g(x, y, z, t))
    return result

print("Vector representation of f(x,y,z) = (x↓y) | x:", list(map(int, vector_representation_f())))
print("Vector representation of g(x,y,z,t) = (z∨y) → (¬x⊕y) → (t∧y):", list(map(int, vector_representation_g())))
