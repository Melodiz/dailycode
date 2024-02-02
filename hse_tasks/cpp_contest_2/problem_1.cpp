#include "iostream"
#include <string>
using namespace std;

bool check_lengh(string data);
bool check_symbols(string data);
bool check_groups(string data);

int main()
{
    string input;
    cin >> input;

    if (check_lengh(input) && check_symbols(input) && check_groups(input))
    {
        cout << "YES" << endl;
        return 0;
    }
    cout << "NO" << endl;
    return 0;
}

bool check_lengh(string data)
{
    if (data.length() < 15 && data.length() > 7)
    {
        return true;
    }
    return false;
}

bool check_symbols(string data)
{
    for (size_t i = 0; i < data.length(); i++)
    {
        if (!(int(data[i]) > 32 && int(data[i]) < 128))
        {
            return false;
        }
    }
    return true;
}

bool check_groups(string data)
{
    bool a, b, c, d = false;
    for (size_t i = 0; i < data.length(); i++)
    {
        if (data[i] <= 0x5A && data[i] >= 0x41)
        {
            a = true;
        }
        else if (data[i] <= 0x39 && data[i] >= 0x30)
        {
            b = true;
        }
        else if (data[i] <= 0x7A && data[i] >= 0x61)
        {
            c = true;
        }
        else
        {
            d = true;
        }
    }
    if (a + b + c + d >= 3)
    {
        return true;
    }
    return false;
}