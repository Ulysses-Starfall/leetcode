class MajorityElement:
    """面试题 17.10. 主要元素"""
    @staticmethod
    def func2(nums):
        """摩尔投票法"""
        major = 0
        cnt = 0
        for i in nums:
            if cnt == 0:
                major = i

            if i == major:
                cnt += 1
            else:
                cnt -= 1

        if cnt > 0:
            major_cnt = 0
            for i in nums:
                if i == major:
                    major_cnt += 1
            if major_cnt > len(nums) / 2:
                return major

        return -1
