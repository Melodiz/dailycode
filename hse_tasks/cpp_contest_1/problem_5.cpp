#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    short n;
    short k;
    short m;
    short dif;
    short res = 0;

    cin >> n >> k >> m;
    if (m > k)
    {
        cout << 0 << endl;
        return 0;
    }

    while (n >= k)
    {
        dif = (n / k) * (k / m);
        res += dif;
        n -= dif * m;
    }
    cout << res << endl;
    return 0;
}