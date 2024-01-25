#include "iostream"
// #include <string>
using namespace std;

int main()
{
    size_t n = 0;
    cin >> n;

    size_t ans = 0;

    for (size_t i = 0; i < n; i++)
    {
        short a = 0;
        short b = 0;
        cin >> a >> b;

        if (b - a >= 2)
        {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}