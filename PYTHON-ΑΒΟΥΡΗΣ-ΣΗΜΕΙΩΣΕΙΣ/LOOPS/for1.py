# Μάθημα 8: Δομή επανάληψης for

# Παραδειγμα 1
dd = {1: 30, 8:20, 2: 40}

for i in dd:
    print(i,'->', dd[i])
print(20*'-')

for i in sorted(dd):
    print(i, '->', dd[i])
print(20*'-')

for i in sorted(dd, key = dd.get):
    print(i, '->', dd[i])
print(20*'-')


# Παραδειγμα 2
li = [ 1, 8, 11, 34, 45, 78, 23, 99]
key = int(input("δώσε κλειδί:"))
for item in li:
    if item == key:
        print("βρέθηκε το ", key)
        break
else:
    print("δεν βρέθηκε το ", key)
    