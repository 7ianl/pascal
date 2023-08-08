/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
  var hash = {};
  for (i = 0; i < t.length; i++){
      if (hash[t[i]]===undefined){
          hash[t[i]] = 1;
      } else {
          hash[t[i]] += 1;
      }
  }
  for (i = 0; i < s.length; i++){
      hash[s[i]] -= 1;
  }
  for (var [k, v] of Object.entries(hash)){
      if (v == 1){
          return k;
      }
  }
};