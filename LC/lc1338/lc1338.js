/**
 * @param {number[]} arr
 * @return {number}
 */
var minSetSize = function(arr) {
  var hash = {};
  var sz = arr.length;
  for (i = 0; i < sz; i++){
      if (hash[arr[i]] === undefined){
          hash[arr[i]] = 1;
      } else {hash[arr[i]] +=1;}
  }
  var cnt = Object.values(hash).sort((a, b)=> b-a);
  var sum = 0, res;
  for (j = 0; j < cnt.length; j++){
      sum += cnt[j];
      if (sum * 2 >= sz){
          res = j;
          break;
      }
  }
  return res + 1;
};