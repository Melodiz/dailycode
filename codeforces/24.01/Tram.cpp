#include "iostream"
// #include <string>
using namespace std;

int main()
{
    int n = 0;
    cin >> n;

    int cur = 0;
    int ans = 0;
    short a = 0;
    short b = 0;

    for (size_t i = 0; i < n; i++)
    {
        cin >> a >> b;
        cur -= a;
        cur += b;
        ans = max(ans, cur);
    }

    cout << ans << endl;
    return 0;
}