/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
  let p1 = 0, p2 = (nums.length - 1), tmp;
  while (p1 < p2){
      if (nums[p1] % 2){
          tmp = nums[p1];
          nums[p1] = nums[p2];
          nums[p2] = tmp;
          p2 -= 1;
      } else {p1 += 1;}
  }
  return nums;
};