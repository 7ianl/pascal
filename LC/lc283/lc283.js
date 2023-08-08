/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
  let p = 0;
  for (i = 0; i < nums.length; i++){
      if (nums[i]){
          nums[p] = nums[i];
          p+=1;
      }
  }
  for (j = p; j < nums.length; j++){
      nums[j] = 0;
  }
};