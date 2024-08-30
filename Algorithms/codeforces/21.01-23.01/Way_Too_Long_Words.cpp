#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore();

    vector<string> words;

    for (int i = 0; i < n; i++)
    {
        string a;
        getline(cin, a);
        words.push_back(a);
    }

    for (int i = 0; i < n; i++)
    {
        string word = words[i];
        if (word.size() > 10)
        {
            cout << word.front() << word.size() - 2 << word.back() << endl;
        }
        else
        {
            cout << word << endl;
        }
    }

    return 0;
}
