/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
  var tmp = {};
  var disp = k%nums.length;
  var c = nums.length-disp;
  for(var i = 0; i<c; i++){
      tmp[i] = nums[i]
  }
  for (var i = c; i <nums.length; i++){
      nums[i-c] = nums[i]
  }
  for (var i = 0; i < c; i++){
      nums[disp+i] = tmp[i]
  }
};