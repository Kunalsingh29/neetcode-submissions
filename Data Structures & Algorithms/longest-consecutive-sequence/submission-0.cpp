class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> uset(nums.begin(), nums.end());
        int longest_length = 0;

        for (int num : uset) {
            // Only start counting if it's the start of a sequence
            if (uset.find(num - 1) == uset.end()) {
                int curr = num;
                int streak = 1;

                while (uset.find(curr + 1) != uset.end()) {
                    curr++;
                    streak++;
                }

                longest_length = max(longest_length, streak);
            }
        }

        return longest_length;
    }
};
