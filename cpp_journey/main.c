#include <stdio.h>
#include <math.h>

int factorial(int n) { // compute factorial of n
    if (n == 0) return 1; // base case
    return n * factorial(n - 1); // recursive case
}

double calculate(double x, double n)
{  // calculate the term of the Taylor series (kinde of)
    return pow(-x, n) / factorial(n + 1);
}

int main()
{
    double x; 
    printf("Введите число x в интревале от -1 до 1, например 0.25"); // выводим число
    scanf("%lf", &x); // вводим число
    int n = 0; // количество слагаемых
    double result = 0; // результат

    while (fabs(calculate(x, n)) >= pow(10, -5))
    {  // пока не достигнем заданной точности
        result += calculate(x, n); // добавляем слагаемое
        n++; // увеличиваем количество слагаемых
    }
    printf("%lf\n", result); // выводим результат
    return 0;
}