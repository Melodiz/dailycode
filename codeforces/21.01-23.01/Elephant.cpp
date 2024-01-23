#include <iostream>
#include <string>
#include <set>
using namespace std;

int main()
{
    int a;
    cin >> a;
    if (a%5 == 0)
    {
        cout << a/5 << endl;
        return 0;
    }
    
    cout << a/5 + 1 << endl;

    return 0;
}