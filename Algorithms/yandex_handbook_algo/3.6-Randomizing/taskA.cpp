#include <vector>
#include <algorithm>
#include <iostream>

void Lomuto_partition(std::vector<int>& data, int pivot)
{
    int i = 0;
    for (int j = 1; j < data.size(); j++)
    {
        if (data[j] <= pivot)
        {
            i++;
            std::swap(data[i], data[j]);
        }
    }
   std::swap(data[i], data[0]);
    
}

int main()
{
    int n, p;
    std::cin >> n;
    std::vector<int> data;
    for (int j = 0; j < n; ++j)
    {
        std::cin >> p;
        data.push_back(p);
    }
    Lomuto_partition(data, data[0]);
    for (int j = 0; j < n; ++j)
    {
        std::cout << data[j] << ' ';
    }
    return 0;
}