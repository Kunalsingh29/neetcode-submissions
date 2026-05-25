class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int size = s.size();
        int length = 0;
        int temp_length = 0;
        int left = 0, right = 0;
        //set<char> unique_char;
        unordered_map< char, int> unique_char;
        while(right<s.length()){
            unique_char[s[right]]++;
            while(unique_char[s[right]]>1){
                char l = s[left];
                unique_char[l]--;
                left++;
            }
            length = max(length, (right-left+1));
            right++;
            
        }
        
        return length;
    }
};