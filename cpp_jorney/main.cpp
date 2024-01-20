#include <iostream>
#include <iomanip>
using namespace std;
// 2:50
int main()
{
    short n;
    short m;

    cin >> n;
    cin >> m;

    for (short i = 1; i < n + 1; i++)
    {
        cout << "" << i;
    }
    cout << endl;

    for (short i = 1; i < n + 1; i++)
    {
        for (short j = 0; j < n + 1; j++)
        {
            if (j == 0)
            {
                cout << i;
            }
            else
            {
                cout << setw(5) << (i * j) % m;
            }
        }
        cout << endl;
    }
}
