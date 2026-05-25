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
    int diameterOfBinaryTree(TreeNode* root) {
        int maxD = 0;
        height(root, maxD);
        return maxD;
        
    }
    int height( TreeNode* node, int &maxD){
        if(!node) return 0;
        int lh = height(node->left, maxD);
        int rh = height(node->right, maxD);
        maxD = max(maxD, (lh+rh));
        return 1+max(lh, rh);

    }
};