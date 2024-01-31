#include <iostream>
#include <cmath>

int main()
{
    int v;
    std::cin >> v;

    double res = 0.0;

    for (int i = 1; i <= v; i++)
    {
        res += (1.0/i) * pow(-1, i + 1);
    }

    std::cout << res << std::endl;

    return 0;
}
