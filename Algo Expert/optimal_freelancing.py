def optimalFreelancing(jobs):
    # Write your code here.
    out = [ '_' for _ in range(7) ] 
    profit = 0
    jobs.sort(key = lambda job: job['payment'], reverse = True)
    
    for i in jobs:
        idx = i['deadline'] if i['deadline'] <= 7 else 7
        for j in range(idx, 0, -1):
            if out[j] == '_':
                out[j] = i['payment']
                profit += i['payment']
                break
    
    
    # for job in jobs:
    #     maxTime = min(job['deadline'], 7)
    #     for time in reversed(range(maxTime)):
    #         if out[time] == '_':
    #             out[time] = job['payment']
    #             profit += job['payment']
    #             break
    
    
    print(out)


    return profit

jobs = [
    {
      "deadline": 2,
      "payment": 1
    },
    {
      "deadline": 2,
      "payment": 2
    },
    {
      "deadline": 2,
      "payment": 3
    },
    {
      "deadline": 2,
      "payment": 4
    },
    {
      "deadline": 2,
      "payment": 5
    },
    {
      "deadline": 2,
      "payment": 6
    },
    {
      "deadline": 2,
      "payment": 7
    }
  ]

print(optimalFreelancing(jobs))