class Solution
{
public:
    string removeKdigits(string num, int k)
    {
        if (num.size() <= k)
            return "0";
        for (size_t i = 0; i < num.length() - 1; i++)
        {
            if (k == 0)
                break;
            if (num[i] > num[i + 1])
            {
                num[i] = '*';
                k--;
            }
        }
        for (size_t i = 0; i < num.length(); i++)
        {
            if (num[i] != '0' && num[i] != '*')
                break;
            num[i] = '*';
        }
        erase(num, '*');

        //
        int i = 9;
        while (i > 0)
        {
            cout << k << " " << num << endl;
            for (size_t j = 0; j < num.length(); j++)
            {
                if (not k)
                    break;
                if (char(num[j]) == 48+i)
                {
                    num[j] = '*';
                    k--;
                }
            }
            i--;
        }
        for (size_t i = 0; i < num.length(); i++)
        {
            if (num[i] != '0' && num[i] != '*')
                break;
            num[i] = '*';
        }
        erase(num, '*');

        if (num == "")
            return "0";
        return num;
    }
};