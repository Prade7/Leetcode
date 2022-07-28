class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxL=[]
        e=0
        leftH=[]
        for ele in height:
            if(ele>e):
                leftH.append(ele)
                e=ele
            else:
                leftH.append(e)
        e=0
        rightH=[]
        for ele in range(len(height)-1,-1,-1):
            if(height[ele]>e):
                rightH.append(height[ele])
                e=height[ele]
            else:
                rightH.append(e)
        rightH=rightH[::-1]
        res=[]
        for ele in range(len(leftH)):
            res.append(min(leftH[ele],rightH[ele]))
        count=0
        for ele in range(len(res)):
            if(res[ele]-height[ele]>0):
                count+=res[ele]-height[ele]
        return count
                
            