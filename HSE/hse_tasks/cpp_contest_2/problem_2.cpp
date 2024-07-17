#include "iostream"
#include <string>
#include <algorithm>
using namespace std;

string remove_spaces(string data);
bool check_palindrome(string data);
bool check(string data);

string remove_spaces(string data)
{
    data.erase(remove(data.begin(), data.end(), ' '), data.end());
    return data;
}

bool check_palindrome(string data)
{
    string rev_data = data;
    reverse(rev_data.begin(), rev_data.end());
    if (data == rev_data)
    {
        return true;
    }
    return false;
}

bool check(string data)
{
    data = remove_spaces(data);
    if (check_palindrome(data))
    {
        return true;
    }
    return false;
    
}

int main()
{
    string data;

    getline(cin, data);
    if (check(data))
    {
        cout << "yes" << endl;
        return 0;
    }
    cout << "no" << endl;
    
    return 0;
}