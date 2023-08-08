/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
  var res = [0, 0];
  for (i = 0; i < nums.length; i++){
      res = [Math.max(res[1], res[0]), res[0] + nums[i]];
  }
  return Math.max(res[0], res[1]);
};