name= "Αγαμέμνων"
print(ord('α'))
print(ord('ά'))
print(ord("\n"))
print(ord(" "))
print((ord('A')))        #41 hex = 65
print(chr(ord('a')))
# SLICING
print("======================================")
s="κάτω στους πέρα "   #SLICING->υποσύνολα
print(s[0])
print(s[5:10])
print(s[5:])
print(s[:6])
print(s[-2])                #τον δεύτερο από το τέλος
print(s[-4:])           #από τον μείον 4 έως το τέλος
#Οι συμβολοσειρές είναι αμετάβλητες ακολουθίες χαρακτήρων, δεν επιτρέπεται η αλλαγή τους.
#name="nicos"
#name[0]="N"    #error
# STRING LENGTH
print(len(s))
#print(s[len(s)])    #IndexError: string index out of range
print(s[len(s)-2])
s = 'καλήν εσπέρα άρχοντες'
print(s[-8:]+s[:5])