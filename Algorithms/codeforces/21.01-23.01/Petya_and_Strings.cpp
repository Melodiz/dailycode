#include <iostream>
#include "string"
using namespace std;

int main()
{
    string st1, st2;

    cin >> st1 >> st2;

    for (short i = 0; i < st1.size(); i++)
    {
        char a = tolower(st1[i]);
        char b = tolower(st2[i]);
        if (a < b)
        {
            cout << -1 << endl;
            return 0;
        }
        else if (a > b)
        {
            cout << 1 << endl;
            return 0;
        }
    }
    cout << 0 << endl;
    return 0;
}
