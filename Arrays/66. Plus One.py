def plusOne(self, digits: List[int]) -> List[int]:
    n=len(digits)
    i=n-1
    while i>=0:
        if digits[i]<9:
            digits[i]=digits[i]+1
            return digits
        else:
            digits[i]=0
            carry=1
        i=i-1
    digits.insert(0,1)
    return digits