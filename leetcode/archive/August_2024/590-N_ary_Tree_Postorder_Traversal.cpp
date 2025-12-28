class Solution
{
public:
    vector<int> postorder(Node* root)
    {
        // Return an empty vector if the root is null
        if (root == nullptr) return {};

        vector<int> result;

        // Lambda function for DFS traversal
        function<void(Node*)> traverse = [&](Node* node) {
            // Traverse all children of the current node
            for (Node* child : node->children)
            {
                traverse(child);
            }
            // Add the current node's value to the result vector
            result.push_back(node->val);
        };

        // Initiate DFS from the root node
        traverse(root);

        // Return the result vector with post-order traversal values
        return result;
    }
};