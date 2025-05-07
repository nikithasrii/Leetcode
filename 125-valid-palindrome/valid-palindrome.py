class Solution:
    def isPalindrome(self, s: str) -> bool:
        making=''.join(char.lower() for char in s if char.isalnum())
        return making==making[::-1]