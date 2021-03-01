class MaxSubArray:
    """[53]最大子序和"""
    @staticmethod
    def func1(nums):
        """贪心算法1"""
        tmp_max = 0
        ret = nums[0]
        for i in nums:
            tmp_max = max(i, i + tmp_max)
            ret = max(ret, tmp_max)

        return ret

    @staticmethod
    def func2(nums):
        """动态规划"""
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)

    @staticmethod
    def func3(nums):
        """贪心算法2"""
        tmp_max = 0
        ret = nums[0]
        for i in nums:
            if tmp_max > 0:
                tmp_max += i
            else:
                tmp_max = i
            ret = max(tmp_max, ret)

        return ret


if __name__ == "__main__":
    print(MaxSubArray.func3([-2,1,-3,4,-1,2,1,-5,4]))
