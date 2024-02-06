#include "iostream"
#include <string>
#include <algorithm>
#include <set>
using namespace std;

bool check(string data);
string removeDumnLetters(string data);

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
        if(!(letters.find(data[i]) != letters.end()))
        {
            res += data[i];
        }
    }
    return res;
}

bool check(string data)
{
    char firstLetter = data[0];
    return false;
}

int main()
{
    string word;
    cin >> word;
    cout << removeDumnLetters(word) << endl;

    return 0;
}
