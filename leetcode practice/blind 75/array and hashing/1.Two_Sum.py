nums = [3, 2, 4]
target = 6

 # class Solution:
 #    def twoSum(self, nums: list[int], target: int) -> list[int]:
 #        prevMap = {}  # val -> index
 #
 #        for i, n in enumerate(nums): # assign index for nums
 #            diff = target - n
 #            if diff in prevMap:
 #                return [prevMap[diff], i] # return indices of the two numbers such that they add up to target
 #            prevMap[n] = i # add numbers to dictionary if diff not fount in nums


# prevMap = {}  # val -> index
#
# for i, n in enumerate(nums):
#     diff = target - n
#     if diff in prevMap:
#         print('content in prevMap')
#         print([prevMap[diff], i])
#     prevMap[n] = i # if not in
#     print('prevMap:')
#     print(prevMap)
#enumerate It first prints tuples of index and element pairs. Then it changes the starting index while printing them together.
# Finally, it prints the index and element separately, each on its own line.
#0 3
# 1 2
# 2 4
# why this does not work
# prevMap = []
# # other ideas
# for i in range(len(nums)):
#     diff = target - nums[i]
#     if diff in prevMap:
#         print(prevMap[diff], i)
#     prevMap.append(nums[i])