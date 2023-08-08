/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
  let c = parseInt(x.toString().split("").reverse().join(""), 10);
  if (x < 0) { c = -c; }
  return (-Math.pow(2, 31) <= c && c <= Math.pow(2, 31)-1) ? c : 0;
};