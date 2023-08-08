/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
  let sub = [];
  sub.push(nums[0]);
  for (i = 1; i < nums.length; i++){
      if (nums[i] > sub[sub.length-1]){
          sub.push(nums[i]);
      } else {
          for (j = 0; j < sub.length; j++){
              if(sub[j] >= nums[i]){
                  sub.splice(j, 1, nums[i]);
                  break;
              }
          }
      }
  }
  return sub.length;
};