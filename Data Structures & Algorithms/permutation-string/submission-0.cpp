class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        vector<int> s1_freq(26, 0), s2_freq(26, 0);
        for (char c : s1) s1_freq[c - 'a']++;

        int windowSize = s1.size();
        for (int i = 0; i < s2.size(); i++) {
            s2_freq[s2[i] - 'a']++;

            // Maintain the window size
            if (i >= windowSize) {
                s2_freq[s2[i - windowSize] - 'a']--;
            }

            if (s1_freq == s2_freq) return true;
        }

        return false;
    }
};
