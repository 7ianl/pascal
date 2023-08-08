/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
  var hash = [], n = k, max = 0, cur = 0, c;
  for (i = 0; i < nums.length; i++) {
      if (nums[i] === 0){
          hash.push(i);
          if (n === 0){
              c = hash.splice(0, 1);
              if (c === undefined) {cur = 0;}
              else {cur = i - c;}
              max = Math.max(max, cur);
          } else {
              n -=1;
              cur +=1;
              max = Math.max(max, cur);
          } 
      } else { 
          cur+=1;
          max = Math.max(max, cur);
      }
  }
  return max;
};