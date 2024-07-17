#include <iostream>
#include <map>
#include <string>
#include <vector>

long long normalizer(int avec[], int bvec[], int N);

int main()
{
    // preparing
    int M, N;
    std::cin >> M >> N;
    M--;

    std::string first_name;
    std::cin >> first_name;
    int first_vec[N];
    for (int i = 0; i < N; i++)
    {
        std::cin >> first_vec[i];
    }

    std::string names[M];
    int data[M][N];

    for (int i = 0; i < M; i++)
    {
        std::cin >> names[i];
        for (int j = 0; j < N; j++)
        {
            std::cin >> data[i][j];
        }
    }
    // cooking 
    long long max_val = -9223372036854775800;
    long long cur;
    std::vector<std::string> ans;
    for (int i = 0; i < M; i++)
    {
        cur = normalizer(first_vec, data[i], N);
        if (cur > max_val)
        {
            ans.clear();
            ans.push_back(names[i]);
            max_val = cur;
        }
        else if (cur == max_val)
        {
            ans.push_back(names[i]);
        }
    }

    // printing answer
    for (size_t i = 0; i < ans.size(); i++)
    {
        std::cout << ans[i] << std::endl;
    }

    return 0;
}

long long normalizer(int avec[], int bvec[], int N)
{
    long long ans = 0;
    for (int i = 0; i < N; i++)
    {
        ans += (avec[i] * bvec[i]);
    }
    return ans;
}