#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <tuple>
using namespace std;

void fileStatistic(const string fileName, int &lines, int &words, int &letters);

void fileStatistic(const string fileName, int &lines, int &words, int &letters)
{
    ifstream in(fileName);
    char ch;
    bool flag = false;
    while (in >> std::noskipws >> ch)
    {
        // cout << int(ch) << endl;
        if ((int(ch) > 0x40 && int(ch) < 0x5B) ||
            (int(ch) > 0x60 && int(ch) < 0x7B))
        {
            ++letters;
            flag = true;
        }
        else
        {
            if (flag)
            {
                ++words;
                flag = false;
            }
        }

        if (ch == '\n')
        {
            ++lines;
            // flag = false;
        }
    }
    in.close();
}

int main()
{
    using namespace std;
    int letters = 0, words = 0, lines = 0;
    fileStatistic("input.txt", lines, words, letters);

    cout << "Input file contains: " << endl;
    cout << letters << " letters" << endl;
    cout << words << " words" << endl;
    cout << lines << " lines" << endl;
    return 0;
}