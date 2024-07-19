#include <algorithm>
#include <iostream>
#include <vector>

long long max_product(const std::vector<long>& arr, int n)
{
    long a = std::max(arr[0], arr[1]);
    long b = std::min(arr[0], arr[1]);
    for (int i = 2; i < n; i++)
    {
        if (arr[i] >= a)
        {
            b = a;
            a = arr[i];
        }
        else if (arr[i] > b)
        {
            b = arr[i];
        }
    }
    return static_cast<long long>(a) * static_cast<long long>(b);
}

int main()
{
    int n; 
    std::cin >> n;
    std::vector<long> arr(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> arr[i];
    }
    test_max_product();  // Uncomment to test the function with various test cases
    std::cout << max_product(arr, n) << std::endl;
    return 0;
}
