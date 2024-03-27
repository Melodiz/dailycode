#include <assert.h>
#include <cmath>
#include <iostream>

Class Rational()
{
public:
    int nu;
    int de;
    int div;

    Rational(int numerator = 0, int denumerator = 1)
    {
        div = std::gcd(numerator, denumerator)
        nu = numerator/div;
        de = denumerator/div;

        if (denom < 0)
        {
            de = -denumerator/div;
            nu = numerator/div;
        }
        
    }
}