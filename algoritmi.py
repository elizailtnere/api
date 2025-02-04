saraksts = [5, 78, 38, 6, 91, 3]

for j in range(len(saraksts) -1):
    for i in range(len(saraksts) -1-j):
        if saraksts[i] > saraksts[i+1]:
            temp = saraksts[i]
            saraksts[i] = saraksts[i+1]
            saraksts[i+1] = temp

print(saraksts)

def meklēt(list, num):
    for i in range(len(list) -1):
        if num == list[i]:
            print(num, "Eksistē:", i)
            return
    print (num, "Neeksistē")

meklēt(saraksts, 2)
meklēt(saraksts, 38)