///////////////////////////////////////////////////////////////////////////////
/// \file
/// \brief      Main module for Problem: Increment Value
/// \version    0.1.0
/// \date       30.01.2024
///
/// TASK DESCRIPTION
///
/// Write a function `void increment(int &value)`
/// that increments the value of
/// the passed integer by 1.
///
///////////////////////////////////////////////////////////////////////////////

#include "iostream"
#include <string>

void increment(int &value);

int main()
{
    int data;
    std::cin >> data;
    increment(data);
    std::cout << data << std::endl;
    return 0;
}

void increment(int &value)
{
    value += 1;
}
