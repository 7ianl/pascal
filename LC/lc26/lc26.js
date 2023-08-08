/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  let p = 0, last = -100000;
  for (i = 0; i < nums.length; i++) {
      if (nums[i] != last){
          nums[p] = nums[i];
          p += 1;
          last = nums[i];
      }
  }
  nums.splice(p, nums.length - p);
};