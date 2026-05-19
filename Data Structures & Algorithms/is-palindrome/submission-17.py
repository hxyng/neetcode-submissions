class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ", "").lower()
        str_only = []

        for s in string:
            if s.isalnum():
                str_only.append(s)

        return str_only == str_only[::-1]
