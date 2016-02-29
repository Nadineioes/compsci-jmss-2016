# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

words = []
wordgiven = ''
while wordgiven != 'quit':
    wordgiven = input("word: ")
    if wordgiven != 'quit':
        words.append(wordgiven)

words.sort()
print(words)