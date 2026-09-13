class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in contains:
                contains.remove(s[l])
                l += 1
            contains.add(s[r])
            res = max(len(contains), res)
        return res