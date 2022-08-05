class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2
        
        def sort(nums1):
            if(len(nums1)>1):
                left=nums1[:len(nums1)//2]
                right=nums1[len(nums1)//2:]
                i=0
                j=0
                k=0
                sort(left)
                sort(right)
                while(i<len(left) and j<len(right)):
                    if(left[i]<right[j]):
                        nums1[k]=left[i]
                        i+=1
                    else:
                        nums1[k]=right[j]
                        j+=1
                    k+=1
                while(i<len(left)):
                    nums1[k]=left[i]
                    i+=1
                    k+=1
                while(j<len(right)):
                    nums1[k]=right[j]
                    j+=1
                    k+=1
                
        return sort(nums1)
        
        
    
        
        
        
        