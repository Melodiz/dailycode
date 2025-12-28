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
class Solution
{
public:
    string smallestFromLeaf(TreeNode* root)
    {
        string ans = "";
        ans += char(root->val + 97);
        while (root->left && root->right)
        {
            if (determineDirection(root))
            {
                ans = char(root->left->val+97) + ans;
                root = root->left;
            }
            else
            {
                ans = char(root->left->val+97) + ans;
                root = root->right;
            }
        }
        return ans;
        }
    bool determineDirection(TreeNode* root)
    {
        if (root->left->val > root->right->val)
        {
            return true;
        }
        else if (root->left->val < root->right->val)
        {
            return false;
        }
        return determineDirection(root->left) || determineDirection(root->right);
    }
};