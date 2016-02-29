# write a program that reads in 10 numbers, then prints the sum of those

num = ''
numbers = []
for i in range(10):
    num = input('Number: ')
    num = int(num)
    numbers.append(num)
sum = sum(numbers)
print(sum)