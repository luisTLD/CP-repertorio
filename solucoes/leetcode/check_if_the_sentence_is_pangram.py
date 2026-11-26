# LeetCode - Check if the Sentence Is Pangram
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = set()
        for c in sentence:
            pangram.add(c)
            if len(pangram) == 26:
                return True
        return False
