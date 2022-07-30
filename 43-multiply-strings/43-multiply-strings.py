class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dict1={"0":48,"1":49,"2":50,"3":51,"4":52,"5":53,"6":54,"7":55,"8":56,"9":57}
        a=0
        for ele in num1:
            a=a*10+(dict1[ele]-48)
        b=0
        for ele in num2:
            b=b*10+(dict1[ele]-48)
        return str(a*b)
        
