#include <iostream>
#include <vector>

void heapify(int arr[], int n, int i)
{
    int largest = i;
    int left = 2*i+1;
    int right = 2*i+2;

    if (left < n && arr[left]>arr[largest])
    {
        largest = left;
    }
    if (right < n && arr[right]>arr[largest])
    {
        largest = right;
    }
    if (i != largest)
    {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
void heapSort(int arr[], int n)
{
    // build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // One by one extract an element from heap
    for (int i = n - 1; i >= 0; i--)
    {
        // Move current root to end
        std::swap(arr[0], arr[i]);

        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}

/* A utility function to print array of size n */
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; ++i)
        std::cout << arr[i] << " ";
    std::cout << "\n";
}

// Driver program
int main()
{
    int arr[] = {60, 20, 40, 70, 30, 10};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Heapify algorithm
    // The loop must go reverse, as you will get after analyzing manually
    // (i=n/2 -1) because other nodes/elements are leaf nodes
    // (i=n/2 -1) for 0-based indexing
    // (i=n/2)  for 1-based indexing
    for (int i = n / 2 - 1; i >= 0; i--)
    {
        heapify(arr, n, i);
    }

    std::cout << "After heapifying array is \n";
    printArray(arr, n);

    heapSort(arr, n);

    std::cout << "Sorted array is \n";
    printArray(arr, n);

    return 0;
}