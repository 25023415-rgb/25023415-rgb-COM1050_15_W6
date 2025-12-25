n = list(map(int , input().split()))
m = list(map(int , input().split()))
phantuchung = []
for i in n:
    if i in m and i not in phantuchung:
        phantuchung.append(i)
print(phantuchung)
