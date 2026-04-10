# 1. Sum of List Elements
print("---- 1. Sum of List Elements ----")

numbers = list(map(int, input("Enter numbers (space separated): ").split()))

total = 0
for num in numbers:
    total += num

print("Sum of elements:", total)



# 2. Max & Min in List
print("\n---- 2. Max & Min in List ----")

max_val = numbers[0]   # using indexing
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Maximum:", max_val)
print("Minimum:", min_val)



# 3. Sort List (ASC/DESC)
print("\n---- 3. Sort List ----")

# Using slicing to copy list
asc_list = numbers[:]  
asc_list.sort()

desc_list = numbers[:]
desc_list.sort(reverse=True)

print("Ascending:", asc_list)
print("Descending:", desc_list)



# 4. Frequency Counter
print("\n---- 4. Frequency Counter ----")

freq = {}  # dictionary

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency of elements:", freq)



# 5. Student Marks Dictionary
print("\n---- 5. Student Marks Dictionary ----")

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks   # dictionary storing

print("Student Records:", students)



# 6. Highest Scorer Finder
print("\n---- 6. Highest Scorer ----")

highest_name = None
highest_marks = -1

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

print(f"Topper: {highest_name} with {highest_marks} marks")
