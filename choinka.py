import time
wysokosc = int(input("Podaj wysokość: "))
ile = int(input("Podaj z ilu częsć ma składac się choinka: "))
print()
print()

#choinka
red = "\033[1;31m"
grean = "\033[1;32m"
end = "\033[0m"

przerwa = wysokosc * ile
n = 1
for x in range(1, ile+1):
    for i in range(n,wysokosc+1):
        time.sleep(0.5)
        for j in range(przerwa, i-1,-1):
            print(end=" ")
        for k in range(1,i+1):
            print(f"{grean}*{end}", end=" ")
        print()
    n = n + 2
    wysokosc = wysokosc + 2



#pień
for i in range(0, ile):
    for j in range(przerwa-3,-1,-1):
        print(end=" ")

    if ile == 1:
        a = round(ile/2)
        time.sleep(0.3)
        print(a*" "+" * *")


    elif ile == 2:
        for k in range(1, ile+1):
            time.sleep(0.3)
            print(" *", end=" ")


    else:
        for k in range(1, ile+1):
            time.sleep(0.3)
            print("*", end=" ")

    print()


#napis wesołych świąt
przerwa = round(przerwa/2) * " "
print()
time.sleep(0.3)
print(f"{przerwa}{red}WESOŁYCH ŚWIĄT!{end}\n")