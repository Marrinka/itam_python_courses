def summation(s: str):
    l = list(map(int, s.split()))
    maxel = 0
    for i in range(len(l)):
        if l[i] < 0:
            l[i] = abs(l[i])*2
        if l[i] > maxel:
            maxel = l[i]

    sum = 0
    for el in l:
        sum+= el / maxel
    return (sum)


