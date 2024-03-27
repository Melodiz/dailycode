///////////////////////////////////////////////////////////////////////////////
/// \file
/// \brief      Main module for Problem: Print Data
/// \version    0.1.0
/// \date       30.01.2024
///
/// TASK DESCRIPTION
///
/// Write overloaded functions `void print(int)` and `void print(double)` that
/// print an integer and a double, respectively.
///
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
using namespace std;


void printInt(int number);
void printDouble(double number);

int main()
{
    int a = -124;
    double b = 134.312;

    printInt(a);
    printDouble(b);

    return 0;
}

void printInt(int number)
{
    cout << number << endl;
}

void printDouble(double number){
    cout << number << endl;
}
