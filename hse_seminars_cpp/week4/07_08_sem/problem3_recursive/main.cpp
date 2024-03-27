///////////////////////////////////////////////////////////////////////////////
/// \file
/// \brief      Main module for a Problem: Sum digits
/// \version    0.1.0
/// \date       22.01.2022
///
/// TASK DESCRIPTION
///
/// Write a program that takes a number and
/// find sum of digits recursively.
///
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include "string"
using namespace std;

int SumOfDigitsRecursiv(int number);

int main()
{
    int number;
    cin >> number;

    cout << SumOfDigitsRecursiv(number) << endl;

    return 0;
}


int SumOfDigitsRecursiv(int number)
{
    if (number < 10)
    {
        return number%10;
    }
    return SumOfDigitsRecursiv(number/10) + number%10;
}
