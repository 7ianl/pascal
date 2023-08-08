/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
  if (s.length === 0){return true;}
  else if (t.length === 0){return false;}
  else if (s[0] == t[0]){return isSubsequence(s.substring(1), t.substring(1));}
  else return isSubsequence(s, t.substring(1));
};