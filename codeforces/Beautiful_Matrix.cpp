#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    short a, b;
    short num;

    for (short i = 0; i < 5; i++)
    {
        for (short j = 0; j < 5; j++)
        {
            cin >> num;
            if (num == 1)
            {
                a = i + 1;
                b = j + 1;
            }
        }
    }
    
    cout << abs(3-a)+abs(3-b) << endl;

    return 0;
}