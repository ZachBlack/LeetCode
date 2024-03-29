"""
    PROMPT:
            Write a function that reverses a string. The input string is given as an array of characters s.

            You must do this by modifying the input array in-place with O(1) extra memory.
            
            Time Complexity:    O(N)
            Space Complexity:   O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        for i in range(mid):
            temp = s[i]
            s[i] = s[-(i+1)]
            s[-(i+1)] = temp
