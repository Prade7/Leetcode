class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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
        
        # nums[:len(nums)//2]=nums[::2]
        nums[::]=nums[::-1]
        nums[::2],nums[1::2]=nums[(len(nums)//2):],nums[:len(nums)//2]
        
    #      k = len(nums)//2
    # nums.sort(reverse = True)
    # nums[::2], nums[1::2] = nums[k:], nums[:k]