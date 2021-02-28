class SumOddLengthSubarrays:
    """1588. 所有奇数长度子数组的和"""
    @staticmethod
    def func1(arr) -> int:
        length = len(arr)
        index = 0
        window = 1
        res = 0
        while window <= (2 * int(length / 2)) + 1:
            while index + window <= length:
                sub_arr = arr[index:index + window]
                res += sum(sub_arr)
                index += 1

            index = 0
            window += 2

        return res

    @staticmethod
    def func2(arr):
        """
        对于一个数字，它所在的数组，可以在它前面再选择 0, 1, 2, ... 个数字，一共有 left = i + 1 个选择；

        可以在它后面再选择 0, 1, 2, ... 个数字，一共有 right = n - i 个选择。

        如果在前面选择了偶数个数字，那么在后面，也必须选择偶数个数字，这样加上它自身，才构成奇数长度的数组；

        如果在前面选择了奇数个数字，那么在后面，也必须选择奇数个数字，这样加上它自身，才构成奇数长度的数组；

        数字前面共有 left 个选择，其中偶数个数字的选择方案有 left_even = (left + 1) / 2 个，奇数个数字的选择方案有 left_odd = left / 2 个；

        数字后面共有 right 个选择，其中偶数个数字的选择方案有 right_even = (right + 1) / 2 个，奇数个数字的选择方案有 right_odd = right / 2 个；

        所以，每个数字一共在 left_even * right_even + left_odd * right_odd 个奇数长度的数组中出现过。
        """
        res = 0
        length = len(arr)
        for i in range(length):
            left = i + 1
            right = length - i
            left_odd, left_even = left // 2, (left + 1) // 2
            right_odd, right_even = right // 2, (right + 1) // 2
            res += arr[i] * (left_odd * right_odd + left_even * right_even)

        return res


if __name__ == "__main__":
    var = [1,4,2,5,3]
    print(SumOddLengthSubarrays.func2(var))
