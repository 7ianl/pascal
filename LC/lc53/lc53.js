/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  var cur = nums[0], res = nums[0];
  for (i = 1; i < nums.length; i++){
      cur = Math.max(cur + nums[i], nums[i]);
      res = Math.max(cur, res);
  }
  return res;
};