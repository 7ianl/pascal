/**
 * @param {number[]} arr
 * @return {number[]}
 */
var replaceElements = function(arr) {
  let max = -1, max2 = -1;
  for (i = arr.length - 1; i >= 0; i--) {
      max2 = (max > arr[i]) ? max : arr[i];
      arr[i] = max;
      max = max2;
  }
  return arr;
};