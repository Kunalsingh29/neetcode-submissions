class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>>output;
        // to print 3 elements in output that corresponds to 3 sum 
        // find 3 element from beginning that sum upto 0;
        // start from 1, then check left and right pointer to find the sum. 
        sort(nums.begin(), nums.end());
    
        int n = nums.size();
        int l = 0, r = 0;
        for(int i = 0; i<n-2; i++){
            if(i>0 && nums[i] == nums[i-1] ){
                continue;
            }

            l = i+1;
            r = n-1;
            while(l<r){
                int threesum = nums[i] + nums[l] + nums[r];
                if(threesum >0){
                    r-=1;
                }
                else if(threesum<0){
                    l+=1;
                }
                else{
                    output.push_back({nums[i], nums[l], nums[r]});
                    // output.push_back(nums[l]);
                    // output.push_back(nums[r]);
                    //v.insert(v.end(), {1, 2, 3});
                    l++;
                    while(l<r && nums[l] == nums[l-1]){
                        l+=1;
                    }

                }
            }
           // return output;
            

        }
        return output;
    }
};