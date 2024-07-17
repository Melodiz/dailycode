#include <iostream>
#include <string>
#include <set>
#include <string>
using namespace std;

int main()
{
    string data;
    cin >> data;

    short u = 0;
    short l = 0;

    for (size_t i = 0; i < data.size(); i++)
    {
        if (toupper(data[i]) == data[i])
        {
            u++;
        }
        else
        {
            l++;
        }
    }

    if (u > l)
    {
        for (size_t i = 0; i < data.size(); i++)
        {
            cout << char(toupper(data[i]));
        }
        cout << endl;
        return 0;
    }

    for (size_t i = 0; i < data.size(); i++)
    {
        cout << char(tolower(data[i]));
    }
    cout << endl;
    return 0;
}
