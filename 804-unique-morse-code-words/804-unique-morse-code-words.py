class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hm={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        # print(hm["g"]+hm["i"]+hm["n"])
        
        res=[]
        for ele in words:
            h=""
            for i in ele:
                print(hm[i])
                h+=hm[i]
            res.append(h)
        
        res=set(res)
        return len(res)
