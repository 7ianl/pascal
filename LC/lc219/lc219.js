/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    var hash = {};
    var res = false;
    for (i=0; i<nums.length;i++){
        if (hash[nums[i]] === undefined || i - hash[nums[i]] > k){
            hash[nums[i]] = i;
        } else {
            res = true;
            break;
        }
    } 
    return res;
};