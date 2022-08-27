class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        
        for ele in range(len(word)):
            if(word[ele]==ch):
                return word[0:ele+1][::-1]+word[ele+1:]
        return word