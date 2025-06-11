x = int(input("Enter the number to get multiplication Table: "))

# method 1
def get_table(x):
    for i in range(1, 11):
        print(f"{x} × {i} = {x * i}",)
        
get_table(x)
    
print('\n')
    
# method 2
def get_table2(x):
    i = 1
    while i <= 10:
        print(f"{x} × {i} = {x * i}")
        i += 1
get_table2(x)
print('\n')
# method 3

print("\n".join([f"{x} × {i} = {x * i}" for i in range(1, 11)]))

print('\n')
# method 4
table3 = "\n".join(map(lambda i: f"{x} ×  {i} = {x * i}", range(1, 11)))
print(table3)
print('\n')

# method 5
def get_table4(x, i=1):
    if i > 10:
        return
    print(f"{x} × {i} = {x * i}")
    get_table4(x, i+1)
get_table4(x)
print('\n')

# method 6

table5 = {i: x * i for i in range(1, 11)}
for i, result in table5.items():
    print(f"{x} × {i} = {result}")
    
print('\n')

# method 7
for index, i in enumerate(range(1, 11), start = 1):
    print(f"{x} × {index} = {x * i}")


