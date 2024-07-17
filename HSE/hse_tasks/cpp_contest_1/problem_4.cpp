#include <iostream>

int main()
{
    using namespace std;
    double ans = 0;
    size_t n;
    short sign = 1;

    cin >> n;
    for (size_t i = 1; i < n+1; i++)
    {
        ans += (1./i)*sign;
        sign *= -1;
    }
    
    cout << ans << endl;
    return 0;
}