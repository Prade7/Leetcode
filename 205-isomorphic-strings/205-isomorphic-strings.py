class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
#         hm={}
        
#         for i in (s):
#             if(i not in hm):
#                 hm[i]=1
#             else:
#                 hm[i]+=1
#         hm=list(hm.values())
#         hm.sort()
#         print(hm)
#         hm2={}
#         for i in t:
#             if(i not in hm2):
#                 hm2[i]=1
#             else:
#                 hm2[i]+=1
                
#         hm2=list(hm2.values())
#         hm2.sort()
#         if(hm==hm2):
#             return True
#         else:
#             return False

        return len(set(s))==len(set(t))==len(set(zip(s,t)))