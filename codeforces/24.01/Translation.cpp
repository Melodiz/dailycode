#include "iostream"
#include <string>
using namespace std;

int main()
{
    string str1;
    string str2;

    cin >> str1;
    cin >> str2;
    size_t n = str1.size();

    if (str2.size() != n)
    {
        cout << "NO" << endl;
        return 0;
    }

    for (size_t i = 0; i < n; i++)
    {
        if (str1[i] != str2[n - 1 - i])
        {
            cout << "NO" << endl;
            return 0;
        }
    }

    cout << "YES" << endl;
    return 0;
}