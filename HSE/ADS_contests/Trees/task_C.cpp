#include <iostream>
#include <vector>
#include <limits>

using namespace std;
struct Node {
    int key;
    int left;
    int right;
};

bool isBSTUtil(const vector<Node>& tree, int nodeIndex, long long minKey, long long maxKey) {
    if (nodeIndex == -1) {
        return true;
    }

    const Node& node = tree[nodeIndex];

    if (node.key < minKey || node.key > maxKey) {
        return false;
    }

    return isBSTUtil(tree, node.left, minKey, node.key - 1LL) &&
           isBSTUtil(tree, node.right, node.key, maxKey);
}

bool isBST(const vector<Node>& tree) {
    if (tree.empty()) {
        return true;
    }
    return isBSTUtil(tree, 0, numeric_limits<long long>::min(), numeric_limits<long long>::max());
}

int main() {
    int n;
    cin >> n;

    vector<Node> tree(n);
    for (int i = 0; i < n; ++i) {
        cin >> tree[i].key >> tree[i].left >> tree[i].right;
    }

    if (isBST(tree)) {
        cout << "CORRECT" << endl;
    } else {
        cout << "INCORRECT" << endl;
    }

    return 0;
}