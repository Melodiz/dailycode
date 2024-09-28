/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solutionct
{
public:
    int sumNumbers(TreeNode* root)
    {
        return Node(root, 0);
    }
    int Node(TreeNode* node, int path_sum)
    {
        if (!node)
            return 0;
        path_sum = path_sum * 10 + node->val;
        if (!node->left && !node->right)
            return path_sum;

        return Node(node->left, path_sum) + Node(node->right, path_sum);
    }
};