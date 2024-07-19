#include <iostream>
#include <string>

void printSkewSum(const std::string& a, const std::string& b, int n)
{
    for (int i = 0; i < n; ++i) { std::cout << a[i] << b[i]; }
}

int main()
{
    int n;
    std::cin >> n;
    std::string a, b;
    std::cin >> a >> b;
    printSkewSum(a, b, n);
    return 0;
}