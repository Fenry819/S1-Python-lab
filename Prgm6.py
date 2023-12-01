names=input("Enter the names:")
a_count = 0

for name in names:
    a_count += name.lower().count('a')

print(f"Total occurrences of 'a': {a_count}")