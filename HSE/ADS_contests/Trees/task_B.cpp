#include <iostream>
#include <limits>
#include <vector>

struct Node {
    int key;
    int left;
    int right;
};

bool IsBSTUtil(const std::vector<Node>& tree, int root, int min, int max)
{
    if (root == -1) return true;
    if (tree[root].key <= min || tree[root].key >= max) return false;
    return IsBSTUtil(tree, tree[root].left, min, tree[root].key) &&
           IsBSTUtil(tree, tree[root].right, tree[root].key, max);
}

bool IsBST(const std::vector<Node>& tree, int root)
{
    return IsBSTUtil(tree, root, std::numeric_limits<int>::min(), std::numeric_limits<int>::max());
}

int main()
{
    int n;
    std::cin >> n;
    std::vector<Node> tree(n);
    for (int i = 0; i < n; ++i)
    {
        std::cin >> tree[i].key >> tree[i].left >> tree[i].right;
    }

    if (IsBST(tree, 0))
    {
        std::cout << "CORRECT" << std::endl;
    }
    else
    {
        std::cout << "INCORRECT" << std::endl;
    }

    return 0;
}