// #include <cmath>
#include <string>
#include <iostream>
#include <set>
using namespace std;

int main()
{
    short n;
    cin >> n;
    for (size_t i = 0; i < (n - 1) / 2; i++)
    {
        cout << "I hate that I love that ";
    }

    if (n % 2 == 0)
    {
        cout << "I hate that I love it" << endl;
    }
    else
    {
        cout << "I hate it" << endl;
    }

    return 0;
}