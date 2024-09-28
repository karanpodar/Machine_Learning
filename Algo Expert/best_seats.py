def bestSeat(seats):
    # Write your code here.
    best_seat = -1
    space = 0
    l = r = 0

    while r < len(seats):
        if seats[r] == 1:
            if r-l-1 > space:
                space = r-l-1
                best_seat = (l + r) // 2
            l = r
        r += 1
    return best_seat
