class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqMap;
        vector<int> top_k_elements;
        priority_queue<pair<int, int>, vector<pair<int,int>>, greater<>> frequency_queue;
        // populate map based on freuency. 
        // create bucket list. 
        // populate bucket based onfrequewncy of element. 
        // finally populate the result with k elements. 
        for(auto &num: nums){
            freqMap[num]++;
        }
        int n = nums.size();
        vector<vector<int>> bucket_list(n+1);
        for(auto &[num, freq]: freqMap){
            bucket_list[freq].push_back(num);
        }

        for(int i = n; i>=0 & top_k_elements.size()<k; --i){

            for(auto &elem:bucket_list[i]){
                top_k_elements.push_back(elem);
                if(top_k_elements.size() == k) break;
            }
           // top_k_elements.push_back(bucket_list[i]);
        }//

        return top_k_elements;

    }

};
