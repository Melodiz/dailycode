class Solution
{
private:
    unordered_map<int, vector<int>> adj;
    int comp;

public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k)
    {
        comp = 0;

        int src = 0;

        for (const vector<int>& edge: edges)
        {
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        dfs(src, -1, values, k);
        return comp;
    }

private:
    int dfs(int root, int parent, vector<int>& values, int k)
    {
        int ans = values[root];

        for (int neigh: adj[root])
        {
            if (parent != neigh)
            {
                ans += dfs(neigh, root, values, k);
            }
        }

        if (ans % k == 0)
        {
            comp++;
            return 0;
        }

        return ans % k;
    }
};