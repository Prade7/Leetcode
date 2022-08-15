class Solution:
    def findMin(self, nums: List[int]) -> int:
#         nums=set(nums)
#         nums=list(nums)
#         print(nums)
#         left=0
#         right=len(nums)-1
#         res=nums[0]
#         while(left<=right):
#             if(nums[left]<nums[right]):
#                 res=min(nums[0],nums[left])
#                 break
#             mid=(left+right)//2
#             res=min(nums[mid],res)
            
#             if(nums[left]<nums[mid]):
#                 left=mid+1
#             else:
#                 right=mid-1
#         return res


        return min(nums)
        
        
        