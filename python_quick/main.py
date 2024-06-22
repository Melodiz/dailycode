import sympy as sp

# Define the variables
z, x, y = sp.symbols('z x y')

# Define the polynomials
f1 = x+y+z -3
f2 = x**2+y**2+z**2 - 3
f3 = x**3+y**3+z**3 - 1


# Create the ideal
I = [f1, f2, f3]

# Compute the Grobner basis with respect to the lexicographic order
G = sp.groebner(I, x, y, z, order='lex')

# Print the Grobner basis
print("Grobner basis:")
for g in G:
    print(g)