/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
  let res = [cost[0], cost[1]];
  cost.push(0);
  for (i = 2; i < cost.length; i++){
      res.push(Math.min(cost[i] + res[i-1], cost[i] + res[i-2]));        
  }
  return res[res.length-1];
};