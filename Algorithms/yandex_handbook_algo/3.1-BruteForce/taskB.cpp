#include <iostream>

int NumberOfCombination(int n, int k)
{
    if (k == 0 || k == n)
        return 1;
    else
        return NumberOfCombination(n - 1, k - 1) + NumberOfCombination(n - 1, k);
}

int main()
{
    int n, k;
    std::cin >> n >> k;
    if (n < k)
    {
        std::cout << 0 << std::endl;
    }
    else
    {
        std::cout << NumberOfCombination(n, k) << std::endl;
    }
    return 0;
}