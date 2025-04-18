'''πράξεις με συμβολοσειρές
τελεστής	αποτέλεσμα
<seq> + <seq>	συνένωση
<seq> * <int>	επανάληψη
<seq>[]	δείκτης
len(<seq>)	μήκος ακολουθίας
<seq>[:]	τεμαχισμός
for <var> in <seq>:	επανάληψη
<expr> in <seq>	συμμετοχή (Boolean)'''
first_name="Nicos"
Surname="Papanicos"
print(first_name+Surname)    #synenwsi
print(first_name,Surname)     # αλληλουχία
print("babis"*3)
for k in Surname:
    print(k)
print('h' in 'babis')      # h does not belong to "babis"