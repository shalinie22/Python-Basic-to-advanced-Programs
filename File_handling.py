# Section 5: File Handling (4 Questions)
# 17. Count Lines

# Read a text file.

# Print

# # Total number of lines


with open("sha.txt", 'r') as sh:
    # print(len(sh.readlines()))
    print(sum(1 for __ in sh))

# 18. Word Frequency

# Given a file

# apple orange apple banana orange apple

# Print

# apple : 3

# orange : 2

# banana :1

with open("freq.txt","r") as fr:
    freq_text = fr.read().split(" ")

print(freq_text)

s={}
for i in freq_text:
    s[i] = s.get(i,0)+1

print(s)


# 19. Copy File

# Read one file and copy its contents into another file.

with open("sha.txt","r") as sh:
    with open("sha_copy.txt","w") as sh_copy:
        sh_copy.write(sh.read())
# 
# 20. Student Marks File

# Input file

# John,78

# Amy,92

# Bob,61

# David,35

# Read the file.

# Print

# John Pass

# Amy Pass

# Bob Pass

# David Fail


with open("Student.txt", "r") as stu:
    students = stu.readlines()

print(students)

for i in students:
    name, marks = i.strip().split(",")
    print(f"{name} {'Pass' if int(marks)>=40 else 'Fail'}")