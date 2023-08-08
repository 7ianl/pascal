/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  dp = 0, cont = 0, mem = {};
  for (i = 0; i < s.length; i++) {
      cont = (s[i] in mem) ? 
          ((cont + 1 > i - mem[s[i]]) ? i - mem[s[i]] : cont+1) : (cont + 1);
      dp = (dp > cont) ? dp : cont;
      mem[s[i]] = i;
  }
  return dp;
};