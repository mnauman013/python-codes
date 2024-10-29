#To check the number is even or odd by using different methods.
x = int(input("Enter the number to check if it is even or odd: "))
# 1st: Modulus Operator
def check_even_odd(x):
    if x % 2 == 0:
        print(f"The number {x} is even.")
    else:
        print(f"The number {x} is odd.")
        
check_even_odd(x)

#2nd: Bitwise ANd operator
def check_by_bitwise(x):
    if x & 1 == 0:
        print(f"The number {x} is even.")
    else:
        print(f"The number {x} is odd.")
        
check_by_bitwise(x)

#3rd Using Division and Floor check
def check_by_division(x):
    if (x // 2) * 2 == x:
        print(f"The number {x} is even.")
    else:
        print(f"The number {x} is odd.")
        
check_by_division(x)

#4th Using Ternary Conditional Expression
def check_by_ternary(x):
    print(f"The number {x} is {'even' if x % 2 == 0 else 'odd'}.")
check_by_ternary(x)

#5th Using Lambda
check_by_lambda = lambda x: print(f"The number {x} is even.") if x % 2 == 0 else print(f"The number {x} is odd.")
check_by_lambda(x)
    
#6th Recursion method
def check_by_recursion(x):
    if x == 0:
        print(f"The number {x} is even.")
    elif x == 1:
        print(f"The number {x} is odd.")
    else:
        check_by_recursion(x-2)

check_by_recursion(x)
# in method 6th, the output like
# if even " 0 is even"
# if odd " 1 is odd" 
#if want to show the original number to show in output so use this code

#6th updated 
def check_recursive_original(x, original_x = None):
    if original_x is None:
        original_x = x
    if x == 0:
        print(f"The number {original_x} is even.")
    elif x == 1:
        print(f"The number {original_x} is odd.")
    else:
        check_recursive_original(x - 2, original_x)
        
check_recursive_original(x)      