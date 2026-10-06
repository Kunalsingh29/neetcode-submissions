class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = []
        num_palindrome = 0

        for i in range(n):
            l, r = i, i

            while l>=0 and r<n and s[l] == s[r]:
                # fpund a palindrone: when youenter while loop :
                # add to list: 
                num_palindrome += 1
                l = l-1
                r = r+1

            l, r = i, i+1

            while l>=0 and r<n and s[l] == s[r]:
                # fpund a palindrone: when youenter while loop :
                # add to list: 
                #res.append(s[l:r+1])
                num_palindrome += 1
                l = l-1
                r = r+1
                
        return num_palindrome



