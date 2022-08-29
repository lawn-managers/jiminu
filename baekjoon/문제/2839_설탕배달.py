kg = int(input())

for i in range(kg, -1, -1) :
    if i % 5 == 0 and (kg-i) % 3 == 0 :
        print(i//5 + (kg-i)//3)
        break
    if i == 0 :
        print(-1)