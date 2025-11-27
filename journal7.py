import sys

# Default scores if no parameters are given
scores = [10, 20, 30, 40, 50]

if len(sys.argv) > 1:

    scores = [int(x) for x in sys.argv[1:]]
    print("User provided scores:")
else:
    print("No parameters given using default scores:")

print("Scores:", scores)

total = sum(scores)
average = total / len(scores) if scores else 0

print("Sum:", total)
print("Average:", average)

