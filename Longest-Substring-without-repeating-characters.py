"""
- Longest Substring without repeating characters.

- Solution 1: sliding window:
    - using defaultdict - check char[i] in dict ? -> up left +1 : i + 1
    -Complexity: 
        +Time complexity : O(N);
        +Space complexity : O(26)(characters in the english alpha) -> O(1)
"""
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex = defaultdict(lambda : -1)
        l = 0
        ansSize = 0
        for r, ch in enumerate(s):
            if  lastIndex[ch] >= l:
                l = lastIndex[ch]+1
            lastIndex[ch] = r
            windSize = r - l +1
            if windSize > ansSize:
                ansSize = windSize
        return ansSize
