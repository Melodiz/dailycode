#include <iostream>
#include <string>
#include <set>
using namespace std;

int main()
{
    string str;
    cin >> str;
    set<char> a;

    for (size_t i = 0; i < str.size(); i++)
    {
        a.insert(str[i]);
    }
    
    cout << a.size() << endl;
    return 0;
}