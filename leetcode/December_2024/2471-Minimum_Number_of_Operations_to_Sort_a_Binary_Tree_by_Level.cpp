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
    static int minimumOperations(TreeNode* root)
    {
        TreeNode* q[100000];
        int front = 0, back = 0;
        q[back++] = root;
        int swaps = 0;
        while (back - front > 0)
        {
            const int qz = back - front;
            int* idx = (int*) alloca(qz * sizeof(int));
            iota(idx, idx + qz, 0);
            int* arr = (int*) alloca(qz * sizeof(int));
            for (int i = 0; i < qz; i++)
            {
                auto node = q[front++];
                arr[i] = node->val;
                if (node->left) q[back++] = node->left;
                if (node->right) q[back++] = node->right;
            }
            // each value is unique, no need for stable_sort
            sort(idx, idx + qz, [&](int i, int j) {
                return arr[i] < arr[j];
            });
            for (int i = 0; i < qz;)
            {
                int j = idx[i];
                if (j != i)
                {// check twice
                    swaps++;
                    swap(idx[i], idx[j]);
                }
                else
                    i++;// next iteration
            }
        }
        return swaps;
    }
};


auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();