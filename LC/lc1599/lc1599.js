/**
 * @param {number[]} customers
 * @param {number} boardingCost
 * @param {number} runningCost
 * @return {number}
 */
var minOperationsMaxProfit = function(customers, boardingCost, runningCost) {
  var maxProfit = 0;
  var curProfit = 0;
  var curCustomers = 0;
  var boarding = 0;
  var rotations = 0;
  var maxRotation = 0;
  if (runningCost >= boardingCost * 4){
      return -1;
  }
  for (i = 0; i < customers.length; i++){
      rotations += 1;
      curCustomers += customers[i];
      boarding = Math.min(curCustomers, 4);
      curCustomers -= boarding;
      curProfit += (boarding*boardingCost - runningCost);
      if (maxProfit < curProfit){
          maxProfit = curProfit;
          maxRotation = rotations;
      }
  }
  while(curCustomers){
      rotations += 1;
      boarding = Math.min(curCustomers, 4);
      curCustomers -= boarding;
      curProfit += (boarding*boardingCost - runningCost);
      if (maxProfit < curProfit){
          maxProfit = curProfit;
          maxRotation = rotations;
      }
  }
  return (maxRotation === 0 ? -1 : maxRotation);
};