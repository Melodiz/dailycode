#include <iostream>
using namespace std;

int main()
{
    double ans = 0;
    int n;
    short sign = 1;

    cin >> n;
    for (float i = 1; i < n+1; i++)
    {
        ans += (1/i)*sign;
        sign *= -1;
    }
    
    cout << ans << endl;
    return 0;
}