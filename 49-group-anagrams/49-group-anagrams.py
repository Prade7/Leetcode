class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict1={}
        for ele in strs:
            d=(" ".join(sorted(ele)))
            if(d not in dict1):
                dict1[d]=[]
            dict1[d].append(ele)
        return (dict1.values())        
                
        