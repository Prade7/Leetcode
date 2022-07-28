class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        if(x<0):
            return False
        if(x==x[::-1]):
            return True