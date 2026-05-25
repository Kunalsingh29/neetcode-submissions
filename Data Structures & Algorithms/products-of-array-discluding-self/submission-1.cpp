class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefix_sum = 1, postfix_sum = 1;
        vector<int> prefix_list; 
        vector<int> postfix_list;
        vector<int> result;
        for(int i = 0; i<nums.size(); i++){
            if(i == 0) prefix_list.push_back(1);
            else{
                prefix_sum*=nums[i-1];
                prefix_list.push_back(prefix_sum);
                //cout<<"prefix_sum = "<< " for i ==:"<<i<< " --"<<prefix_sum<<endl;
            }
        }
         for(int i = nums.size() - 1; i>=0; i--){
            if(i == (nums.size() - 1)) postfix_list.push_back(1);
            else{
                postfix_sum*=nums[i+1];
                postfix_list.push_back(postfix_sum);
                //cout<<"postfix_sum = "<<" for i ==:"<<i<< " --"<< postfix_sum<<endl;
            
            }
        }
        for(int i = 0; i<nums.size(); i++){
            // cout<<" value for this i == "<<i<<" is"<< prefix_list[i]<< " and" <<postfix_list[i]<<"= "<< prefix_list[i]*postfix_list[i]<<endl;
            result.push_back(prefix_list[i]*postfix_list[nums.size() - i-1]); 
        }
        return result;

       
    }
};