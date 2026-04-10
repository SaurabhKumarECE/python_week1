# -----------------------------------------
# Day 5: File Handling & Exception Handling
# -----------------------------------------

# 1. Write User Input to File
def write_to_file(filename: str):
    """Writes user input to a file"""
    try:
        data = input("Enter text to write into file: ")
        with open(filename, 'w') as f:
            f.write(data)
        print(" Data written successfully.")
    except Exception as e:
        print(" Error writing to file:", e)


# -----------------------------------------
# 2. Read from File
def read_from_file(filename: str):
    """Reads and prints file content"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print("\nFile Content:")
        print(content)
    except FileNotFoundError:
        print(" File not found.")
    except Exception as e:
        print(" Error reading file:", e)


# -----------------------------------------
# 3. Word Count Program
def word_count(filename: str):
    """Counts words in a file"""
    try:
        with open(filename, 'r') as f:
            content = f.read()
        words = content.split()
        print("Total words:", len(words))
    except FileNotFoundError:
        print(" File not found.")


# -----------------------------------------
# 4. Division by Zero Handling
def safe_division():
    """Handles division safely"""
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print(" Cannot divide by zero!")
    except ValueError:
        print(" Invalid input!")


# -----------------------------------------
# 5. Read CSV File
import csv

def read_csv_file(filename: str):
    """Reads CSV file and prints rows"""
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            print("\nCSV Content:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(" CSV file not found.")


# -----------------------------------------
# Main Execution
# -----------------------------------------
if __name__ == "__main__":

    file_name = "sample.txt"
    csv_file = "sample.csv"

    # 1. Write to file
    print("---- Write to File ----")
    write_to_file(file_name)

    # 2. Read from file
    print("\n---- Read from File ----")
    read_from_file(file_name)

    # 3. Word Count
    print("\n---- Word Count ----")
    word_count(file_name)

    # 4. Division Handling
    print("\n---- Safe Division ----")
    safe_division()

    # 5. Read CSV
    print("\n---- Read CSV ----")
    read_csv_file(csv_file)