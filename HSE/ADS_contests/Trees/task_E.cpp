#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <cstdint> 
using namespace std;

struct TreapNode {
    int key;
    int priority; 
    int size; 
    TreapNode* left;
    TreapNode* right;

    TreapNode(int _key) : key(_key), priority(rand()), size(1), left(nullptr), right(nullptr) {}
};

void update_size(TreapNode* node) {
    if (node) {
        node->size = 1;
        if (node->left) node->size += node->left->size;
        if (node->right) node->size += node->right->size;
    }
}

pair<TreapNode*, TreapNode*> split(TreapNode* root, int key) {
    if (!root) return {nullptr, nullptr};
    if (key <= root->key) {
        auto left_split = split(root->left, key);
        root->left = left_split.second;
        update_size(root);
        return {left_split.first, root};
    }
    else {
        auto right_split = split(root->right, key);
        root->right = right_split.first;
        update_size(root);
        return {root, right_split.second};
    }
}

TreapNode* merge(TreapNode* left, TreapNode* right) {
    if (!left || !right) return left ? left : right;
    if (left->priority > right->priority) {
        left->right = merge(left->right, right);
        update_size(left);
        return left;
    }
    else {
        right->left = merge(left, right->left);
        update_size(right);
        return right;
    }
}

TreapNode* insert(TreapNode* root, TreapNode* node) {
    if (!root) return node;
    if (node->key == root->key) return root; 
    if (node->priority > root->priority) {
        auto splitted = split(root, node->key);
        node->left = splitted.first;
        node->right = splitted.second;
        update_size(node);
        return node;
    }
    if (node->key < root->key)
        root->left = insert(root->left, node);
    else
        root->right = insert(root->right, node);
    update_size(root);
    return root;
}

TreapNode* erase(TreapNode* root, int key) {
    if (!root) return root;
    if (root->key == key) {
        TreapNode* merged = merge(root->left, root->right);
        delete root;
        return merged;
    }
    if (key < root->key)
        root->left = erase(root->left, key);
    else
        root->right = erase(root->right, key);
    update_size(root);
    return root;
}

bool exists(TreapNode* root, int key) {
    while (root) {
        if (root->key == key) return true;
        if (key < root->key)
            root = root->left;
        else
            root = root->right;
    }
    return false;
}

string next_elem(TreapNode* root, int key) {
    TreapNode* current = root;
    int succ = INT32_MAX;
    bool found = false;
    while (current) {
        if (current->key > key) {
            if (current->key < succ) {
                succ = current->key;
                found = true;
            }
            current = current->left;
        }
        else {
            current = current->right;
        }
    }
    if (found)
        return to_string(succ);
    else
        return "none";
}

string prev_elem(TreapNode* root, int key) {
    TreapNode* current = root;
    int pred = INT32_MIN;
    bool found = false;
    while (current) {
        if (current->key < key) {
            if (current->key > pred) {
                pred = current->key;
                found = true;
            }
            current = current->right;
        }
        else {
            current = current->left;
        }
    }
    if (found)
        return to_string(pred);
    else
        return "none";
}

string kth_element(TreapNode* root, int k) {
    if (!root || k <= 0 || k > root->size)
        return "none";
    int current_rank = root->left ? root->left->size : 0;
    if (k == current_rank + 1)
        return to_string(root->key);
    else if (k <= current_rank)
        return kth_element(root->left, k);
    else
        return kth_element(root->right, k - current_rank - 1);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    srand(time(0));

    TreapNode* root = nullptr;
    string operation;
    int x;

    while(cin >> operation >> x){
        if(operation == "insert"){
            if(!exists(root, x)){
                TreapNode* node = new TreapNode(x);
                root = insert(root, node);
            }
        }
        else if(operation == "delete"){
            if(exists(root, x)){
                root = erase(root, x);
            }
        }
        else if(operation == "exists"){
            cout << (exists(root, x) ? "true" : "false") << "\n";
        }
        else if(operation == "next"){
            cout << next_elem(root, x) << "\n";
        }
        else if(operation == "prev"){
            cout << prev_elem(root, x) << "\n";
        }
        else if(operation == "kth"){
            cout << kth_element(root, x) << "\n";
        }
    }

    return 0;
}