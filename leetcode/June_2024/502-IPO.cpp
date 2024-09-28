class Solution
{
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital)
    {
        priority_queue<int> maxHeap;
        vector<pair<int, int>> projects;
        
        for (size_t i = 0; i < profits.size(); ++i)
        {
            projects.push_back({capital[i], profits[i]});
        }
        
        sort(projects.begin(), projects.end());
        
        int i = 0;
        while (k--)
        {
            while (i < projects.size() && projects[i].first <= w)
            {
                maxHeap.push(projects[i].second);
                ++i;
            }
            
            if (maxHeap.empty())
                break;
            
            w += maxHeap.top();
            maxHeap.pop();
        }
        
        return w;
    }
};