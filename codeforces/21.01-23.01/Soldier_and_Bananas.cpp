#include <iostream>
#include <string>
#include <set>
using namespace std;
 
int main()
{
    int a, budget, n;
    cin >> a >> budget >> n;
 
    int amount = 0;
    for (size_t i = 0; i < n; i++)
    {
        amount += a * (i + 1);
    }
 
    cout << max(amount - budget, 0) << endl;
 
    return 0;
}