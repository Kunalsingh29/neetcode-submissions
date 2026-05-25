class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // n, k-n to be sought.
        int n = nums.size();
        unordered_map<int, int> pairDict;
        for(int i = 0; i<n; i++){
            if(pairDict.find(target-nums[i])!= pairDict.end()){
                return {pairDict[target-nums[i]], i};
            }
            else{
                pairDict[nums[i]] = i;
            }
        }
        return {-1};
        
    }
};