class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=set(ransomNote)
        for ele in r:
            if(ele in magazine):
                print(magazine.count(ele)-ransomNote.count(ele))

                if(magazine.count(ele)-ransomNote.count(ele)<0):
                    return False
            else:
                return False
        return True
                