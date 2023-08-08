/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves = function(nums) {
  var k = Math.min.apply(null, nums);
  var s = nums.reduce((a, c) => a + c, 0);
  return s-k*nums.length;
};