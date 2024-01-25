// #include <cmath>
#include <string>
#include <iostream>
#include <set>
using namespace std;

int main()
{
    long a, b, c, d;
    cin >> a >> b >> c >> d;

    set<long> ans;
    ans.insert(a);
    ans.insert(b);
    ans.insert(c);
    ans.insert(d);

    cout << 4 - ans.size() << endl;
    return 0;
}