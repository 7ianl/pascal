/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
  var res = 0;
  for (i = 0; i <31; i++){
      if (x%2 - y%2 !==0){
          res += 1;
      }
      x >>= 1;
      y >>= 1;
  }
  return res;
};