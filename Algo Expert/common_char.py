def commonCharacters(strings):

    strings.sort(key=lambda a: len(a))
    visit = {a for a in strings[0]}
    out = list(visit)

    for i in strings:
        for j in visit:
            if j not in set(i) and j in out:
                out.remove(j)
    return out


strings =["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]
print(commonCharacters(strings))