class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        b=len(nums)-1
        n=nums[::]
        ind1=0
        ind2=0
        nums.sort()
        for i in range(1,len(nums)):
            if(nums[a]+nums[b]==target):
                ind1=nums[a]
                ind2=nums[b]
                break
            elif(nums[a]+nums[b]>target):
                b-=1
            else:
                a+=1
        f=n.index(ind1)
        n[f]="p"
        g=n.index(ind2)
        return f,g
                        
            
        