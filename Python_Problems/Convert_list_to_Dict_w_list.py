routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

d = {}

for i in routes:
    if i[0] in d:
        print(d[i[0]])
        d[i[0]].append(i[1])
    else:
        d[i[0]] = [ i[1] ]

    print(i[0], i[1])

print(d)