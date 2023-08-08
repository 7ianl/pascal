/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
  let hash = {}, l = s.length;
  for (i = 0; i < l; i++){
      if (hash[s[i]] === undefined){
          hash[s[i]] = i;
      } else {hash[s[i]] = l;}
  }
  let res = Math.min.apply(null, Object.values(hash));
  return (res == l) ? -1 : res;
};