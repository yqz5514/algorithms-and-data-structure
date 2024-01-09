nums = [3, 2, 4]
target = 6

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         prevMap = {}  # val -> index
#
#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i

#enumerate It first prints tuples of index and element pairs. Then it changes the starting index while printing them together.
# Finally, it prints the index and element separately, each on its own line.
#0 3
# 1 2
# 2 4