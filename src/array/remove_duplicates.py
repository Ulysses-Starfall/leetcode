class RemoveDuplicates:
    """26. 删除排序数组中的重复项"""
    @staticmethod
    def remove_duplicates(nums):
        point1, point2 = 0, 1
        n = len(nums)
        while point2 < n:
            if nums[point1] != nums[point2]:
                nums[point1 + 1] = nums[point2]
                point1 += 1

            point2 += 1

        return point1 + 1
