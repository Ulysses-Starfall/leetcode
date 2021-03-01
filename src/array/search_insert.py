class SearchInsert:
    """[35]搜索插入位置"""
    @staticmethod
    def search_insert(nums, target):
        n = len(nums)
        j = 0
        while j < n:
            if nums[j] == target or nums[j] > target:
                return j
            j += 1

        return j

    @staticmethod
    def search_insert2(nums, target):
        right = len(nums) - 1  # 注意
        left = 0
        while left <= right:  # 注意
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1  # 注意
            else:
                right = middle - 1  # 注意

        return left


if __name__ == "__main__":
    print(SearchInsert.search_insert2([1,3,5,6], 5))
