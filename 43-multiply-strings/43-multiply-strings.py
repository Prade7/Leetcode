class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a=0
        for ele in num1:
            a=a*10+(ord(ele)-48)
        b=0
        for ele in num2:
            b=b*10+(ord(ele)-48)
        return str(a*b)