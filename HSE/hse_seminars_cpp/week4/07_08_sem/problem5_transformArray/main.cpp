///////////////////////////////////////////////////////////////////////////////
/// \file
/// \brief      Main module for Problem: Array Transformation
/// \version    0.1.0
/// \date       30.01.2024
///
/// TASK DESCRIPTION
///
/// Write a function `void transformArray(int* arr, int size, int (*transform)(int))`
/// that applies a transformation function to each element of an array.
///
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
using namespace std;

int transform(int data);
void transformArray(int *arr, int size, int (*transform)(int));

int main()
{
    int data[] = {2, 4, 6, 8, 10};

    transformArray(data, sizeof(data) / sizeof(data[0]), transform);

    for (int i = 0; i < sizeof(data) / sizeof(data[0]); i++)
    {
        cout << data[i] << " ";
    }
    cout << endl;

    return 0;
}

int transform(int data)
{
    // for example
    return data * 2;
}
void transformArray(int *arr, int size, int (*transform)(int))
{
    for (size_t i = 0; i < size; i++)
    {
        arr[i] = transform(arr[i]);
    }
    
}
