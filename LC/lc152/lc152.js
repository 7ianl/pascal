/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
  let cur = nums[0], dpPos = [], dpNeg = [], hasZero = false, res;
  if (cur > 0) {
      dpPos.push(cur);
      dpNeg.push(0);
  } else if (cur < 0) {
      dpPos.push(0);
      dpNeg.push(cur);
  } else {
      dpPos.push(0);
      dpNeg.push(0);
      hasZero = true;
  }
  for (i = 1; i < nums.length; i++){
      if (nums[i] > 0){
          if (dpPos[i-1] === 0){
              dpPos.push(nums[i]);
          } else {dpPos.push(dpPos[i-1]*nums[i]);}
          if (dpNeg[i-1] === 0){
              dpNeg.push(0);
          } else {dpNeg.push(dpNeg[i-1]*nums[i]);}
      } else if (nums[i] < 0){
          if (dpPos[i-1] === 0){
              dpNeg.push(nums[i]);
          } else {dpNeg.push(dpPos[i-1]*nums[i]);}
          if (dpNeg[i-1] === 0){
              dpPos.push(0);
          } else {dpPos.push(dpNeg[i-1]*nums[i]);}
      } else {
          hasZero = true;
          dpPos.push(0);
          dpNeg.push(0);
      }
  }
  res = Math.max.apply(null, dpPos);
  if (res > 0) {return res;} else if (hasZero) {return res;} else {
      return Math.max.apply(null, dpNeg);
  }
};