#include <iostream>
#include <vector>

// Function to merge two sorted subarrays
void merge(std::vector<int>& data, int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temporary arrays
    std::vector<int> leftArray(n1);
    std::vector<int> rightArray(n2);

    // Copy data to temporary arrays
    for (int i = 0; i < n1; ++i)
        leftArray[i] = data[left + i];
    for (int i = 0; i < n2; ++i)
        rightArray[i] = data[mid + 1 + i];

    // Merge the temporary arrays back into the original array
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2)
    {
        if (leftArray[i] <= rightArray[j])
        {
            data[k] = leftArray[i];
            ++i;
        }
        else
        {
            data[k] = rightArray[j];
            ++j;
        }
        ++k;
    }

    // Copy the remaining elements of leftArray, if any
    while (i < n1)
    {
        data[k] = leftArray[i];
        ++i;
        ++k;
    }

    // Copy the remaining elements of rightArray, if any
    while (j < n2)
    {
        data[k] = rightArray[j];
        ++j;
        ++k;
    }
}

// Function to implement merge sort
void mergeSort(std::vector<int>& data, int left, int right)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;

        // Recursively sort the first and second halves
        mergeSort(data, left, mid);
        mergeSort(data, mid + 1, right);

        // Merge the sorted halves
        merge(data, left, mid, right);
    }
    return;
}

int main()
{
    int n, p;
    std::cin >> n;
    std::vector<int> data;
    for (int i = 0; i < n; ++i)
    {
        std::cin >> p;
        data.push_back(p);
    }

    // Call mergeSort on the entire array
    mergeSort(data, 0, data.size() - 1);

    // Print the sorted array
    for (const auto& value: data)
    {
        std::cout << value << ' ';
    }
    std::cout << std::endl;

    return 0;
}