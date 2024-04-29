#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}
double calculate(double x, double n)
{
    return pow(-x, n)/factorial(n+1);
}

int main()
{
    double x;
    std::cin >> x;
    int n = 0;
    double result = 0;

    while (abs(calculate(x, n)) >= pow(10, -5))
    {
        result += calculate(x, n);
        n++;
    }
    std::cout << result << std::endl;
    return 0;
}