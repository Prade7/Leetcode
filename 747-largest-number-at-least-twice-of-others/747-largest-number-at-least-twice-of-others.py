class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        q=nums[::]
        def merge(nums):
            if(len(nums)>1):
                left=nums[:len(nums)//2]
                right=nums[len(nums)//2:]

                merge(left)
                merge(right)
                i=0
                j=0
                k=0
                while(i<len(left) and j<len(right)):
                    if(left[i]<right[j]):
                        nums[k]=left[i]
                        i+=1
                    else:
                        nums[k]=right[j]
                        j+=1
                    k+=1
                while(i<len(left)):
                    nums[k]=left[i]
                    i+=1
                    k+=1
                while(j<len(right)):
                    nums[k]=right[j]
                    j+=1
                    k+=1
        merge(nums)
        print(nums)
        f=nums[-1]
        
        for ele in nums:
            if(ele*2>f and ele!=f):
                return -1
        return q.index(f)