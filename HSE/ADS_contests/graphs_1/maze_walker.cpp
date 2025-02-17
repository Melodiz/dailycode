#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const int MAX_N = 1001;

vector<pair<int, int>> graph[MAX_N];
vector<int> program;
set<int> possible_rooms;
bool hangs = false;

void dfs(int room, int step) {
    if (step == program.size()) {
        possible_rooms.insert(room);
        return;
    }

    bool found = false;
    for (auto& [next_room, color] : graph[room]) {
        if (color == program[step]) {
            found = true;
            dfs(next_room, step + 1);
        }
    }

    if (!found) hangs = true;
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    for (int i = 0; i < m; i++) {
        int u, v, c;
        cin >> u >> v >> c;
        graph[u].push_back({v, c});
    }

    int l;
    cin >> l;
    program.resize(l);
    for (int i = 0; i < l; i++) {
        cin >> program[i];
    }

    int s;
    cin >> s;

    dfs(s, 0);

    if (hangs) {
        cout << "Hangs" << endl;
    } else {
        cout << "OK" << endl;
        cout << possible_rooms.size() << endl;
        for (int room : possible_rooms) {
            cout << room << " ";
        }
        cout << endl;
    }

    return 0;
}