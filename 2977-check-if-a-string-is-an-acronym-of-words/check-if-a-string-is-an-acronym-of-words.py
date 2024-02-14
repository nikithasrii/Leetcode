class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n=[]
        for i in words:
            n.append(i[0])
        n="".join(n)
        if n==s:
            return True
        else:
            return False
            