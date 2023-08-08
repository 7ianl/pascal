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
 * @return {number[]}
 */
var preorderTraversal = function(root) {
  let res = [];
  let helper = function(t){
      if (!t){return;} else{
          res.push(t.val);
          helper(t.left);
          helper(t.right);
          return;
      }
  }
  helper(root);
  return res;
};