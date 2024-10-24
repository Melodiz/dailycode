#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
    int key;
    int left;
    int right;
};

void inOrderTraversal(const vector<TreeNode>& tree, int root, vector<int>& result) {
    if (root == -1) return;
    inOrderTraversal(tree, tree[root].left, result);
    result.push_back(tree[root].key);
    inOrderTraversal(tree, tree[root].right, result);
}

void preOrderTraversal(const vector<TreeNode>& tree, int root, vector<int>& result) {
    if (root == -1) return;
    result.push_back(tree[root].key);
    preOrderTraversal(tree, tree[root].left, result);
    preOrderTraversal(tree, tree[root].right, result);
}

void postOrderTraversal(const vector<TreeNode>& tree, int root, vector<int>& result) {
    if (root == -1) return;
    postOrderTraversal(tree, tree[root].left, result);
    postOrderTraversal(tree, tree[root].right, result);
    result.push_back(tree[root].key);
}

int main() {
    int n;
    cin >> n;
    vector<TreeNode> tree(n);

    for (int i = 0; i < n; ++i) {
        cin >> tree[i].key >> tree[i].left >> tree[i].right;
    }

    vector<int> inOrderResult, preOrderResult, postOrderResult;

    inOrderTraversal(tree, 0, inOrderResult);
    preOrderTraversal(tree, 0, preOrderResult);
    postOrderTraversal(tree, 0, postOrderResult);

    for (int key : inOrderResult) {
        cout << key << " ";
    }
    cout << endl;

    for (int key : preOrderResult) {
        cout << key << " ";
    }
    cout << endl;

    for (int key : postOrderResult) {
        cout << key << " ";
    }
    cout << endl;

    return 0;
}