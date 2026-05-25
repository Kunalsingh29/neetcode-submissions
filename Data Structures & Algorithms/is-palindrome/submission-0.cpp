class Solution {
public:
    bool isPalindrome(string s) {
        
        //string s_lower = std::toLowerCase(s);
        int s_size = s.size();
        int low = 0;
        int high = s_size - 1;
        if(s.empty()){
            return true;
        }
        while(high>=low){

            if(!isalnum(s[high])){
                high--;
                continue;
            }
            if(!isalnum(s[low])){
                low++;
                continue;
            }
            if(tolower(s[high])!=tolower(s[low])){
                return false;
                // high--;
                // low++;  
            }

            high--;
            low++;  
        }
        return true;
    }
};