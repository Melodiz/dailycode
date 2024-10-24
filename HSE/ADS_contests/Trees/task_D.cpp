#include <iostream>
#include <string>
#include <algorithm> // Include this for std::max

using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
    int height;
};

int height(Node* node) {
    if (node == nullptr) {
        return 0;
    }
    return node->height;
}

int getBalanceFactor(Node* node) {
    if (node == nullptr) {
        return 0;
    }
    return height(node->left) - height(node->right);
}

Node* leftRotate(Node* node)
{
    Node* right_child = node->right;
    Node* left_child_of_right_child = right_child->left;

    right_child->left = node;
    node->right = left_child_of_right_child;

    // update heights
    node->height = std::max(height(node->left), height(node->right)) + 1;
    right_child->height = std::max(height(right_child->left), height(right_child->right)) + 1;

    return right_child;
}

Node* rightRotate(Node* node)
{
    Node* left_child = node->left;
    Node* right_child_of_left_child = left_child->right;

    left_child->right = node;
    node->left = right_child_of_left_child;

    // update heights
    node->height = std::max(height(node->left), height(node->right)) + 1;
    left_child->height = std::max(height(left_child->left), height(left_child->right)) + 1;

    return left_child;
}

Node* createNode(int key) // default node creation function
{
    Node* node = new Node();
    node->key = key;
    node->left = nullptr;
    node->right = nullptr;
    node->height = 1;
    return node;
}

Node* insert(Node* node, int key)
{  
    if (node == nullptr) { // create a new node if terminal
        return createNode(key);
    }
    // if key is less than node's key, insert in left subtree
    if (key < node->key) {
        node->left = insert(node->left, key);
    }
    // if key is greater than node's key, insert in right subtree
    else if (key > node->key) {
        node->right = insert(node->right, key);
    }
    else { // duplicate keys are not allowed
        return node;
    }
    node->height = std::max(height(node->left), height(node->right)) + 1;
    int balanceFactor = getBalanceFactor(node);

    // Left Left Case
    if (balanceFactor > 1 && key < node->left->key) {
        return rightRotate(node);
    }

    // Right Right Case
    if (balanceFactor < -1 && key > node->right->key) {
        return leftRotate(node);
    }

    // Left Right Case
    if (balanceFactor > 1 && key > node->left->key) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Right Left Case
    if (balanceFactor < -1 && key < node->right->key) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

bool search(Node* node, int key)
{
    if (node == nullptr) {
        return false;
    }
    if (key == node->key) {
        return true;
    }
    if (key < node->key) {
        return search(node->left, key);
    }
    return search(node->right, key); 
}

Node* minValueNode(Node* node)
{
    if (node->left == nullptr) {
        return node;
    }
    return minValueNode(node->left);
}

Node* deleteNode(Node* node, int key)
{
    if (node == nullptr) { // node not found
        return node;
    }

    if (key < node->key) { // key is in left subtree
        node->left = deleteNode(node->left, key);
    }
    else if (key > node->key) { // key is in right subtree
        node->right = deleteNode(node->right, key);
    }
    else { // key is found, delete it

        // node with only one child or no child
        if ((node->left == nullptr) || (node->right == nullptr)) {
            Node* temp = nullptr;
            if (temp == node->left)
                temp = node->right;
            else
                temp = node->left;

            if (temp == nullptr) {
                temp = node;
                node = nullptr;
            }
            else
                *node = *temp;

            delete temp;
        }
        else {
            Node* temp = minValueNode(node->right);
            node->key = temp->key;
            node->right = deleteNode(node->right, temp->key);
        }
    }

    if (node == nullptr) {
        return node;
    }

    // update height
    node->height = std::max(height(node->left), height(node->right)) + 1;

    // get balance factor
    int balanceFactor = getBalanceFactor(node);

    // Left Left Case
    if (balanceFactor > 1 && getBalanceFactor(node->left) >= 0) {
        return rightRotate(node);
    }

    // Left Right Case
    if (balanceFactor > 1 && getBalanceFactor(node->left) < 0) {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Right Right Case
    if (balanceFactor < -1 && getBalanceFactor(node->right) <= 0) {
        return leftRotate(node);
    }

    // Right Left Case
    if (balanceFactor < -1 && getBalanceFactor(node->right) > 0) {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

int main() {
    Node* root = nullptr;
    string operation;
    int key;

    while (cin >> operation >> key) {
        if (operation == "insert") {
            root = insert(root, key);
        } else if (operation == "delete") {
            root = deleteNode(root, key);
        } else if (operation == "exists") {
            cout << (search(root, key) ? "true" : "false") << endl;
        }
    }

    return 0;
}