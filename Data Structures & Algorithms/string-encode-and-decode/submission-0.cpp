class Solution {
public:


    string encode(vector<string>& strs) {
        string str = "";
        for( string s:strs){
            //string s_temp = "";
            str+=(to_string(s.size()) + "^" + s);

        }
        return str;


    }

    vector<string> decode(string s) {
        int len = s.size();
        vector<string> result; // dynamic size. not fixed here.
        int i = 0;
        while(i<len){
            int j = i;
            while(s[j] != '^') j++;
            int temp_len = stoi(s.substr(i, j-i));
            string temp_str = s.substr(j+1, temp_len);
            result.push_back(temp_str);
            i = j+temp_len + 1;

        }
        return result;

    }
};
