/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> pre;
    stack<TreeNode*> s;
    void traverse(TreeNode* t) {
        s.push(t);
        while(!s.empty()){
            TreeNode* n = s.top();
            s.pop();
            if (n != nullptr){
                pre.push_back(n->val);
                s.push(n->right);
                s.push(n->left);
            }
        }
    }
    vector<int> preorderTraversal(TreeNode* root) {
        traverse(root);
        return pre;
    }
};