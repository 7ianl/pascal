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
var isSymmetric = function(root) {
  var helper = function (a, b){
      if (!a) return !b;
      else if (!b) return false;
      else return (a.val == b.val) && helper(a.left, b.right) && helper(a.right, b.left);
  };
  return helper(root.left, root.right);
};