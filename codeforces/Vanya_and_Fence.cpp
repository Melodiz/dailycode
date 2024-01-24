#include "iostream"
// #include <string>
using namespace std;

int main()
{
    size_t n = 0;
    size_t h = 0;
    cin >> n >> h;

    // int data[n];
    size_t ans = 0;
    size_t cur = 0;

    for (size_t i = 0; i < n; i++)
    {
        cin >> cur;
        if (cur > h)
        {
            ans += 2;
        }
        else
        {
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
    
}