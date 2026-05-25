class Solution {
public:


    string encode(vector<string>& strs) {
        string encoded = "";
        for( string word:strs){
            //string s_temp = "";
            encoded+=(to_string(word.size()) + "#" + word);

        }
        return encoded;


    }

    vector<string> decode(string s) {
        int string_length = s.size();
        vector<string> result; // dynamic size. not fixed here.
        int i = 0;
        while(i<string_length){
            int delimiter_pos = i;
            while(s[delimiter_pos] != '#') delimiter_pos++;
            int word_len = stoi(s.substr(i, delimiter_pos-i));// reach the position from i up until delimiter, gets the length.
            string word = s.substr(delimiter_pos+1, word_len);
            result.push_back(word);
            i = delimiter_pos + word_len + 1;

        }
        return result;

    }
};
