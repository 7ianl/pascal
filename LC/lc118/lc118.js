/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
  let res = [], row = [];
  for(i = 0; i < numRows; i++){
      if(i === 0){
          res[i] = [1];
      } else {
          row = [];
          row[0] = 1, row[i] = 1;
          for (j = 1; j < i; j++){
              row[j] = res[i-1][j-1] + res[i-1][j];
          }
          res[i] = row;
      }
  }
  return res;
};