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
 * @param {number} k
 * @return {boolean}
 */
var findTarget = function(root, k) {
  let hash = {};
  let findHelper = function(t) {
      if (!t) {
          return false;
      } else if (k - t.val in hash) {
          return true;
      } else {
          hash[t.val] = 1;
          return (findHelper(t.left) || findHelper(t.right));
      }
  }
  return findHelper(root);
};