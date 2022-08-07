class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha="abcdefghijklmnopqrstuvwxyz"
        for ele in alpha:
            if(ele not in sentence):
                return False
        return True