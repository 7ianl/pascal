/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
  g.sort((a,b) => a-b);
  s.sort((a,b) => a-b);
  let p1 = g.length-1, p2 = s.length-1, res = 0;
  while(p1 >= 0 && p2 >= 0){
      if (g[p1] > s[p2]){
          p1-=1;
      } else {
          p1 -= 1;
          p2 -= 1;
          res += 1;
      }
  }
  return res;
};