class RemoveElement:
    @staticmethod
    def remove_element(nums, val):
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

    @staticmethod
    def remove_element1(nums, val):
        a = 0
        b = 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b


if __name__ == "__main__":
    print(RemoveElement.remove_element([0,1,2,2,3,0,4,2], 3))
