class Merge:
    """88. 合并两个有序数组"""
    @staticmethod
    def merge1(nums1, m, nums2, n):
        """合并后排序"""
        nums1[m:m + n] = nums2
        return nums1.sort()

    @staticmethod
    def merge2(nums1, m, nums2, n):
        """双指针法"""
        nums1_cp = nums1[:m]
        nums1[:] = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1_cp[i] > nums2[j]:
                nums1.append(nums2[j])
                j += 1
            else:
                nums1.append(nums1_cp[i])
                i += 1

        if i < m:
            nums1[i + j:] = nums1_cp[i:]
        if j < n:
            nums1[i + j:] = nums2[j:]
