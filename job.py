def printJobScheduling(arr, t):

    # length of array
    n = len(arr)

    # Sort all jobs according to decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t

    # To store total time or cost
    total_time = 0

    # Iterate through all given jobs
    for i in range(len(arr)):

        # Find a free slot for this job
        # (Note that we start from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                total_time += arr[i][2]
                break

    # Return both the sequence of jobs and the total time
    return job, total_time


# Driver's Code
if __name__ == '__main__':
    arr = [['a', 2, 4],  # Job Array
           ['b', 1, 7],
           ['c', 2, 3],
           ['d', 1, 1],
           ['e', 3, 8]]

    print("Following is maximum profit sequence of jobs")

    # Function Call
    job_sequence, total_time = printJobScheduling(arr, 3)
    print("Job sequence:", job_sequence)
    print("Total time:", total_time)
