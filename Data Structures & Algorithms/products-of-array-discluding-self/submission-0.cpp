class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> output(n, 0);
        int prefix = 1, postfix = 1;
        // prefix output update;
        for(int i = 0; i<n; i++){
            if(i == 0){
                prefix = 1;
            }
            output[i] = prefix;
            prefix = prefix*nums[i];
        }

        for(int j = n-1; j>=0; j--){
            if(j == n-1){
                postfix = 1;
            }
            output[j] = output[j]*postfix;
            postfix  = postfix*nums[j];
        }

        return output;
    }
};