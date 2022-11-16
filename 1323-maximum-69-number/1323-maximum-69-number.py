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
        return max(result_list)
        
           