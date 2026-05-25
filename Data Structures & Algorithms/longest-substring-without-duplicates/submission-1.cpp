class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int maxLength = 0;
        int length = 0;
        int n = s.size();
        int left = 0, right = 0;
        unordered_map<char, int> freqCount;
        
        // traverse the string using right; 
        // track duplicate using left pointer until duplicate is removed. 
        // how to check duplicate? check if the frequency of element is right is >1; 
        // if >1, that means this element is present twice. remove elements until this is 1. 
        while(right<n){
            freqCount[s[right]]++;
            
            while(freqCount[s[right]]>1){
                char lchar = s[left];
                freqCount[lchar]--;
                left++;
            }

            maxLength = max(maxLength, right-left+1);
            right++;
        }
        return maxLength;


    }
    
};