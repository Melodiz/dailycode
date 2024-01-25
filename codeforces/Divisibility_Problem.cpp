// #include <cmath>
#include <string>
#include <iostream>
#include <set>
using namespace std;

int main()
{
    short n;
    cin >> n;
    long a, b;
    long ans;

    for (size_t i = 0; i < n; i++)
    {
        cin >> a >> b;
        ans = a % b;
        if (ans == 0)
        {
            cout << 0 << endl;
        }
        else{
            cout << b - ans << endl;
        }
    }
    

    return 0;
}