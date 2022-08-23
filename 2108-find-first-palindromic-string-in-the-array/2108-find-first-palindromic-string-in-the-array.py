class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for ele in words:
            if(ele[::]==ele[::-1]):
                return ele
        return ""