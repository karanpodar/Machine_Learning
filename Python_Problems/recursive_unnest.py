a = [1,2,3,['a','b',1,2,[3,1,1,['a']]]]

out = []
def unnest(a):
    for i in a:
        if type(i) is list:
            unnest(i)
        else:
            out.append(i)
    return out


print(unnest(a))