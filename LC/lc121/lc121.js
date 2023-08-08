/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let cur = prices[0], prof = 0;
  for (i = 0; i < prices.length; i++){
      if (prices[i] < cur){
          cur = prices[i];
      } else if (prices[i] - cur > prof){
          prof = prices[i] - cur;
      }
  }
  return prof;
};