file1=open('jesko.txt','r')
file2=open('jesko2.txt','w')

lines=file1.readlines()
for i in range(len(lines)):
    if i%2!=0:
        file2.write(lines[i])

file1.close()
file2.close()
file3=open('jesko2.txt','r')
x=file3.read()
print(x)
file3.close()
