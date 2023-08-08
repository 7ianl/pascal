/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  hash = {};
  for (i = 0; i < nums.length; i++) {
      k = target - nums[i];
      if (k in hash) {
          return [i, hash[k]];
      }
      hash[nums[i]] = i;
  }
  return ans;
};