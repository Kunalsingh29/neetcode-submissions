class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        res = ""
        maxLen = 0
        if n ==1:
            return s

        for i in range(n):
            l, r = i, i

            while(l>=0 and r<n and s[l] == s[r]):
                # expamd left right:
                if(r-l+1) > maxLen:
                    res = s[l:r+1]
                    maxLen = r-l+1
                l = l-1
                r = r+1
            
            l, r = i, i+1
            while(l>=0 and r<n and s[l] == s[r]):
                # expamd left right:
                if(r-l+1) > maxLen:
                    res = s[l:r+1]
                    maxLen = r-l+1
                l = l-1
                r = r+1
            
        return res
