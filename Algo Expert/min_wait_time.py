def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    tot_wait = 0
    last_wait = 0
    for i in range(1,len(queries)):
        last_wait += queries[i-1]
        tot_wait += last_wait  
    return tot_wait
