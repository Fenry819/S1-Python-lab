num_rows = 5

for i in range(num_rows):

    for j in range(i + 1):
        print("*", end=" ")

    print()

for i in range(num_rows - 1, 0,-1):
    for j in range(i):
        print("*", end=" ")
    print()