class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1[len(nums1):]=nums2[::]
        
        def merge(nums1):
            if(len(nums1)>1):
                left=nums1[len(nums1)//2:]
                right=nums1[:len(nums1)//2]
                merge(left)
                merge(right)
                i=0
                j=0
                k=0
                
                while(i<len(left) and j<len(right)):
                    if(left[i]<right[j]):
                        nums1[k]=left[i]
                        i+=1
                        k+=1
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
        merge(nums1)
       
        print(nums1)
        if(len(nums1)%2!=0):
            return float(nums1[(len(nums1)//2)])
        else:
            return (nums1[(len(nums1)//2)-1]+nums1[len(nums1)//2])/2
        