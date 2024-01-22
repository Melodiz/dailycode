#include <iostream>
using namespace std;

int main()
{
    short n, k, amount;
    cin >> n >> k;

    for (short i = 0; i < k; i++)
    {
        cin >> amount;
        if (amount <= 0)
        {
            cout << 0 << endl;
            return 0;
        }
    }
    short ans = k;
    short plank = amount;

    for (short i = k; i < n; i++)
    {
        cin >> amount;
        if (amount == plank)
        {
            ans++;
        }
        else
        {
            break;
        }
    }
    cout << ans << endl;

    return 0;
}
