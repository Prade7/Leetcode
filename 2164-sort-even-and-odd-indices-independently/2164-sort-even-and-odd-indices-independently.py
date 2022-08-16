class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        list1=nums[::2]
        list2=nums[1::2]
        
        
        list1.sort()
        list2.sort(reverse=True)
        
        print(list1)
        print(list2)
        list3=[]
        i=0
        n=0
        if(len(list1)>len(list2)):
            n=len(list1)
        else:
            n=len(list2)
        while(i<n):
            if(i<len(list1)):
                list3.append(list1[i])
            if(i<len(list2)):
                list3.append(list2[i])
            i+=1
        print(list3)  
        return list3
            
        
        
        
        