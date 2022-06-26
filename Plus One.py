from string import digits


digits = [1,2,3]

def plusOne(self, digits):
    digit_len = len(digits)
    # print(digit_len)
    for i in reversed(range(digit_len)):
        digits[i] +=1
        if digits[i] < 10 :
            # print(digits)
            return digits
            # print(digits)
        else:
            digits[i] = 0
    if digits[i] == 0:        
        digits.insert(0,1)
    # return digits
    # print(digits)
    return digits
        
    