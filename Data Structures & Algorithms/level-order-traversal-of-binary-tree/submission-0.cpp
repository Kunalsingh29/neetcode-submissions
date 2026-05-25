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
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        // vector to store children of current node. 
       // vector to store all output. 
        
        vector<vector<int>> output;
        queue<TreeNode*> q;
        if(!root) return output;
        q.push(root);

        while(!q.empty()){
            int currSize = q.size();
            vector<int> curLevel;
            for(int i = 0; i<currSize; i++){
                TreeNode* temp = q.front();
                q.pop();
                curLevel.push_back(temp->val);
                if(temp->left) q.push(temp->left);
                if(temp->right) q.push(temp->right);

            }
            
            output.push_back(curLevel);

        }
        return output;



       
        

       


    }
};