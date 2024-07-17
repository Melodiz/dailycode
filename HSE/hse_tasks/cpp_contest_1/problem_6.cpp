#include <iostream>
using namespace std;

int main()
{
    short n;
    short MOD;

    cin >> n >> MOD;
    for (short i = 1; i <= n; i++)
    {
        cout << "\t" << i;
    }
    cout << endl;

    for (short i = 1; i <= n; i++)
    {
        cout << i << "\t";
        for (short j = 1; j <= n; j++)
        {
            cout << i * j % MOD << "\t";
        }
        cout << endl;
    }
    return 0;
}