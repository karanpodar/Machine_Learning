def runLengthEncoding(string):
    # Write your code here.
    out = []
    count = 1

    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i-1]

        if prev != curr or count == 9:
            out.append(str(count))
            out.append(prev)
            count = 0
        count += 1

    out.append(str(count))
    out.append(string[-1])

    return ''.join(out)