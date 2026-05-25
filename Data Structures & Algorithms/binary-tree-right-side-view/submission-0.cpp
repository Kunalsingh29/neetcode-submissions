class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> output;
        if (!root) return output;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                // First node in level when traversed right to left is the rightmost
                if (i == 0) output.push_back(node->val);

                // Push right first so it comes first in next level
                if (node->right) q.push(node->right);
                if (node->left) q.push(node->left);
            }
        }

        return output;
    }
};
