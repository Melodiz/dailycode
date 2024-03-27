#include <complex>
#include <iostream>
#include <assert.h>

class Complex
{
public:
    double re;
    double im;

    Complex(double _reVal = 0.0, double _imVal = 0.0)
    {
        re = _reVal;
        im = _imVal;
    }

    Complex operator+(Complex const& obj)
    {
        Complex res;
        res.re = re + obj.re;
        res.im = im + obj.im;
        return res;
    }

    Complex operator-(Complex const& obj)
    {
        Complex res;
        res.re = re - obj.re;
        res.im = im - obj.im;
        return res;
    }
    Complex operator*(Complex const& obj)
    {
        Complex res;
        res.re  = re * obj.re - im * obj.im;
        res.im = re*obj.im + im * obj.re;
        return res;
    }
};

void print(Complex num)
{
    std::cout << (num).re << " + " << (num).im << "i" << std::endl;
}

int main()
{
    using namespace std;
    
    Complex num1(10, 5);
    Complex num2(-3.5, 4.2);

    Complex num3 = num1 + num2;
    assert(num3.re == 6.5);

    return 0;
}