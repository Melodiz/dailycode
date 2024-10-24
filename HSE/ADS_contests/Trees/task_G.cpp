#include <vector>
#include <iostream>
using namespace std;

// Constants
const int MOD = 1000000001;

// Treap Node Structure
struct Node {
    int key;
    int priority;
    long long sum;
    int size;
    Node* left;
    Node* right;

    Node(int k) : key(k), priority(rand()), sum(k), size(1), left(nullptr), right(nullptr) {}
};

// Utility Functions
int get_size(Node* t)
{
    return t ? t->size : 0;
}

long long get_sum(Node* t)
{
    return t ? t->sum : 0;
}

void update(Node* t)
{
    if (t)
    {
        t->size = 1 + get_size(t->left) + get_size(t->right);
        t->sum = t->key + get_sum(t->left) + get_sum(t->right);
    }
}

// Split treap 't' into 'left' and 'right' based on key.
// All keys < key go to 'left', and >= key go to 'right'.
void split(Node* t, int key, Node*& left, Node*& right)
{
    if (!t)
    {
        left = right = nullptr;
    }
    else if (key > t->key)
    {
        split(t->right, key, t->right, right);
        left = t;
    }
    else
    {
        split(t->left, key, left, t->left);
        right = t;
    }
    update(t);
}

// Merge two treaps 'left' and 'right' and return the new root.
Node* merge(Node* left, Node* right)
{
    if (!left || !right)
        return left ? left : right;
    if (left->priority > right->priority)
    {
        left->right = merge(left->right, right);
        update(left);
        return left;
    }
    else
    {
        right->left = merge(left, right->left);
        update(right);
        return right;
    }
}

// Insert key into treap 't'. Returns the new root.
Node* insert(Node* t, Node* it)
{
    if (!t)
        return it;
    if (it->key == t->key)
        return t;// Ignore duplicates
    if (it->priority > t->priority)
    {
        split(t, it->key, it->left, it->right);
        update(it);
        return it;
    }
    if (it->key < t->key)
        t->left = insert(t->left, it);
    else
        t->right = insert(t->right, it);
    update(t);
    return t;
}

// Erase key from treap 't'. Returns the new root.
Node* erase(Node* t, int key)
{
    if (!t)
        return t;
    if (t->key == key)
    {
        Node* res = merge(t->left, t->right);
        delete t;
        return res;
    }
    if (key < t->key)
        t->left = erase(t->left, key);
    else
        t->right = erase(t->right, key);
    update(t);
    return t;
}

// Find if key exists in treap 't'.
bool find_key(Node* t, int key)
{
    while (t)
    {
        if (t->key == key)
            return true;
        if (key < t->key)
            t = t->left;
        else
            t = t->right;
    }
    return false;
}

// Calculate the sum of keys in [l, r] in treap 't'.
long long range_sum(Node*& t, int l, int r)
{
    Node *t1, *t2, *t3;
    split(t, l, t1, t2);     // t1: < l, t2: >= l
    split(t2, r + 1, t2, t3);// t2: <= r, t3: > r
    long long res = get_sum(t2);
    t = merge(t1, merge(t2, t3));// Merge back
    return res;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    srand(time(0));

    int n;
    cin >> n;
    Node* treap = nullptr;
    long long s = 0;
    while (n--)
    {
        char cmd;
        cin >> cmd;
        if (cmd == '+')
        {
            long long i;
            cin >> i;
            long long fx = (i + s) % MOD;
            // Insert fx if not present
            if (!find_key(treap, fx))
            {
                treap = insert(treap, new Node(fx));
            }
        }
        else if (cmd == '-')
        {
            long long i;
            cin >> i;
            long long fx = (i + s) % MOD;
            // Erase fx if present
            if (find_key(treap, fx))
            {
                treap = erase(treap, fx);
            }
        }
        else if (cmd == '?')
        {
            long long i;
            cin >> i;
            long long fx = (i + s) % MOD;
            if (find_key(treap, fx))
            {
                cout << "Found\n" << flush;
            }
            else
            {
                cout << "Not found\n" << flush;
            }
        }
        else if (cmd == 's')
        {
            long long l, r;
            cin >> l >> r;
            long long fl = (l + s) % MOD;
            long long fr = (r + s) % MOD;
            // Ensure fl <= fr
            if (fl > fr)
            {
                swap(fl, fr);
            }
            long long total = range_sum(treap, fl, fr);
            cout << total << '\n'  << flush;
            s = total;
        }
    }
}