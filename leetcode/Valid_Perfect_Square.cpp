class Solution
{
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2)
    {
        sort(nums1.begin(), nums1.end());
        nums1.erase(unique(nums1.begin(), nums1.end()), nums1.end());
        sort(nums2.begin(), nums2.end());
        nums2.erase(unique(nums2.begin(), nums2.end()), nums2.end());
        vector<int> v_intersection;
        set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(),
                         back_inserter(v_intersection));
        return v_intersection;
    }
};