#include <iostream>
#include <vector>


void sum_matrices(const std::vector<std::vector<int>>& matrix1, const std::vector<std::vector<int>>& matrix, int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            std::cout << matrix1[i][j] + matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int main()
{
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> matrix1;
    std::vector<std::vector<int>> matrix2;
    for (int i = 0; i < n; i++)
    {
        std::vector<int> row(m);
        for (int j = 0; j < m; j++)
        {
            std::cin >> row[j];
        }
        matrix1.push_back(row);
    }
    for (int i = 0; i < n; i++)
    {
        std::vector<int> row(m);
        for (int j = 0; j < m; j++)
        {
            std::cin >> row[j];
        }
        matrix2.push_back(row);
    }
    sum_matrices(matrix1, matrix2, n, m);
    return 0;
}