a,b,c = map(int,input().split())
menu =dict()
s_menu = dict()
service = set()
for _ in range(a):
    food,price = input().split()
    price = int(price)
    menu[food] = price

for _ in range(b):
    food,price = input().split()
    price = int(price)
    s_menu[food] =price

for _ in range(c):
    service.add(input())

n =int(input())
arr= []
for _ in range(n):
    arr.append(input())
buy=0
for i in arr:
    if i in menu:
        buy+=menu[i]
        
if buy >= 20000:
    print("Okey")
    for i in arr:
        if i in s_menu:
            buy+=s_menu[i]
else:
    print("No")

if buy >=50000:      
    for i in arr:
        if i in service:
            print("Okey")
            break
else:
    print("No")
        
