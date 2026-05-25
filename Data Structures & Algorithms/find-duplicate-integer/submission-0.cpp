class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[0];
        /// here slow = fast; 
        // find intersecdtion point in cycle

        do {
            slow = nums[slow];
            fast = nums[nums[fast]];


        } while(slow!=fast);
        slow = nums[0];
        while(slow!=fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
        

        
    }
};