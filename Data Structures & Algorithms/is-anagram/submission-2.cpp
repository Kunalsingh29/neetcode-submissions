class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        unordered_map<char, int> count_s;
        unordered_map<char, int> count_ts;
        for(int i = 0; i<s.length(); i++){
            count_s[s[i]]++;

        }
        for(int i = 0; i<t.length(); i++){
            count_ts[t[i]]++;

        }
        for(int i = 0; i<s.length(); i++){
            if(count_s[s[i]]!= count_ts[s[i]]){
                return false;
            }
            

        }
        return true;



        
    }
};