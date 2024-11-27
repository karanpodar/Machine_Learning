def getNthFib(n):

    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1
    return getNthFib(n-1) + getNthFib(n-2)



def getNthFib(n):
    # Write your code here.
    mem = {1 : 0, 2 : 1}
    if n in mem:
        return mem[n]
    else:
        mem[n] = getNthFib(n-1) + getNthFib(n-2)
        return mem[n]



def getNthFib(n):
    # Write your code here.
    last = [0, 1]
    count = 3
    while count <= n:
        next = last[0] + last[1]
        last[0] = last[1]
        last[1] = next
        count += 1
    return last[1] if n > 1 else last[0]