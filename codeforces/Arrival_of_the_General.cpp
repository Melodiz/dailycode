#include "iostream"
using namespace std;

int main()
{
    short n;
    short a = 0;
    short b = 200;
    cin >> n;

    short ans;
    short data[n];

    for (size_t i = 0; i < n; i++)
    {
        cin >> data[i];
    }

    for (size_t i = 0; i < n; i++)
    {
        a = max(a, data[i]);
        b = min(b, data[i]);
    }

    for (size_t i = 0; i < n; i++)
    {
        if (data[i] == a)
        {
            a = i;
        }
        else if (data[i] == b)
        {
            b = i + 1;
        }
    }
    cout << a << '-' << b << endl;
    cout << a + n - b << endl;
    return 0;
}