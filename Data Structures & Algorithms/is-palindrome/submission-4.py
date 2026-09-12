class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while (right > left):
            leftbool = s[left].isalnum()
            rightbool = s[right].isalnum()
            if (leftbool and rightbool):
                if s[left].lower() != s[right].lower():
                    return False
                left +=1
                right -= 1
            else:
                if not (s[left].isalnum()):
                    left +=1
                if not (s[right].isalnum()):
                    right -=1
        return True
        