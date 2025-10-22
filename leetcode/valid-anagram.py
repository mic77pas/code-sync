class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hashmap1 = {}
        hashmap2 = {}
        
        for ch in s:
            hashmap1[ch] = hashmap1.get(ch, 0) + 1
        for ch in t:
            hashmap2[ch] = hashmap2.get(ch, 0) + 1

        return hashmap1 == hashmap2