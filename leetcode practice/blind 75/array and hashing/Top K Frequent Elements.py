nums = [1,1,1,2,2,3]
k = 2

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
#
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)
#
#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
#
#         # O(n)


count = {}
freq = [[] for i in range(len(nums) + 1)]
#print('freq:', freq)
for n in nums:
    count[n] = 1 + count.get(n, 0)
    #print('count[n]:', count[n],n)
for n, c in count.items():
    #print('count.item:',n,c)
    freq[c].append(n)
    #print('freq:',freq)

res = []
for i in range(len(freq) - 1, 0, -1):
    #print('range:',i)
    for n in freq[i]:
        #print('freq[i]:',freq[i])
        res.append(n)
        #print('res:',res)
        if len(res) == k:
           print(res)