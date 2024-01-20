#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    for (size_t i = 0; i <= 15; i++)
    {
        cout << "\t" << hex << uppercase << i;
    }
    cout << endl;

    for (short n = 2; n < 8; n++)
    {
        cout << n;

        for (short i = 0; i < 16; i++)
        {
            cout << "\t" << char(n*16 + i);
        }
        cout << endl;
        
    }
    

    return 0;
}
