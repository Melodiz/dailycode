#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

void processTree(const string& traversal) {
    stack<string> pathStack;
    vector<string> leafCodes;
    string currentPath = "";

    for (char c : traversal) {
        if (c == 'D') {
            currentPath += '0';
            pathStack.push(currentPath);
        } else if (c == 'U') {
            while (!currentPath.empty() && currentPath.back() == '1') {
                currentPath.pop_back();
            }
            if (!currentPath.empty()) {
                currentPath.back() = '1';
            }
        }
    }

    while (!pathStack.empty()) {
        leafCodes.push_back(pathStack.top());
        pathStack.pop();
    }

    cout << leafCodes.size() << endl;
    for (const string& code : leafCodes) {
        cout << code << endl;
    }
}

int main() {
    int N;
    cin >> N;
    vector<string> traversals(N);

    for (int i = 0; i < N; ++i) {
        cin >> traversals[i];
    }

    for (const string& traversal : traversals) {
        processTree(traversal);
    }

    return 0;
}