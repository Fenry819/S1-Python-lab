#first and last characters exchange
str=input("Enter the string to be swapped: ")
start=str[0]
end=str[-1]
swapped_string=end+str[1:-1]+start
print("swapped_string is: ",swapped_string)