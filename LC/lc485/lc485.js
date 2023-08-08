/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
  let mem = 0, cont = 0;
  for (i = 0; i < nums.length; i++) {
      if (nums[i]) {
          cont += 1;
          mem = (mem > cont) ? mem : cont;
      } else {cont = 0;}
  }
  return mem;
};