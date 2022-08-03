class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        n=len(timeSeries)
        if(n<=0):
            return 0
        time=0
        for i in range(n-1):
            time+=min(timeSeries[i+1]-timeSeries[i],duration)
            
        return time+duration