class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in s:
            if i not in s_map:
                s_map[i] = s.count(i)
        
        for i in t:
            if i not in t_map:
                t_map[i] = t.count(i)

        if s_map == t_map:
            if len(s) != len(t):
                return False
            return True
        else:
            return False