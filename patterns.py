# Different pattern in python

rows = int(input("Enter the number of rows: "))

# Triangle
for i in range(1, rows + 1):
    print( "$ " * i)
print('\n')
    
# inverted triangle
for i in range(rows, 0, -1):
    print("@ " * i)
print('\n')
  
# Pyramids
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
    
print('\n')
#numbers Pyramid or triangle
for i in range(1, rows + 1):
    print(" " * (rows - i) + " ".join(str(j) for j in range(1, i+1)))
print('\n')

# Diamond

for i in range(1, rows + 1):
    print(" " * (rows - i) + "+ " * i)
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "+ " * i)
    
print('\n')

# Pascal triangle

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)
for i in range(rows):
    print(" " * (rows - i), end="")
    for j in range(i + 1):
        value = factorial(i) // (factorial(j)*factorial(i - j))
        print(value, end=" ")
    print()
print('\n')

# hollow square 
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("+ " * rows)  # print line in first and last row
    else:
        print("+ " + "  " * (rows - 2) + "+ ") #print in boundries
        
print("\n")

# consecutive number triangle
a = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(a, end='')
        a +=1
    print()

print('\n')

# butterfly 
for i in range(1, rows + 1):
    print("* " * i + "  " * (rows - i) * 2 + "* " * i)
    
for i in range(rows, 0, -1):
    print("* " * i + "  "* (rows-i)*2+ "* "* i)