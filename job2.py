arr = [
    ['a', 2, 100], 
    ['b', 2, 20], 
    ['c', 1, 40], 
    ['d', 3, 35], 
    ['e', 1, 25]
]

print("Following is maximum profit sequence of Jobs: ")

# Define the number of time slots available
t = 3

# Sort all jobs according to decreasing order of profit
n = len(arr)
for i in range(n):
    for j in range(n - 1 - i):
        if arr[j][2] < arr[j + 1][2]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# To keep track of free time slots
result = [False] * t

# To store result (Sequence of jobs)
job = ['-1'] * t

# Initialize total cost
total_cost = 0

# Iterate through all given jobs
for i in range(len(arr)):
    # Find a free slot for this job
    # (Note that we start from the last possible slot)
    for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
        # Free slot found
        if result[j] is False:
            result[j] = True
            job[j] = arr[i][0]
            # Add the cost of the current job to the total cost
            total_cost += arr[i][2]
            break

# Print the sequence and total cost
print("Job sequence:", job)
print("Total cost:", total_cost)
