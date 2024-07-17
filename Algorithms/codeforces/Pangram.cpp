#include "iostream"
#include "string"
#include "set"
using namespace std;

int main()
{
    int a;
    cin >> a;
    string word = "";
    cin >> word;

    if (a < 26)
    {
        cout << "NO" << endl;
        return 0;
    }

    set<char> data;

    for (size_t i = 0; i < word.length(); i++)
    {
        data.insert(tolower(word[i]));
    }

    if (data.size() == 26)
    {
        cout << "YES" << endl;
        return 0;
    }

    cout << "NO" << endl;
    return 0;
}