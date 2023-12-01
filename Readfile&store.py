file_path = 'class2.py'
file = open(file_path, 'r')
lines_list = file.readlines()
file.close()

if lines_list:
    for line in lines_list:
        print(line.strip())
else:
    print("No content read from the file.")
