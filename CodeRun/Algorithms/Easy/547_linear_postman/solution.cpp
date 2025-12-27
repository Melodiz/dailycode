#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

unsigned int cur = 0;
unsigned int a, b;

unsigned int nextRand24() {
    cur = cur * a + b;
    return cur >> 8;
}

unsigned int nextRand32() {
    unsigned int a = nextRand24(), b = nextRand24();
    return (a << 8) ^ b;
}

// Partition function for Quickselect
int partition(std::vector<unsigned int>& arr, int left, int right, int pivotIndex) {
    unsigned int pivotValue = arr[pivotIndex];
    std::swap(arr[pivotIndex], arr[right]);
    int storeIndex = left;
    for (int i = left; i < right; ++i) {
        if (arr[i] < pivotValue) {
            std::swap(arr[i], arr[storeIndex]);
            ++storeIndex;
        }
    }
    std::swap(arr[storeIndex], arr[right]);
    return storeIndex;
}

// Quickselect function to find the k-th smallest element
unsigned int quickselect(std::vector<unsigned int>& arr, int left, int right, int k) {
    if (left == right) {
        return arr[left];
    }
    int pivotIndex = left + rand() % (right - left + 1);
    pivotIndex = partition(arr, left, right, pivotIndex);
    if (k == pivotIndex) {
        return arr[k];
    } else if (k < pivotIndex) {
        return quickselect(arr, left, pivotIndex - 1, k);
    } else {
        return quickselect(arr, pivotIndex + 1, right, k);
    }
}

int main() {
    int n;
    std::cin >> n;
    std::cin >> a >> b;

    std::vector<unsigned int> x(n);
    for (int i = 0; i < n; ++i) {
        x[i] = nextRand32();
    }

    // Find the median using Quickselect
    unsigned int median = quickselect(x, 0, n - 1, n / 2);

    unsigned long long total_distance = 0;
    for (int i = 0; i < n; ++i) {
        total_distance += std::abs(static_cast<long long>(x[i]) - median);
    }

    std::cout << total_distance << std::endl;

    return 0;
}