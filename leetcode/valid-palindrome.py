class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = []
        for ch in s:
            if ch.isalnum():
                new.append(ch.lower())
        return new == new[::-1]