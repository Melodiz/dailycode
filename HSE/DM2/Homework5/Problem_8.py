from itertools import product

def nor(x: bool, y: bool) -> bool:
    return not (x or y)

def f(x, y, z):
    print(f"{x} {y} {z} -> {int(nor(x, y)), int(nor(x, y) or x)}")
    return (nor(x, y) or x)

def g(x, y, z, t):
    out = [
        z or y, 
        (not x) ^ y, 
        t and y,
        int((z or y) <= ((not x) ^ y)),
        int((((z or y) <= ((not x) ^ y)) <= (t and y)))
    ]
    print(f"{x} {y} {z} {t} -> {out}")
    return (((z or y) <= ((not x) ^ y)) <= (t and y))

def vector_representation_f():
    result = []
    print("\nx, y, z -> f(x, y, z)")
    for x, y, z in product([0, 1], repeat=3):
        result.append(f(x, y, z))
    return result

def vector_representation_g():
    result = []
    print("\nx, y, z, t -> g(x, y, z, t)")  
    for x, y, z, t in product([0, 1], repeat=4):
        result.append(g(x, y, z, t))
    return result

print("Vector representation of f(x,y,z) = (x↓y) | x:", list(map(int, vector_representation_f())))
print("Vector representation of g(x,y,z,t) = (z∨y) → (¬x⊕y) → (t∧y):", list(map(int, vector_representation_g())))