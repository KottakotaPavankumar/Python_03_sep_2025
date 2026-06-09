"""
# Filename: calculate_student_totals_averages.py

def main():
    try:
        with open("marks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                parts = line.split(",")
                name = parts[0]
                marks_str = parts[1:]

                try:
                    marks = list(map(int, marks_str))
                except ValueError:
                    print(f"Error: Non-integer marks found for student '{name}'. Skipping.")
                    continue

                if not marks:
                    print(f"Warning: No marks found for student '{name}'. Skipping.")
                    continue

                total = sum(marks)
                average = total / len(marks)

                print(f"Student: {name} | Total Marks: {total} | Average Marks: {average:.2f}")

    except FileNotFoundError:
        print("Error: 'marks.txt' file not found.")

if __name__ == "__main__":
    main()
"""


f = open("marks.txt" , "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue  # Ignore line and go top

    name = parts[0]
    # Remove parts that are not numbers
    numbers = filter(str.isdigit, parts[1:])
    # Convert all parts to int
    marks = list(map(int, numbers))
    total = sum(marks)
    print(f"{name:20}  {total:3} {total//len(marks):2}")


f.close()
