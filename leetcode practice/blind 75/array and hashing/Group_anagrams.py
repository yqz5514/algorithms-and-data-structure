strs = ["eat","tea","tan","ate","nat","bat"]

#Defaultdict is a container like dictionaries present in the module collections. Defaultdict
# is a sub-class of the dictionary class that returns a dictionary-like object.
# The functionality of both dictionaries and defaultdict are almost same except for the
# fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()


class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word)) #anagram key
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())

# anagram_map = defaultdict(list)
# print(anagram_map)
# for word in strs:
#     print('word:', word)
#     sorted_word = ''.join(sorted(word))
#     print('sorted word:',sorted_word)
#     anagram_map[sorted_word].append(word)
#     print('anagram_map:', list(anagram_map.values()))
#     print(anagram_map)

# word: eat
# sorted word: aet
# anagram_map: [['eat']]
# defaultdict(<class 'list'>, {'aet': ['eat']})
# word: tea
# sorted word: aet
# anagram_map: [['eat', 'tea']]
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea']})
# word: tan
# sorted word: ant
# anagram_map: [['eat', 'tea'], ['tan']]
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea'], 'ant': ['tan']})
# word: ate
# sorted word: aet
# anagram_map: [['eat', 'tea', 'ate'], ['tan']]
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan']})
# word: nat
# sorted word: ant
# anagram_map: [['eat', 'tea', 'ate'], ['tan', 'nat']]
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat']})
# word: bat
# sorted word: abt
# anagram_map: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})