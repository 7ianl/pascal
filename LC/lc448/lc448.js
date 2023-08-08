/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
  let res = [], tmp;
  for (i = nums.length - 1; i >= 0; i--){
      if (nums[i] !== i+1 && nums[nums[i]-1] !== nums[i]) {
          tmp = nums[nums[i]-1];
          nums[nums[i]-1] = nums[i];
          nums[i] = tmp;
          i++;
      }
  }
  for (j = 0; j < nums.length; j++){
      if (nums[j] !== j+1) {
          res.push(j+1);
      }
  }
  return res;
};