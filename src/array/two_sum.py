class TwoSum:
    """1.两数之和"""
    @staticmethod
    def two_sum(nums, target):
        """列表搜索"""
        for index, value in enumerate(nums):
            tmp = nums[:index]
            if target - nums[index] in tmp:
                return [index, tmp.index(target - nums[index])]
        return []

    @staticmethod
    def two_sum_2(nums, target):
        """字典搜索"""
        hashmap = dict()
        for index, value in enumerate(nums):
            if hashmap.get(target - nums[index], None) is not None:
                return [index, hashmap[target - nums[index]]]
            hashmap[value] = index


if __name__ == "__main__":
    var = [3, 3]
    print(TwoSum.two_sum(var, 6))
