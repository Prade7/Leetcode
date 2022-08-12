class Solution:
    def defangIPaddr(self, address: str) -> str:
        result=""
        for ele in address:
            if(ele=="."):
                result+="[.]"
            else:
                result+=ele
        return result