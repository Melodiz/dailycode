///////////////////////////////////////////////////////////////////////////////
/// \file
/// \brief      Main module for Problem: Execute Callback
/// \version    0.1.0
/// \date       30.01.2024
///
/// TASK DESCRIPTION
///
/// Write a function `void executeCallback(void (*callback)())` that takes a
/// function pointer and executes the callback function.
///
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
using namespace std;

void executeCallback(void (*callback)());
void Callback(int number);

int main()
{
    int a = 3;
    a = executeCallback(Callback(a));

    cout << a << endl;
    return 0;
}

void executeCallback(void (*callback)())
{
    Callback();
}

void Callback(int number)
{
    number *= number;
}