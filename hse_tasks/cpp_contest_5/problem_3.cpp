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

int main()
{
    using namespace std;

    Complex num1(10.3, -5.1);
    Complex num2(-3.5, 4.2);

    test(num1, num2);
    return 0;
}

void test(Complex num1, Complex num2)
{
    std::complex<double> n1(num1.re, num1.im);
    std::complex<double> n2(num2.re, num2.im);
    double dif = 0.0001;

    assert((num1 + num2).re - real(n1 + n2) < dif && (num1 + num2).im - imag(n1 + n2) < dif);
    std::cout << "Checkpoint #1\n";

    assert((num1 - num2).re - real(n1 - n2) < dif && (num1 - num2).im - imag(n1 - n2) < dif);
    std::cout << "Checkpoint #2\n";

    assert((num1 * num2).re - real(n1 * n2) < dif && (num1 * num2).im - imag(n1 * n2) < dif);
    std::cout << "Checkpoint #3\n";

    assert((num1 / num2).re - real(n1 / n2) < dif && (num1 / num2).im - imag(n1 / n2) < dif);
    assert((num2 / num1).re - real(n2 / n1) < dif && (num2 / num1).im - imag(n2 / n1) < dif);
    std::cout << "Checkpoint #4\n";

    assert((num1 - 5.43).re - real(n1 - 5.43) < dif && (num1 - 5.43).im - imag(n1 - 5.43) < dif);

    assert((num1 + 5.43).re - real(n1 + 5.43) < dif && (num1 + 5.43).im - imag(n1 + 5.43) < dif);
    std::cout << "Checkpoint #5\n";

    assert((-num1).re - real(-n1) < dif && (-num1).im - imag(-n1) < dif);
    assert((+num1).re - real(+n1) < dif && (+num1).im - imag(+n1) < dif);
    std::cout << "Checkpoint #6\n";

    assert((num1 * 5.43).re - real(n1 * 5.43) < dif && (num1 * 5.43).im - imag(n1 * 5.43) < dif);
    assert((num1 / 5.43).re - real(n1 / 5.43) < dif && (num1 / 5.43).im - imag(n1 / 5.43) < dif);
    std::cout << "Checkpoint #7\n";

    assert(num1.Im() == num1.im && num1.Re() == num1.re);
    std::cout << "Checkpoint #7\n";

    assert(abs(num1) == std::abs(n1));
    std::cout << "Checkpoint #8\n";

    assert(num1 == num1 && num1 != num2);
    std::cout << "Checkpoint #9\n";

    std::cout << "All tests are passed" << std::endl;
    // std::cout << (((num1 * num2).re) == (real(n1 * n2))) << std::endl;
    // std::cout << (num1 / num2).re  << ' ' << real(n1 / n2) << std::endl;
    // std::cout << (num1 / num2).im  << ' ' << imag(n1 / n2) << std::endl;
    // std::cout << (num1 * num2).re - real(n1 * n2) << std::endl;
}
