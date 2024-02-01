class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        vector<int> result(temperatures.size(), 0);
        vector<int> stack;

        for (size_t i = temperatures.size() - 1; i >= 0; --i)
        {
            int curr_temperature = temperatures[i];

            while (!stack.empty() && curr_temperature >= temperatures[stack.back()])
            {
                stack.pop_back();
            }
            if (!stack.empty())
            {
                result[i] = stack.back() - i;
            }
            stack.push_back(i);
        }
        return result;
    }
};