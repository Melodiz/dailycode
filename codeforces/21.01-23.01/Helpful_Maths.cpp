#include <string>
#include <sstream>
#include "iostream"
using namespace std;

int main()
{
    string str;
    getline(cin, str);

    stringstream input(str);

    string segment;
    short a, b, c = 0;

    while (getline(input, segment, '+'))
    {
        // short num = stoi(segment);
        // cout << num << endl;
        switch (stoi(segment))
        {
        case 3:
            c++;
            break;
        case 2:
            b++;
            break;
        case 1:
            a++;
            break;
        default:
            break;
        }
    }
    string ans;

    while (a > 0)
    {
        ans += "1+";
        a--;
    }
    while (b > 0)
    {
        ans += "2+";
        b--;
    }
    while (c > 0)
    {
        ans += "3+";
        c--;
    }
    ans.pop_back();
    cout << ans << endl;
    
}