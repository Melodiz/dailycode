class Solution
{
public:
    vector<int> sortArray(vector<int>& nums)
    {
        return MergeSort(nums, 0, nums.size() - 1);
    }

    vector<int> MergeSort(vector<int>& nums, int left, int right)
    {
        if (left >= right)
        {
            return {nums[left]};
        }

        int mid = left + (right - left) / 2;
        vector<int> leftArray = MergeSort(nums, left, mid);
        vector<int> rightArray = MergeSort(nums, mid + 1, right);

        return MergeTwoArrays(leftArray, rightArray);
    }

    vector<int> MergeTwoArrays(vector<int>& nums1, vector<int>& nums2)
    {
        vector<int> mergedArray;
        int i = 0, j = 0;

        while (i < nums1.size() && j < nums2.size())
        {
            if (nums1[i] < nums2[j])
            {
                mergedArray.push_back(nums1[i]);
                i++;
            }
            else
            {
                mergedArray.push_back(nums2[j]);
                j++;
            }
        }

        while (i < nums1.size())
        {
            mergedArray.push_back(nums1[i]);
            i++;
        }

        while (j < nums2.size())
        {
            mergedArray.push_back(nums2[j]);
            j++;
        }

        return mergedArray;
    }
};