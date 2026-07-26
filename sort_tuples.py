# 12. Sort Tuples

# Given

# students=[
# ("John",82),
# ("Amy",95),
# ("Bob",74)
# ]

# Sort by marks using lambda.

# Output

# [
# ("Bob",74),
# ("John",82),
# ("Amy",95)
# ]

def sort_tuples(students):
    return sorted(students, key=lambda x: x[1])

print(sort_tuples([("John",82),("Amy",95),("Bob",74)]))