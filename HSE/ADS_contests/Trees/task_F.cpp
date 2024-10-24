#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

struct Node {
    long long a;
    long long b;
    int index;
};

bool buildCartesianTree(int N, vector<Node> &nodes, vector<int> &parent, vector<int> &left_child, vector<int> &right_child) {
    sort(nodes.begin(), nodes.end(), [&](const Node &x, const Node &y) -> bool {
        return x.a < y.a;
    });
    
    stack<Node*> s;
    for(auto &node : nodes){
        int last_popped = 0;
        while(!s.empty() && s.top()->b >= node.b){
            last_popped = s.top()->index;
            s.pop();
        }
        if(last_popped != 0){
            parent[last_popped] = node.index;
            left_child[node.index] = last_popped;
        }
        if(!s.empty()){
            parent[node.index] = s.top()->index;
            right_child[s.top()->index] = node.index;
        }
        s.push(&node);
    }
    
    int roots = 0;
    for(int i=1;i<=N;i++) {
        if(parent[i] == 0) roots++;
    }
    return roots == 1;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;
    vector<Node> nodes(N);
    for(int i=0;i<N;i++){
        cin >> nodes[i].a >> nodes[i].b;
        nodes[i].index = i+1; // 1-based indexing
    }

    vector<int> parent(N+1, 0);
    vector<int> left_child(N+1, 0);
    vector<int> right_child(N+1, 0);
    
    bool possible = buildCartesianTree(N, nodes, parent, left_child, right_child);
    
    if(possible){
        cout << "YES\n";
        vector<Node> original_order(N+1);
        for(auto &node : nodes){
            original_order[node.index] = node;
        }
        for(int i=1;i<=N;i++){
            cout << parent[i] << " " << left_child[i] << " " << right_child[i] << "\n";
        }
    }
    else{
        cout << "NO\n";
    }
    
    return 0;
}