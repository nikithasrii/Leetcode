class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        v=0
        for i in jewels:
            for j in stones:
                if i==j:
                    v+=1
        return v

        