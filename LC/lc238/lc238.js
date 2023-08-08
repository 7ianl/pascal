/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  let cur = 1, tmp;
  let res = Array(nums.length).fill(1);
  for (i = nums.length - 1; i >= 0; i--){
      res[i] *= cur;
      cur *= nums[i];
  }
  cur = 1;
  for (i = 0; i < nums.length; i++){
      res[i] *= cur;
      cur *= nums[i];
  }
  return res;
};