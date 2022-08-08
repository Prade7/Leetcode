class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        total_count=[]
        for  ele in mat:
            total_count.append(ele.count(1))
        print(total_count)
        minx=[]
        for ele in range(k):
            m=min(total_count)
            m=total_count.index(m)
            minx.append(m)
            total_count[m]=99999
            # print(total_count)
        return (minx)
            
            