#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

int Lomuto_partition(std::vector<int>& data, int low, int high)
{
    int pivot = data[high];
    int i = low - 1;
    for (int j = low; j < high; ++j)
    {
        if (data[j] <= pivot)
        {
            ++i;
            std::swap(data[i], data[j]);
        }
    }
    std::swap(data[i + 1], data[high]);
    return i + 1;   
}

void randomizedQuickSort(std::vector<int>& data, int low, int high)
{
    if (low < high)
    {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(low, high);
        int random_pivot_index = dis(gen);
        std::swap(data[random_pivot_index], data[high]);

        int pivot_index = Lomuto_partition(data, low, high);
        randomizedQuickSort(data, low, pivot_index - 1);
        randomizedQuickSort(data, pivot_index + 1, high);
    }
}

int main()
{
    int n, p;
    std::cin >> n;
    std::vector<int> data(n);
    for (int j = 0; j < n; ++j)
    {
        std::cin >> p;
        data[j] = p;
    }
    randomizedQuickSort(data, 0, n - 1);

    for (int j = 0; j < n; ++j)
    {
        std::cout << data[j] << ' ';
    }
    return 0;
}