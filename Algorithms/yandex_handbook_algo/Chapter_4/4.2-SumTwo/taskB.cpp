#include <iostream>
#include <vector>

void sumPols(const std::vector<int>& A, const std::vector<int>& B, int n, int m)
{
    if (n > m)
    {
        std::vector<int> result = A;
        for (int i = 0; i < m; i++) { result[i + n - m] += B[i]; }
        for (int i = 0; i < result.size(); i++) { std::cout << result[i] << ' '; }
    }
    else
    {
        std::vector<int> result = B;
        for (int i = 0; i < n; i++) { result[i + m - n] += A[i]; }
        for (int i = 0; i < result.size(); i++) { std::cout << result[i] << ' '; }
    }
}

int main()
{
    int n, m, p;
    std::vector<int> polA;
    std::vector<int> polB;

    std::cin >> n;
    for (int j = 0; j < n+1; j++)
    {
        std::cin >> p;
        polA.push_back(p);
    }
    std::cin >> m;
    for (int j = 0; j < m+1; ++j)
    {
        std::cin >> p;
        polB.push_back(p);
    }
    std::cout << std::max(n,m) <<std::endl;
    sumPols(polA, polB, n+1, m+1);
    return 0;
}