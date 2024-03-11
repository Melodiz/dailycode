import sys
sys.set_int_max_str_digits(248_621_000)
a = (2**82_589_933-1)
print('passed')
file = open("prime_number", "w")
file.write(str(a))
file.close()
print('end')