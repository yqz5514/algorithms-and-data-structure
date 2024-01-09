s = "anagram"
t = "nagaram"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
#- . get(s[i], 0): if s[i] is not in the hashmap yet, assign default value which is 0 to this  item.
#- build in function : Counter(s) == Counter(t)
#- how to do O(1) instead O(s+t) : sorting