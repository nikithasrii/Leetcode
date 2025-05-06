class Solution:
    def maxProduct(self, n: int) -> int:
        digits = list(map(int, str(n)))  
        return max(a * b for a, b in combinations(digits, 2))
        
        