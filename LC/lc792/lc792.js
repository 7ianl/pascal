/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var numMatchingSubseq = function(s, words) {
  var isSubseq = function(s, sub){
      if (sub === ''){return true;}
      else if (s === ''){return false;}
      else if (sub[0]==s[0]){return isSubseq(s.substring(1), sub.substring(1));}
      else return isSubseq(s.substring(1), sub);
  };
  let seqs = [], nonseqs = [];
  return words.reduce(function(acc, cur){
      if(seqs.includes(cur)){
          return acc+1;
      } else if (nonseqs.includes(cur)){
          return acc;
      }
      else if (isSubseq(s, cur)){
          seqs.push(cur);
          return acc+1;
      } else {
          nonseqs.push(cur);
          return acc;
      }
  }, 0);
};