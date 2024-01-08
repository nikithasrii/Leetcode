class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        if x<0:
            return False
        else:
            ans=0
            i=0
            d=0
            while(temp):
                temp=temp//10
                d+=1
            temp=x
            d=d-1
            while(temp):
                ans+=(temp%10)*pow(10,d)
                temp=temp//10
                d=d-1
            print(ans)
            return ans==x