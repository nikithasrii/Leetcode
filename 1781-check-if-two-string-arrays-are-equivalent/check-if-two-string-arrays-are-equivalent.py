class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n="".join(word1)
        m="".join(word2)
        if n==m:
            return True
        else:
            return False