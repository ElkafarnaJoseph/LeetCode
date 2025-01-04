num = 123
s_num = str(num)
to_int = int(s_num[:: - 1])
print(to_int)
# ^^ for the positive 

# for negative  >> 
num = -123
s_num = str(num)[1:] # removes the "-"
add_neg = int('-' + s_num[:: - 1]) # put the - back and switch to int and reverse it
print(add_neg)

# the bounds of 32-bits are [-2**31 , 2**31 - 1]

# applying a function
def reverse( x):
    # 32-bit signed integer range check
    if x > (2**31 - 1) or x < -2**31:
        return 0
    
    # Reverse the number
    if x < 0:
        reversed_num = int('-' + str(x)[1:][::-1])
    else:
        reversed_num = int(str(x)[::-1])
    
    # Check if the reversed number is within the 32-bit signed integer range
    if reversed_num > (2**31 - 1) or reversed_num < -2**31:
        return 0

    return reversed_num

print(reverse(1234563789))