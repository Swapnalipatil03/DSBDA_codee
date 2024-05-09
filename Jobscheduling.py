def job_schedule(jobs):
    # Sort the jobs based on their deadlines in descending order
    jobs.sort(key=lambda x: x[1], reverse=True)
    
    # Find the maximum deadline among all jobs
    max_deadline = max(jobs, key=lambda x: x[2])[2]
    
    # Create a time slot list initialized with False representing all slots are initially empty
    slot = [False] * max_deadline
    
    # Initialize profit to zero
    profit = 0
    
    # Get the total number of jobs
    n = len(jobs)

    # Iterate over each job
    for i in range(n):
        # Get the deadline of the current job
        deadline = jobs[i][2] - 1
        
        # While there are available slots before the deadline
        while deadline >= 0 and slot[deadline]:
            # Decrement the deadline until an empty slot is found
            deadline = deadline - 1
        
        # If there is an available slot before the deadline
        if deadline >= 0:
            # Mark the slot as occupied
            slot[deadline] = True
            # Add the profit of the current job to the total profit
            profit += jobs[i][1]
    
    # Return the total profit
    return profit

# Define the list of jobs with format (job_id, profit, deadline)
jobs = [(1, 50, 2), (2, 10, 1), (3, 20, 2), (4, 30, 1), (5, 40, 3)]

# Call the job_schedule function with the list of jobs and print the result
print(job_schedule(jobs))
