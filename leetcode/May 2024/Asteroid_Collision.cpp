class Solution
{
public:
    vector<int> asteroidCollision(vector<int>& asteroids)
    {
        std::vector<int> st{asteroids[0]};
        for (int i = 1; i < asteroids.size(); ++i)
        {
            if (asteroids[i] * st.back() < 0)
            {
                std::cout << st.back() << " " << asteroids[i] << std::endl;
                while (!st.empty())
                {
                    if (asteroids[i] * st.back() > 0) { break; }
                    else if (abs(asteroids[i]) > abs(st.back()))
                    {
                        st.pop_back();
                        st.push_back(asteroids[i]);
                    }
                    else if (abs(asteroids[i]) == abs(st.back())) { st.pop_back(); }
                    else { break; }
                }
            }
            else
                st.push_back(asteroids[i]);
        }


        return st;
    }
};