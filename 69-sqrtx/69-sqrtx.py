class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start=0
        end=x
        while(start<=end):
            mid=start+(end-start)//2
            if(mid*mid>x):
                end=mid-1
            if(mid*mid<x):
                start=mid+1
            if(mid*mid==x):
                return mid
        return start-1