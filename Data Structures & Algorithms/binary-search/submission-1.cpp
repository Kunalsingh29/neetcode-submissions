class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        // left = 0; right = n-2 
        // mid = left + right-left/2
        // if target < mid, right sgift, if target > mid, left shift mid +1; 
       // if mid == target reruen index return -1
       int left = 0;
       int n = nums.size();
       int right = n-1;
       while(left<=right){
            int mid = left + (right - left)/2;
            if(nums[mid] == target) return mid; 
            else if(nums[mid]> target) right = mid-1;
            else left = mid+1;    
       }
        return -1;

    
    }

};