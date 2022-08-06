class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_dif=arr[1]-arr[0]
        
        res=[[arr[0],arr[1]]]
        
        for i in range(1,len(arr)-1):
            q=[]
            if((arr[i+1]-arr[i])<min_dif):
                min_dif=arr[i+1]-arr[i]
                # q=[arr[i+1],arr[i]]
                # print(arr[i+1]-arr[i])
                res=[]
            if(arr[i+1]-arr[i]==min_dif):
                q=[arr[i],arr[i+1]]
                res.append(q)
        return res