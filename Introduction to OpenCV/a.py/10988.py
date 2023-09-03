a=input()
flag = True
for i in range(len(a)//2):
    if a[i] != a[len(a)-1-i]:
        flag = False
        break

if flag == True:
    print(1)
else:
    print(0)