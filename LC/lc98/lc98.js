/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
  var getMin = t => {
      if (!t.left) return t.val;
      else return getMin(t.left);
  }
  var getMax = t => {
      if (!t.right) return t.val;
      else return getMax(t.right);
  }
  var helper = function(t){
      if (t === null){
          return true;
      } else return ((t.left ? t.val > getMax(t.left) : true) 
                     && (t.right ? t.val < getMin(t.right) : true)
                    && helper(t.left) && helper(t.right));
  };
  return helper(root);
};