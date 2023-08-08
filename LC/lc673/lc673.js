/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumberOfLIS = function(nums) {
  let dp = [], res = 0;
  for (i = 0; i < nums.length; i++){
      dp[i] = 1;
      for (j = 0; j < i; j++){
          if (nums[j] < nums[i] && dp[j] >= dp[i]){
              dp[i] = dp[j]+1;
          }
      }
  }
  let c = Math.max(...dp), ct = [], tmp;
  for (j = 0; j < dp.length; j++){
      if(dp[j] == 1){
          ct[j] = 1;
      } else {
          tmp = 0;
          for (k = 0; k < j; k++){
              if (dp[k] == dp[j]-1 && nums[k] < nums[j]){
                  tmp += ct[k];
              }
          }
          ct[j] = tmp;
      }
  }
  for (r = 0; r < dp.length; r++){
      if (dp[r] == c){
          res += ct[r];
      }
  }
  return res;
};