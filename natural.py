#to get a natural number
#method 1
print('Natural numbers: ', end='')
def natural(x):
    for i in range(1, x + 1):
        print(i, end=' ')
natural(7)
print('\n')
#method 2
n = int(input("Enter a number to get natural numbers up to: "))
print ("Natural numbers: ", end='')
for i in range(1, n + 1):
    print(i, end=' ')
    
print('\n')

#method 3
print('Natural number:', end='')
i = 1
while i <= n:
    print(i, end=' ')
    i += 1
print('\n')

#method 4
print('Natural numbers: ', end='')
def natural_no(x, y):
    if x > y:
        return
    print(x, end=' ')
    natural_no(x + 1, y)
natural_no(1, n)
print('\n')

#method 5
print('Natural numbers: ', end='')
print(' '.join(str(i) for i in range(1, n + 1)))