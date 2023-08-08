/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
  var res = 0;
  for (i = 0; i <logs.length; i++){
      if (logs[i] === "./"){
          continue;
      }
      else if (logs[i] === "../"){
          res = res === 0 ? 0 : res-1;
      }
      else {
          res += 1;
      }
  }
  return res;
};