# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read

numbers = []
num = 0
while num != -1:
    num = input('number: ')
    num = int(num)
    if num != -1:
        numbers.append(num)
sum = sum(numbers)
print(sum)