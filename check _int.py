#To check status of integer with differnt methods
#Take the input from user
a = int(input("Enter the 1st integer (a): "))
b = int(input("Enter the 2nd integer (b): "))
# .strip() remove the spaces and .lower() means if user accidently write 'true', 'TRUE', 'True' , this will return only "True"
flag = input("Enter the flag(Either True or False): ").strip().lower() == "true"
# 1st method
def check_1st(a, b, flag):
    if (a >= 0) != (b >= 0) and not flag:
        return True
    elif a < 0 and b < 0 and flag:
        return True
    else:
        return False
print(check_1st(a, b, flag))
    
#2nd method

def check_2nd(a, b, flag):
    return True if((a >= 0) != (b >= 0) and not flag) or (a < 0 and b < 0 and flag) else False
print(check_2nd(a, b, flag))

#3rd method
check_3rd = lambda a, b, flag: ((a >= 0) != (b >= 0) and not flag) or (a < 0 and b < 0 and flag)
print(check_3rd(a, b, flag))

#4th method
def check_4th(a, b, flag):
    condition_1 = (a >= 0 and b < 0 or a < 0 and b >= 0 and not flag)
    condition_2 = a < 0 and b < 0 and flag
    return condition_1 or condition_2
print(check_4th(a, b, flag))

#5th method
def check_5th(a, b, flag):
    if ((a >= 0) ^ (b >= 0) and not flag):
        return True
    elif a < 0 and b < 0 and flag:
        return True
    else:
        False
print(check_5th(a, b, flag))

#6th method
import numpy as np
def check_6th(a, b, flag):
    if np.logical_xor(a >= 0, b >= 0) and not flag:
        return True
    elif a < 0 and b < 0 and flag:
        return True
    else:
        return False
    
print(check_6th(a, b, flag))