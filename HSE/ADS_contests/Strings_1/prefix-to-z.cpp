#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> z_from_prefix(const std::vector<int>& P, int n)
{
    std::vector<int> Z(n, 0);
    for (int i = 1; i < n; i++)
        if (P[i])
            Z[i - P[i] + 1] = P[i];

    Z[0] = 0;

    if (Z[1])
        for (int i = 1; i < Z[1]; i++)
            Z[i + 1] = Z[1] - i;

    int t;
    for (int i = Z[1] + 1; i < n - 1; i++)
    {
        t = i;
        if (Z[i] && !Z[i + 1])
            for (int j = 1; j < Z[i] && Z[i + j] <= Z[j]; j++)
            {
                Z[i + j] = std::min(Z[j], Z[i] - j);
                t = i + j;
            }
        i = t;
    }
    return Z; 
}

int main()
{
    int n;
    std::cin >> n;
    std::vector<int> P_array(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> P_array[i];
    }

    std::vector<int> Z = z_from_prefix(P_array, n);
    for (int i = 0; i < n; i++) 
    {
        std::cout << Z[i] << " ";
    }
    std::cout << std::endl; 
}