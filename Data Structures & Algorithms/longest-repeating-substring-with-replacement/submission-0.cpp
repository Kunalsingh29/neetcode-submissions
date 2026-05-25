class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.size();
        int left = 0, right = 0;
        unordered_map<char, int> freqCount;
        char maxElement;
        int maxCount = 0;
        int maxLength = 0;
        while(right<n){
           
            freqCount[s[right]]++;
        
            maxCount = max(maxCount, freqCount[s[right]]);
        
            while((right-left+1- maxCount)>k && left<n){
                freqCount[s[left]]--;
                left++;
            }

            maxLength = max(maxLength, right-left+1);
            right++;

        }
        return maxLength;
        
    }
};