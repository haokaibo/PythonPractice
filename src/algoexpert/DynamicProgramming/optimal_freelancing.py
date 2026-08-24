def optimalFreelancing(jobs):
    # Write your code here.
    # Solution
    # 1. The max payment we can get depends on the sum of the max available payment we can get
    # 2. For a single day, there is only one task can be done. We should choose the largest payment value as the job to be done on a single day.
    # 3. We can use a dict to hold the maximum payment that can be got for a single day.
    # 4. Use a sum to max_payment we can get. For each iteration, we need to substract the payment if it exsits in the dict if there is a job already in the dict.
    # 5. Then add the new larger payment in the sum
    # Time complexity: O(nlog(n))
    
    if jobs is None or len(jobs) == 0:
        return 0

    LENGTH_OF_PERIOD = 7
    jobs.sort(key=lambda job: job["payment"], reverse=True)

    timeline = [False] * LENGTH_OF_PERIOD # There are only 7 days for a period

    profit = 0

    for job in jobs:
        max_time = min(job["deadline"], LENGTH_OF_PERIOD)
        for time in reversed(range(max_time)):
            if timeline[time] == False:
                timeline[time] = True
                profit += job["payment"]
                break
    return profit


jobs = [
    {
      "deadline": 1,
      "payment": 1
    },
    {
      "deadline": 1,
      "payment": 2
    }
  ]

print(optimalFreelancing(jobs))