#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    if (n <= 6)
    {
        std::cout << "No" << std::endl;
        return 0;
    }
    std::cout << "Yes" << std::endl;
    std::cout << n << " ";
    for (int i = 1; i < n; ++i)
    {
        std::cout << i << " ";
    }
    return 0;
}