# 1
a: int = int(input("Enter a number: "))
a_1 = (a - 10) if a > 10 else (a * 10)
print(a_1)

# 2
b: int = int(input("Enter a number 'b': "))
c: int = int(input("Enter a number 'c': "))
d: int = int(input("Enter a number 'd': "))
sum_bcd: int = b + c + d
b_1 = sum_bcd if sum_bcd > 100 else "The sum is lower than 100"
print(b_1)

# 4
age: int = int(input("Enter your age: "))
age_1 = age if 0 < age < 120 else "The age is not acceptable"
print(age_1)

# 5
g: int = int(input("Enter a 3 digit number: "))
g_1 = (g // 10) % 10 if 100 < g < 1000 else "This number is illegal "
print(g_1)

# 6
n: int = int(input("Enter a number: "))
for n in range(n, 0, -1):
    print(n, end=" ")
print()

# 7
x: int = int(input("Enter the first number: "))
y: int = int(input("Enter the second number: "))
for i in range(x, y + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 8
n: int = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, end=" ")
    elif i % 5 == 0:
        print(i, end=" ")
print()

# 9
n: int = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()

# 11
sum_of_neg: int = 0
while True:
    n: int = int(input("Enter a number: "))
    if n == 0:
        break
    if n < 0:
        sum_of_neg += n
print(sum_of_neg)

# 12
list1: list[int] = []
for i in range(10):
    x: int = int(input("Enter a number: "))
    list1.append(x)
print(list1[::-1])

# 13
counter: int = 0
while True:
    y: int = int(input("Enter a number: "))
    if y == 0:
        break
    if y < 0 or y == 1:
        continue
    else:
        divider: int = 2
        while divider < y:
            if y % divider == 0:
                break
            divider += 1
        if divider == y:
            counter += 1

print(counter)

# 14
numbers: list[int] = []
for i in range(5):
    z: int = int(input("Enter a number: "))
    numbers.append(z)
avg_num: float = sum(numbers) / len(numbers)
above_avg: int = 0
for i in range(len(numbers)):
    if numbers[i] > avg_num:
        above_avg += 1
print(f"The average of numbers is {avg_num:.2f}")
print(f"{above_avg} numbers that are above average")

# 15
x: int = int(input("Enter the first number: "))
y: int = int(input("Enter the second number: "))
counter: int = 0
if y != 0:
    while x >= y:
        x -= y
        counter += 1
    print(f"The result of dividing is {counter}")
else:
    print("You cannot divide by zero")

# 16
number: int = int(input("Enter a 3 digit number: "))
save: int = number
sum_numbers: int = 0
while number > 0:
    units = number % 10
    sum_numbers += units
    number = number // 10
    print(f"{units} {"+" if number > 0 else "="}", end=" ")
if sum_numbers % 3 == 0:
    print(f"{sum_numbers} Divisible by 3")
else:
    print(f"{sum_numbers} Is not divisible by 3")
