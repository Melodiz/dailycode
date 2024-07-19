#include <algorithm>
#include <iostream>
#include <vector>


long long optimized_solution(std::vector<int> arr, int n)
{
    std::sort(arr.begin(), arr.end());
    long long product1 = static_cast<long long>(arr[n - 1]) * arr[n - 2] * arr[n - 3] * arr[n-4];
    long long product2 = static_cast<long long>(arr[0]) * arr[1] * arr[n - 1] * arr[n - 2];
    long long product3 = static_cast<long long>(arr[0]) * arr[1] * arr[2] * arr[3];
    return std::max(std::max(product1, product2), product3);
}

int main()
{
    int n;
    std::cin >> n;
    std::vector<int> arr(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> arr[i];
    }

    std::cout << optimized_solution(arr, n) << std::endl;
    return 0;
}
