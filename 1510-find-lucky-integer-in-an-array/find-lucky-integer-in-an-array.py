class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=[]
        for i in arr:
            v=arr.count(i)
            if i==v:
                l.append(i)
            else:
                l.append(-1)
        return max(l)
        