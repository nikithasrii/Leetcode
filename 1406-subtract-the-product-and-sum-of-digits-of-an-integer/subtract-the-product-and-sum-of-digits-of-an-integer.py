class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        m= 1

        while n > 0:
            split = n%10
            s+= split
            m*= split
            n = n//10

        return m-s

        