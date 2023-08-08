class Solution {
public:
    int search(vector<int>& nums, int target) {
        int a = 0, b = (int)nums.size()-1;
        while (a <= b) {
            int k = (a+b)/2;
            if(nums[k] == target) return k;
            if(nums[k] > target) b = k-1;
            else a = k+1;
        }
        return -1;
    }
};