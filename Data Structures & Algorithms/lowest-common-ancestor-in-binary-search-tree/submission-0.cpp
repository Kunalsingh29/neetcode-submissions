/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr || root == p|| root == q) return root; //base case; 

        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);

        // if both values are in left and right of root, then current root is he LCA. 
         //it must be in left or right now. 
         //one f them is null and other non null. 
         if(left != nullptr && right != nullptr){
            return root;
            }

        return left!=nullptr?left:right;

    

    }
};