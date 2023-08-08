/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function(nums) {
  var res = 0;
  for (i = 0; i < nums.length-2; i++){
      for (j = i+1; j < nums.length-1; j++){
          var upper = nums[i] + nums[j];
          var lower = nums[i] - nums[j];
          if (lower < 0) {lower = -lower;}
          for (k = j+1; k < nums.length; k++){
              if (nums[k] > lower && nums[k] < upper) {res++;}
          }
      }
  }
  return res;
};