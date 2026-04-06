from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs[0]):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    if i == 0:
                        return ""
                    return strs[0][:i]
            i += 1
        
        return strs[0][:i]