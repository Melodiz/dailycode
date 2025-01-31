#include <iostream>
#include <vector>

std::vector<int> vec_mul(const std::vector<int> &a, const std::vector<int> &b, int mod, int n)
{
    std::vector<int> res(n);
    for (int i = 0; i < n; ++i)
    {
        res[i] = a[i] * b[i] % mod;
    }
    return res;
}

std::vector<int> fast_pow(const std::vector<int> &initial, int k, int mod, int n)
{
    std::vector<int> result(k + 1, 0);
    std::vector<int> current = initial;
    std::vector<int> temp(n);

    for (int i = 1; i <= k; ++i)
    {
        int sum = 0;
        for (int j = 0; j < n; ++j)
        {
            sum = (sum + current[j]) % mod;
        }
        result[i] = sum;

        if (i < k)
        {
            temp = vec_mul(current, current, mod, n);
            current = std::move(temp);
        }
    }

    return result;
}

int main()
{
    int n, k;
    std::cin >> n >> k;
    std::vector<int> initial(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> initial[i];
    }
    int mod = 998244353;
    // do first steps:
    std::vector<int> result;
    
    for (int i = 0; i < n; ++i) {
        for (int j = i+1; j < n; ++j) {
            result.push_back(initial[i] + initial[j]);
        }
    }

    std::vector<int> ans = fast_pow(result, k, mod, n);
    for (int i = 0; i < k+1; ++i)
    {
        std::cout << ans[i] << "\n";
    }
    std::cout << std::endl;
    return 0;
}
