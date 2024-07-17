#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore();

    int ans = 0;

    for (int i = 0; i < n; i++)
    {
        short a,b,c;
        cin >> a >> b >> c;
        if (a+b+c>=2)
        {
            ans +=1;
        }
    }
    cout << ans << endl;

    return 0;
}
