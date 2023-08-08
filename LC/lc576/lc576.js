/**
 * @param {number} m
 * @param {number} n
 * @param {number} maxMove
 * @param {number} startRow
 * @param {number} startColumn
 * @return {number}
 */
var findPaths = function(m, n, maxMove, startRow, startColumn) {
  var max = m * n, pos = startRow*n + startColumn, m = Math.pow(10, 9)+7;
  var oobNum = (k) => {
      return (k-n< 0) + (k + n >= max) + (k % n === 0) + ((k+1) % n ===0);
  };
  var dp = [];
  if (maxMove === 0){
      return 0;
  }
  for (i = 0; i < max; i++){
      dp.push(oobNum(i));
  }
  var res = dp[pos];
  var helper = function(e, i, a) {
          return (i-n<0 ? 0 : a[i-n]) + (i+n>=max ? 0 : a[i+n])
          + (i%n===0 ? 0 : a[i-1]) + ((i+1)%n===0 ? 0 : a[i+1]);
      };    
  for (j=1; j <maxMove; j++){
      dp = dp.map(helper).map(a => a%m);
      res += dp[pos];
  }
  return res%m;
};