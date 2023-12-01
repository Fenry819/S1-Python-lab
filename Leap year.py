current=int(input("Enter the current year:"))
final=int(input("Enter the final year:"))
print("List of leap years:")
for year in range(current,final):
    if(year%4==0) and (year%100!=0) or (year%400==0):
        print(year)

