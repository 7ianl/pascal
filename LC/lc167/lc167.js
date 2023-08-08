/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
  let p1 = 0, p2 = numbers.length-1, k;
  while(true){
      k = numbers[p1] + numbers[p2];
      if (k < target) {
          p1 += 1;
      } else if (k > target) {
          p2 -= 1;
      } else {return [p1+1, p2+1];}
  }
};