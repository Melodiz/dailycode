#include <iostream>
#include <vector>

bool canWin(int n, int m)
{
    std::vector<std::vector<int>> data(n + 1, std::vector<int>(m + 1, 0));

    // Initialize the first row and first column
    for (int j = 1; j < m+1; ++j)
    {
        if (!data[0][j - 1]) { data[0][j] = 1; }
    }
    for (int i = 1; i < n+1; ++i)
    {
        if (!data[i - 1][0]) { data[i][0] = 1; }
    }

    // Fill the rest of the data table
    for (int a = 1; a < n+1; ++a)
    {
        for (int b = 1; b < m+1; ++b)
        {
            if ((data[a - 1][b - 1] && data[a][b - 1] && data[a - 1][b]))
                data[a][b] = 0;
            else 
                data[a][b] = 1;
        }
    }

    return data[n][m];
}

int main()
{
    int n, k;
    std::cin >> n >> k;
    if (canWin(n, k))
    {
        std::cout << "Win\n";
    }
    else
    {
        std::cout << "Loose\n";
    }
    return 0;
}