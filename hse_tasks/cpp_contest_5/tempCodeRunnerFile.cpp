#include <assert.h>
#include <cmath>
#include <complex>
#include <iostream>

class Complex;
void test(Complex num1, Complex num2);

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
        res.re = re * obj.re - im * obj.im;
        res.im = re * obj.im + im * obj.re;
        return res;
    }

    Complex operator/(Complex const& obj)
    {
        Complex res;
        double denominator = pow(obj.re, 2) + pow(obj.im, 2);
        res.re = (re * obj.re + im * obj.im) / denominator;
        res.im = (im * obj.re - re * obj.im) / denominator;
        return res;
    }
    Complex operator+() const
    {
        Complex res;
        res.re = +re;
        res.im = +im;
        return res;
    }

    Complex operator-() const
    {
        Complex res;
        res.re = -re;
        res.im = -im;
        return res;
    }
    double Re()
    {
        return re;
    }
    double Im()
    {
        return im;
    }
};

double abs(const Complex& num)
{
    double res = 0;
    res += sqrt(pow(num.re, 2) + pow(num.im, 2));
    return res;
}
bool operator==(const Complex& n1, const Complex& n2)
{
    return (n1.re == n2.re && n1.im == n2.im);
}
bool operator!=(const Complex& n1, const Complex& n2)
{
    return !(n1 == n2);
}
