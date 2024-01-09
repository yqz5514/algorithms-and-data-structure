#nums = [1, 2, 3, 4]
# nums = [1,2,3,4]
nums = [1,2,3,4,1,2,3,6]
#nums = [1,1,1,3,3,4,3,2,4,2]

#brute force
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
# #This line defines a method named containsDuplicate.
# # self refers to the instance of the Solution class on which this method is called.
# # nums: list[int] is a type-annotated parameter indicating that nums is expected to be a list of integers.
# # -> bool is a type hint specifying that the method returns a boolean value, either True or False
# #
#         '''
#         a Python class named Solution, which contains a single method called containsDuplicate.
#         This method checks if a list of integers, nums, contains any duplicate numbers.
#         '''
#         n = len(nums)
#         for i in range(n - 1): # i = 0,1,2
#             for j in range(i + 1, n): # j repersents the location of the rest of numbers except nums[i]
#                 if nums[i] == nums[j]:
#                     return True
#         return False
# print(Solution().containsDuplicate(nums))



# Solution.containsDuplicate(nums) encountered error, but Solution() works


#sorting
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


#hashset
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False