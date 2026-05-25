class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        //unordered_map<unordered_map<char, int>, vector<string>> AnagramList;
        // sorting each string and addind coresponding string to result;
        unordered_map<string, vector<string>> stringMap;
        for(string s:strs){
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            stringMap[sortedS].push_back(s);
        }
        vector<vector<string>> output;
       
        for(const auto&pair:stringMap){
            output.push_back(pair.second);
        }
        return output;
        
    }
};