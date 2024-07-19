#include <iostream>

int sumTwoNumbers(int a, int b)
{
    return a + b;
}

int main()
{
    int num1, num2;
    std::cin >> num1;
    std::cin >> num2;
    int sum = sumTwoNumbers(num1, num2);
    std::cout << sum << std::endl;
    return 0;
}