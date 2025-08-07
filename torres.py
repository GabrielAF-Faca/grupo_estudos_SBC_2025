

from statistics import mode


n = int(input())
t = [int(x) for x in input().split(" ")]


moda = mode(t)

print(t.count(moda))
