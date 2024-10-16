#include <iostream>
#include <random>

unsigned long long getMax(const unsigned long long arr[], int n)
{
    unsigned long long mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}

// A function to do counting sort of arr[] according to the digit represented by exp.
void countSort(unsigned long long arr[], int n, unsigned long long exp)
{
    unsigned long long* output = new unsigned long long[n];
    unsigned long long count[256] = {0};

    // Store count of occurrences in count[]
    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 256]++;

    // Change count[i] so that count[i] now contains actual position of this digit in output[]
    for (int i = 1; i < 256; i++)
        count[i] += count[i - 1];

    // Build the output array
    for (int i = n - 1; i >= 0; i--)
    {
        output[count[(arr[i] / exp) % 256] - 1] = arr[i];
        count[(arr[i] / exp) % 256]--;
    }

    // Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    for (int i = 0; i < n; i++)
        arr[i] = output[i];

    delete[] output;
}

void radixsort(unsigned long long arr[], int n)
{
    unsigned long long m = getMax(arr, n);

    // Do counting sort for every byte.
    // exp is 256^i where i is current byte number
    for (unsigned long long exp = 1; m / exp > 0; exp *= 256)
        countSort(arr, n, exp);

    unsigned long long sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += arr[i] * (i + 1);
    }
    std::cout << sum << std::endl;
}

unsigned int cur = 0; // unsigned 64-bit number
unsigned long long a, b;

unsigned long long nextRand24()
{
    cur = cur * a + b; // calculated with overflow
    return cur >> 8;   // number from 0 to 2^24 - 1
}

unsigned long long nextRand32()
{
    unsigned long long x = nextRand24(), y = nextRand24();
    return (x << 8) ^ y; // number from 0 to 2^32 - 1
}

int main()
{
    int t, n;
    std::cin >> t >> n;
    std::cin >> a >> b; // Use global a and b
    while (t--)
    {
        unsigned long long* arr = new unsigned long long[n];
        for (int i = 0; i < n; i++)
            arr[i] = nextRand32();
        radixsort(arr, n);
        delete[] arr;
    }
    return 0;
}