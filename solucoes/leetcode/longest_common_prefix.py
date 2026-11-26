# LeetCode - Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs:
                if i >= len(s) or s[i] != char:
                    return result

            result += char

        return result
