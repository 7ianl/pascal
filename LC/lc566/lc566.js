/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
  var x = mat.length, y = mat[0].length;
  if (x * y != r * c) {return mat;}
  var stack = [];
  var res = [], t = [];
  for (i = 0; i < r; i++){
      for(j = 0; j < c; j++){
          if (stack.length === 0) {stack = mat.pop()};
          t.push(stack.pop());
      }
      t = t.reverse();
      res.push(t);
      t = [];
  }
  res = res.reverse();
  return res;
};