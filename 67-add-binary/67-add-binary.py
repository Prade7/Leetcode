class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if(a=="0" and b=="0"):
            return str(0)
        aa=0
        c=0
        for ele in range(len(a)-1,-1,-1): 
            if(ele=="0"):
                c+=1
            if(a[ele]=="1"):
                c+=pow(2,aa)
            aa+=1  
        
        aa=0
        d=0
        for ele in range(len(b)-1,-1,-1): 
            if(ele=="0"):
                d+=1
            if(b[ele]=="1"):
                d+=pow(2,aa)
            aa+=1  
        d+=c
        count=""
        while(True):
            if(d)==2 :
                count+="0"
                count+="1"
                break
            if(d==0):
                count+="0"
                break
            if(d%2!=0):
                count+="1"
                d-=1
                d/=2
            if(d%2==0):
                count+="0"
                d/=2
        
        count=count[::-1]
        for ele in range(len(count)):
            if(count[ele]!="0"):
                return count[ele::]
            