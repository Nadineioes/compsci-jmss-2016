notNum=True
while notNum:
    try:
        x = input("Please enter a whole number")

        x = int(x)
        notNum = False
    except ValueError:
        print("hey! Doofus! I asked for an integar!! Not a ",x)
print("x is",x)
