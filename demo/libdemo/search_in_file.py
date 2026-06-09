#Accept file name and search string from the user
file_name = input("Enter the file name: ")

search_string = input("Enter the string to search for:")

try:
    with open(file_name,"r")as f:
        lines = f.readlines()
    found = False
    for line_number,line in enumerate (lines,start=1):
        if search_string in line:
            print(f"string found in line {line_number}:{line.strip()}")
            found = True
    if not found :
        print("string not found in the file.")
except  FileNotFoundError:
            print(f"File'{file_name}' not found")


"""
filename = input("Enter filename :")

try:
    f = open(filename, "rt")
    search_string = input("Enter search string :")

    for lineno, line in enumerate(f.readlines(), start = 1):
        if search_string in line:
            print(f'Found at {lineno}')
            break
    else:
        print('Sorry! Not found!')

    f.close()
except Exception  as ex:
    print('Error : ', ex)
"""