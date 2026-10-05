class Solution:
    def count_char(self, string):
        s = {}
        for char in string:
            if char not in s:
                s[char] = 1
            else:
                s[char] += 1
        return s

    def isAnagram(self, s, t):
        if self.count_char(s) == self.count_char(t):
            return True
        else:
            return False

        