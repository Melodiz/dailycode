#include <iostream>
using namespace std;

int main()
{
    short n;
    cin >> n;
    
    short ans = 0;

    string s;
    while (n--)
    {
        cin >> s;
        if (s[1] == '+')
        {
            ans++;
        }
        else
        {
            ans--;
        }
    }

    cout << ans << endl;

    return 0;
}
