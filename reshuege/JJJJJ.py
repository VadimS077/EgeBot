f = open("inf_22_10_20_27b.txt")
n = int(f.readline())
maxsum = 0
raz = 0
minraz1 = 999999
minraz2 = 99999
for i in range(n):
    a, b = map(int, f.readline().split())
    maxsum += max(a, b)
    raz= abs(a-b)
    if raz % 3 == 1:
        minraz1 = min(minraz1 ,raz)
    if raz%3==2:
        minraz2= min(minraz2, raz)
    if raz==10:
        print(a,b)
if maxsum%3==0:
    print(maxsum)
elif maxsum%3==1:
    print(maxsum - minraz1)
else:
    print(maxsum - minraz2)
print(maxsum)


