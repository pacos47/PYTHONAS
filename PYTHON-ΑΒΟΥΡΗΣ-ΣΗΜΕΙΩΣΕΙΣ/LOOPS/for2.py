# Παραδειγμα 1
li1 = [1,2,3, 9]
li2 = [5,6,7, 8]
li3 = [0,4,4, 0]
li = [li1,li2,li3]

for i in li:
    for j in i:
        print(j, end ="\t")
    print()


# Παραδειγμα 2
st = "καλή σας μέρα αρχόντες"

li = []
for ch in st:
    if ch.isalpha():
        li.append(ch)

print(li)


# Παραδειγμα 3
grammata = {}
tonoumena = {"ά": "α",
             "έ": "ε",
             "ή": "η",
             "ί":"ι",
             "ό":"ο",
             "ύ": "υ",
             "ώ":"ω"}

keimeno = input("Δώσε το κείμενο :")

for c in keimeno :
    if c.isalpha():
        if c in tonoumena:
            c = tonoumena[c]
        c = c.upper()
        grammata[c] = grammata.get(c,0) + 1

for c in sorted(grammata.keys()) :
    print ( c, " : ", grammata[c])

sentence = "T"
characters = {}

for character in sentence:
    characters[character] = characters.get(character,0)+1 

print(characters)
