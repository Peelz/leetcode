class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        collector = {}
        start = 0
        ans = 0
        # for i, c in enumerate(s):
        for i in range(len(s)):
            c = s[i]
            if c in collector and collector[c] >= start:
                start = collector[c] + 1
            else:
                ans = max(ans, i - start + 1)
            collector[c] = i
        return ans
