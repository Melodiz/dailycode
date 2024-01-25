#include "iostream"
// #include <string>
using namespace std;

int main()
{
    size_t n = 0;
    cin >> n;

    short pred = 0;
    cin >> pred;

    size_t ans = 0;
    for (size_t i = 0; i < n - 1; i++)
    {
        short cur = 0;
        cin >> cur;

        if (cur != pred)
        {
            ans++;
        }
        pred = cur;
    }
    cout << ans + 1 << endl;
    return 0;
}