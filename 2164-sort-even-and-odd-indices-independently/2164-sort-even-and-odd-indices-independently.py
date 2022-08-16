class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        list1=nums[::2]
        list2=nums[1::2]
        list1.sort()
        list2.sort(reverse=True)
        list3=[]
        i=0
        while(i<len(nums)):
            if(i<len(list1)):
                list3.append(list1[i])
            if(i<len(list2)):
                list3.append(list2[i])
            i+=1
        return list3
            
        
        
        
        