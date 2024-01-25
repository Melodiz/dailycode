// #include <cmath>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    string a;
    string b;

    cin >> a;
    cin >> b;

    short ans[a.size()];

    for (size_t i = 0; i < a.size(); i++)
    {
        ans[i] = a[i]^b[i];
    }

    for (size_t i = 0; i < a.size(); i++)
    {
        cout << ans[i];
    }
    cout << endl;
    return 0;
    
}