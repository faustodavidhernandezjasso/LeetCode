class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # No muy elegante
        # if (len(s) != len(t)):
        #     return False
        # dic = {}
        # for letter in s:
        #     if (dic.get(letter) == None):
        #         dic[letter] = 1
        #     else:
        #         dic[letter] += 1
        # for letter in t:
        #     if (dic.get(letter) == None):
        #         return False
        #     else:
        #         dic[letter] -= 1
        # for val in dic.values():
        #     if (val != 0):
        #         return False
        # return True