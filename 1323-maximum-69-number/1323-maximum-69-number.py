class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num=str(num)
        result_list=[]
        # temp=""
        # c=0
        # for index,item in enumerate(str_num):
        
        while(True):
            temp=""
            c=0
            for ele in str_num:
                if(ele=="6" and c==0):
                    temp+="9"
                    c=1
                else:
                    temp+=ele
            result_list.append(int(temp))
            if(len(result_list)==len(str_num)):
                break
        print(result_list)
        
        def merge_sort(result_list):
            if(len(result_list)>1):
                left=result_list[:len(result_list)//2]
                right=result_list[len(result_list)//2:]
                merge_sort(left)
                merge_sort(right)
                
                i=0
                j=0
                k=0
                while(i<len(left) and j<len(right)):
                    if(left[i]<right[j]):
                        result_list[k]=left[i]
                        i+=1
                    else:
                        result_list[k]=right[j]
                        j+=1
                    k+=1
                while(i<len(left)):
                    result_list[k]=left[i]
                    i+=1
                    k+=1
                while(j<len(right)):
                    result_list[k]=right[j]
                    j+=1
                    k+=1
            return result_list[-1]
        return merge_sort(result_list)
                
               
        # return max(result_list)
        
           