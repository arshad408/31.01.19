fname = input("Enter file name: ")
num = 0
with open(fname, 'r') as a:
    for line in a:
        num += 1
print("Number of lines:")
print(num)
