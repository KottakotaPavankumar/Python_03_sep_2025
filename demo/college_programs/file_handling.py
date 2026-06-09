# Writing to a file in "w" mode
with open("output.txt", "w") as file:
    file.write("Hello, this is a line written to the file.")


# Appending to the same file in "a" mode
with open("output.txt", "a") as file:
    file.write("\nThis line is appended to the file.")


# Reading the entire file using .read()
with open("output.txt", "r") as file:
    content = file.read()
print("File content:\n", content)


# Getting the current position using .tell()
with open("output.txt", "r") as file:
    position = file.tell()
print("Current position:", position)


# Seeking to a specific position using .seek()
with open("output.txt", "r") as file:
    file.seek(10)  # Move the pointer to position 10
    seekread = file.read()
print("File data from position 10:", seekread)
file.close()
