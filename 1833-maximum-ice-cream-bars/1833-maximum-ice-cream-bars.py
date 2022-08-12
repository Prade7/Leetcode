class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for ele in costs:
            if(coins-ele>=0):
                coins-=ele
                print(coins)
                c+=1
                print(c)
            else:
                return c
        return c
                