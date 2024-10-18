class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sett = set()
        maxLen = 0
        l = 0

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+= 1
                
            sett.add(s[r])
            maxLen = max(maxLen, r -l +1)
        print(sett)

        return maxLen

### T(C) O(n)
### S(c) O(n)
