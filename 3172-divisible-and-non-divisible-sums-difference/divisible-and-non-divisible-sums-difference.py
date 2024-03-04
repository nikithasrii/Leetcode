class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        Divisible=0
        NotDivisible=0
        for i in range (1,n+1):
            if i%m==0:
                Divisible+=i
            else:
                NotDivisible+=i
        return  NotDivisible- Divisible


        