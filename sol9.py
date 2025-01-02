x = 10
def check_num(num):
    string = str(num)
    reversed_string = string[::-1]
    if string == reversed_string :
        return True
    else : 
        return False

print(check_num(x))


