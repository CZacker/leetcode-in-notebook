def max(strs):
    if len(strs) == 0:
        return ""
    res = ""
    for i in zip(*strs):
        if len(set(i)) == 1:
            res += i[0]
        else:
            return res

    return res
ord()