'''Να κατασκευάσετε λεξικό 
τηλεφωνικών επαφών και να γράψετε 
εντολές για την εισαγωγή νέων 
εγγραφών από το χρήστη και εκτύπωσης 
του λεξικού με αλφαβητική σειρά'''

tel={"bill":"123654123"}
tel.update({"Ambi":25457 ,"John" : 84512226})
print(tel)



key_list=[]
for x in tel:
  key_list.append(x)
key_list.sort()  
print(key_list)
###......................d.items()...Returns a list of key-value pairs (TUPLES) in a dictionary.
tel_list= list(tel.items())
tel_list.sort()
print(tel_list)

