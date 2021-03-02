class PlusOne:
    """66. 加一"""
    @staticmethod
    def plus_one(digits):
        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            i -= 1

        return digits
