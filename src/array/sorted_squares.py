class SortedSquares:
    """977. 有序数组的平方"""
    @staticmethod
    def array_square(nums):
        start = 0
        end, index = len(nums) - 1, len(nums) - 1
        res = [0] * len(nums)

        while start <= end:
            if nums[start] * nums[start] >= nums[end] * nums[end]:
                res[index] = nums[start] * nums[start]
                start += 1
            else:
                res[index] = nums[end] * nums[end]
                end -= 1
            index -= 1

        return res


if __name__ == "__main__":
    var = [-4,-1,0,3,10]
    print(SortedSquares.array_square(var))
