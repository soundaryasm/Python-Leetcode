# -*- coding: utf-8 -*-
# 此题最难的地方不在于算法,而是在于while循环中start 和end的边界条件 - 何时有等号,何时start增加,何时end减少
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end: #
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


if __name__ == '__main__':
    s = Solution()
    #nums =[4, 5, 6, 7, 0, 1, 2]
    nums = [4,5,6,7,0,1,2]
    #nums = [1,3]
    target = 0
    print(s.search(nums,target))
