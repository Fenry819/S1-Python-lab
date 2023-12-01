list=list(range(1000,10000))
for i in list:
    if all(int(digit)%2==0 for digit in str(i)):
print(list)