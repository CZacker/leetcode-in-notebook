def fib(lenght, index):
    res = []
    for i in range(lenght):
        if i == 0 or i == 1:
            res.append(1)
        else:
            res.append(res[i - 2] + [i - 1])
    return res[index]


a = []
s = input()

if s != "":
    for x in s.split():
        a.append(int(x))

print(fib(*a))