/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(matrix, k) {
  var rows = matrix.length, cols = matrix[0].length;
  var lo = matrix[0][0], hi = matrix[rows-1][cols-1];
  while(lo <= hi){
      var mid = lo + Math.floor((hi - lo)/2);
      var count = 0, maxNum = lo;
      for (r = 0; r < rows; r++){
          var c = rows - 1;
          while(c >= 0 && matrix[r][c]> mid) c--;
          if (c >= 0){
              count += (c+1);
              maxNum = Math.max(maxNum, matrix[r][c]);
          }
      }
      if (count == k) return maxNum;
      else if (count < k) lo = mid + 1;
      else hi = mid - 1;
  }
  return lo;
};