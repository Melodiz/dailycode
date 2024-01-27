// #include <cmath>
#include <iostream>
using namespace std;

int main()
{
    double n;
    cin >> n;
    double amount;
    double ans = 0;

    for (size_t i = 0; i < n; i++)
    {   
        cin >> amount;
        ans += amount/n;
    }
    cout << ans << endl;
    return 0;

}