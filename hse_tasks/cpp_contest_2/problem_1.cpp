#include "iostream"
#include <string>
using namespace std;

bool check_lengh(string data);
bool check_symbols(string data);
bool check_groups(string data);

int main()
{
    string input;
    getline(std::cin, input);

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
    if (data.length() > 7 && data.length() < 15)
    {
        //std::cout << "length checked" << std::endl;
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
    //std::cout << "Symbols checked" << std::endl;
    return true;
}

bool check_groups(string data)
{
    int a = 0, b = 0, c = 0, d = 0;
    for (size_t i = 0; i < data.length(); i++)
    {
        if (int(data[i]) > 64 && int(data[i]) < 91)
        {
            a = 1;
        }
        else if (int(data[i]) > 96 && int(data[i]) < 123)
        {
            b = 1;
        }
        else if (int(data[i]) > 47 && int(data[i] < 58))
        {
            c = 1;
        }
        else
        {
            d = 1;
        }
    }
    if ((a + b + c + d) > 2)
    {
        //std::cout << "Uniquness check" << std::endl;
        return true;
    }
    return false;
}