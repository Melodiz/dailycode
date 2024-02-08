#include "iostream"
#include <string>
#include <algorithm>
#include <set>
using namespace std;

string build(string data);
string removeDumnLetters(string data);
string replaceLetters(string data);
string removeDigits(string data);
string changeLenght(string data);

string removeDumnLetters(string data)
{
    string res = "";
    set<char> letters;
    letters.insert('a');
    letters.insert('y');
    letters.insert('e');
    letters.insert('h');
    letters.insert('i');
    letters.insert('o');
    letters.insert('u');
    letters.insert('w');

    // hate it, cau'se i can not make a set with values
    // like that: set<char> letters {'a', 'e', 'h', 'i', 'o', 'u', 'w', 'y'};

    for (size_t i = 0; i < data.length(); i++)
    {
        // bool found = (find(letters.begin(), letters.end(), data[i]) != letters.end());
        if (!(letters.find(data[i]) != letters.end()))
        {
            res += data[i];
        }
    }
    return res;
}

string replaceLetters(string data)
{
    for (size_t i = 0; i < data.length(); i++)
    {
        switch (data[i])
        {
        case 'b':
        case 'f':
        case 'p':
        case 'v':
            data[i] = '1';
            break;
        case 'c':
        case 'g':
        case 'j':
        case 'k':
        case 'q':
        case 's':
        case 'x':
        case 'z':
            data[i] = '2';
            break;
        case 'd':
        case 't':
            data[i] = '3';
            break;
        case 'l':
            data[i] = '4';
            break;
        case 'm':
        case 'n':
            data[i] = '5';
            break;
        case 'r':
            data[i] = '6';
            break;
        default:
            break;
        }
    }
    return data;
}

string removeDigits(string data)
{
    for (int i = 0; i < data.length(); i++)
    {
        if (isdigit(data[i]))
        {
            if (data[i] == data[i + 1])
            {
                data.erase(i, 1);
                i--;
            }
        }
    }
    return data;
}

string changeLenght(string data)
{

    if (data.length() > 3)
    {
        data.erase(data.begin() + 3, data.end());
    }
    else
    {
        while (data.length() < 3)
        {
            data.append("0");
        }
    }
    return data;
}

string build(string data)
{
    char firstLetter = data[0];
    data.erase(0, 1);
    data = removeDumnLetters(data);
    data = replaceLetters(data);
    data = removeDigits(data);
    data = changeLenght(data);

    return firstLetter + data;
}

int main()
{
    string word;
    cin >> word;

    cout << build(word) << endl;

    return 0;
}
