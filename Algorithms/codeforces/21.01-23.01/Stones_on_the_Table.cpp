#include <iostream>
#include <string>
#include <set>
using namespace std;

int main()
{
    size_t n;
    cin >> n;
    size_t ans = 0;

    string str;
    cin >> str;

    for (size_t i = 0; i < n-1; i++)
    {
        if (str[i] == str[i+1])
        {
            ans++;
        }
        
    }
    
    cout << ans << endl;
    return 0;

}