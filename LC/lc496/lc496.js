/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {
  let dpStack = [], mem = {};
  for(i = nums2.length-1; i>= 0; i--){
      n = nums2[i];
      while(true){
          let k = dpStack.pop();
          if (k === undefined){
              mem[n] = -1;
              dpStack.push(n);
              break;
          } else if (k>n){
              mem[n] = k;
              dpStack.push(k);
              dpStack.push(n);
              break;
          }
      }
  }
  return nums1.map(x => mem[x]);
};