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
    
    if (a.size() % 2 ==0)
    {
        cout << "CHAT WITH HER!" << endl;
        return 0;
    }
    
    cout << "IGNORE HIM!" << endl;
    return 0;
}