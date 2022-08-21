class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        
        for ele in nums:
            result.append(ele*ele)
        print(result)
        
        def merge(result):
            if(len(result)>1):
                left=result[:len(result)//2]
                right=result[len(result)//2:]
                merge(left)
                merge(right)
                i=0
                j=0
                k=0
                while(i<len(left) and j<len(right)):
                    if(left[i]<right[j]):
                        result[k]=left[i]
                        i+=1
                        k+=1
                    else:
                        result[k]=right[j]
                        j+=1
                        k+=1
                while(i<len(left)):
                    result[k]=left[i]
                    i+=1
                    k+=1
                while(j<len(right)):
                    result[k]=right[j]
                    j+=1
                    k+=1
        merge(result)
        
        return result
        
        
        
        
        