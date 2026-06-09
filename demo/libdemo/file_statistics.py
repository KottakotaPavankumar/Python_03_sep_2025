
# Filename suggestion: file_statistics.py

def main():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, "r") as f:
            lines = f.readlines()

        num_lines = len(lines)
        num_chars = 0
        num_words = 0

        for line in lines:
            num_chars += len(line)
            num_words += len(line.split())

        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

if __name__ == "__main__":
    main()


"""
filename = input("Enter filename :")

try:
    f = open(filename, "rt")
    contents = f.read()
    chars = len(contents)
    lines = contents.count('\n')
    words = contents.count(' ') + lines
    print(f'Chars  : {chars:3}')
    print(f'Words  : {words:3}')
    print(f'Lines  : {lines:3}')
    f.close()
except Exception  as ex:
    print('Error : ', ex)
"""