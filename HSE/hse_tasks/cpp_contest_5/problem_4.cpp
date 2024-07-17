#include <algorithm>
#include <assert.h>
#include <cmath>
#include <iostream>
#include <numeric>

// class Rational;
// void test();

class Rational
{
public:
    int nu;
    int de;
    int div;

    Rational(int numerator = 0, int denumerator = 1)
    {
        div = std::gcd(numerator, denumerator);

        if (denumerator < 0)
        {
            de = -denumerator / div;
            nu = -numerator / div;
        }
        else
        {
            de = denumerator / div;
            nu = numerator / div;
        }
    }
    
    int numerator() const
    {
        return nu;
    }
    int denominator() const
    {
        return de;
    }

    Rational operator=(const Rational& obj)
    {
        nu = obj.nu;
        de = obj.de;
        return *this;
    }

    Rational operator=(const int num)
    {
        nu = num;
        de = 1;
        return *this;
    }

    Rational operator+(const Rational& obj) const
    {
        return Rational{nu * obj.de + obj.nu * de, de * obj.de};
    }
    Rational operator+(const int& obj) const
    {
        return Rational{nu + obj * de, de};
    }
    Rational operator+=(const Rational& obj)
    {
        *this = *this + obj;
        return *this;
    }

    Rational operator-(const Rational& obj) const
    {
        return -obj + *this;
    }
    Rational operator-(const int obj) const
    {
        return Rational{nu - obj * de, de};
    }
    friend Rational operator-(const int num, const Rational& obj)
    {
        return Rational{num * obj.de - obj.nu, obj.de};
    }
    Rational operator-=(const Rational& obj)
    {
        *this = *this - obj;
        return *this;
    }

    Rational operator*(const Rational& obj) const
    {
        return Rational{nu * obj.nu, de * obj.de};
    }
    Rational operator*(const int obj) const
    {
        return Rational{obj * nu, de};
    }
    friend Rational operator*(const int num, const Rational& obj)
    {
        return Rational{num * obj.nu, obj.de};
    }
    Rational operator*=(const Rational& obj)
    {
        *this = *this * obj;
        return *this;
    }

    Rational operator/(const Rational& obj)
    {
        return Rational{nu * obj.de, de * obj.nu};
    }
    Rational operator/=(const Rational& obj)
    {
        *this = *this / obj;
        return *this;
    }

    Rational operator-() const
    {
        return Rational{-nu, de};
    }
    Rational operator+() const
    {
        return Rational{nu, de};
    }

    Rational& operator++()
    {
        *this += 1;
        return *this;
    }

    Rational operator++(int)
    {
        Rational res = *this;
        operator++();
        return res;
    }

    Rational& operator--()
    {
        *this -= 1;
        return *this;
    }

    Rational operator--(int)
    {
        Rational res = *this;
        operator--();
        return res;
    }
};

bool operator==(const Rational a, const Rational b)
{
    return (a.nu == b.nu && a.de == b.de);
}
bool operator!=(const Rational a, const Rational b)
{
    return (a.nu != b.nu || a.de != b.de);
}

// int main()
// {
//     test();
//     return 0;
// }

// void test()
// {
//     using namespace std;
//     Rational n1(35, 14);
//     Rational n2(135, 10);

//     double a1 = 2.5;
//     double a2 = 13.5;

//     assert((n1 + n2).nu == 16 && (n1 + n2).de == 1);
//     // assert((7 + n1).nu == 19 && (n1+7).de == 2);
//     cout << "Checkpoint #1\n";

//     assert((n1 * n2).nu == 135 && (n1 * n2).de == 4);
//     assert((7 * n1).nu == 35 && (n1 * 7).de == 2);
//     cout << "Checkpoint #2\n";
// }