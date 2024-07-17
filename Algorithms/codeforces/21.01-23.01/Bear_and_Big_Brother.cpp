#include <iostream>
#include <string>
#include <set>
using namespace std;

int main()
{
    size_t a,b;
    cin >> a >> b;

    size_t counter = 0;
    while (a<=b)
    {
       a*=3;
       b*=2;
       counter ++;
    }
    
    cout << counter << endl;
    return 0;

}