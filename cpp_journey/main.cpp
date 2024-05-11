#include <iostream>

int powerMod(int base, int exponent, int modulus)
{
    int result = 1;
    base = base % modulus;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

bool isGenerator(int a, int modulus)
{
    for (int m = 1; m < 42; ++m)
    {
        if (powerMod(a, m, modulus) == 1)
            return false;
    }
    return powerMod(a, 42, modulus) == 1;
}

int main()
{
    const int modulus = 49;
    std::cout << "Generators of Z_49: ";
    for (int a = 1; a < modulus; ++a)
    {
        if (isGenerator(a, modulus))
        {
            std::cout << a << " ";
        }
    }
    std::cout << std::endl;
    return 0;
}