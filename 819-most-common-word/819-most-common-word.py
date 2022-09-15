class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         para=""
#         for ele in paragraph:
#             if(ele.isalpha() or ele==" "):
#                 para+=ele
            
#         para=para.split()
#         print(para)
#         paragraph=[]
        
#         for ele in para:
#             if(ele.lower() in banned):
#                 continue
#             paragraph.append(ele.lower())
#         print(paragraph)
#         hm={}
#         for ele in paragraph:
#             if(ele not in hm):
#                 hm[ele]=1
#             else:
#                 hm[ele]+=1
#         print(hm)
#         max_val=max(hm.values())
#         for ele,index in hm.items():
#             if(index==max_val):
#                 return ele

        punct=["!","?",",",";",".","'"]
        p=""
        for ele in paragraph:
            if(ele in punct):
                p+=" "
            else:
                p+=ele
        # print(p)
        p=p.split()
        # print(p)
        para=[]
        ban=[]
        for ele in banned:
            ban.append(ele.lower())
        for ele in p:
            if(ele.lower() in ban):
                continue
            para.append(ele.lower())
        # print(para)
        hm={}
        for ele in para:
            if(ele not in hm):
                hm[ele]=1
            else:
                hm[ele]+=1
        
        print(hm)
        para_max=max(list(hm.values()))
        print(para_max)
        for items,index in hm.items():
            if(index==para_max):
                return items
        
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        