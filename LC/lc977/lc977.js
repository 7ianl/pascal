/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
  /* let a = nums.map(x => x*x), p, tmp1, tmp2, res = [];
  for (i = 0; i < nums.length-1; i++) {
      if (a[i] < a[i+1]) {
          p = i;
          break;
      }
  }
  let b = a.splice(p+1);
  b.reverse();
  tmp1 = a.pop(), tmp2 = b.pop();
  while (a.length || b.length){
      if (tmp1 && tmp2) {
          if (tmp1 < tmp2){
              res.push(tmp1);
              tmp1 = a.pop();
          } else {
              res.push(tmp2);
              tmp2 = b.pop();
          } 
      }
      else if (tmp1) {
          res.push(tmp1);
          tmp1 = a.pop();
      } else {
          res.push(tmp2);
          tmp2 = b.pop();
      }
  }
  return res; */
  return nums.map(x => x*x).sort((a, b) => a- b);
};