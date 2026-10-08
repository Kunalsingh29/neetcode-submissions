from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        n = len(s)

        @cache
        def dfs(idx):
            left, right = 0, 0
            if idx == n:
                return 1
            if s[idx] == "0":
                return 0
            if 1 <= int(s[idx]) <= 9:
                left = dfs(idx + 1)
            if idx + 2 <= n and 10 <= int(s[idx:idx+2]) <= 26:
                right = dfs(idx + 2)
            return left + right

        return dfs(0)