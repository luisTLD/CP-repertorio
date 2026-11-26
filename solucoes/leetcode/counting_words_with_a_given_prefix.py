# LeetCode - Counting Words with a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total = 0
        l = len(pref)

        for word in words:
            if l <= len(word):
                i = 0
                while i < l:
                    if word[i] == pref[i]:
                        i += 1
                    else:
                        break

                if i == l:
                    total += 1

        return total
