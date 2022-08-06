class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        order=heights[::]
        
        def merge(order):
            if(len(order)>1):
                left=order[:len(order)//2]
                right=order[len(order)//2:]
                merge(left)
                merge(right)
                i=0
                j=0
                k=0
                
                while(i<len(left) and j<len(right)):
                    if(left[i]<right[j]):
                        order[k]=left[i]
                        i+=1
                    else:
                        order[k]=right[j]
                        j+=1
                    k+=1
                while(i<len(left)):
                    order[k]=left[i]
                    i+=1
                    k+=1
                while(j<len(right)):
                    order[k]=right[j]
                    j+=1
                    k+=1
        merge(order)
        print(order)
        count=0
        # print(heights)
        for ele in range(len(heights)):
            if(heights[ele]!=order[ele]):
                count+=1
                # print(heights[ele],order[ele])
        return count