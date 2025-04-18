s="πέρα στους πέρα κάμπους"
s.replace("στους","εις τους")
print(s)    #  s unchanged, default
rep_s=s.replace("στους","εις τους") #no need to define new var , see line 15 below so print(s.replace("στους","εις τους"))
print(rep_s)
count=s.count("πέρα")
print(count)
print(s.isalpha())    # false because of Greek????
s_latin="perastoysperakampoys"
print(s_latin.isalpha())    #no , because of spaces
print(s.isdigit())
print(s.islower())    #true
s_upper=s.upper() ; print(s_upper)   #MULTILINE STATESMENTS SEPARATED BY ;
print(s == s_upper.lower())   # mustbe true as lower() recups original string
print(s.capitalize())    #NO NEED TO DEFINE NEW VARS !!!!!!!!
print(s.find("στους")) ; print(s.find("kiki"))   #
print(s.split())   # here split char is space, result is LIST
'''join-> metre un string parmis les elements d'une liste, syntax:string.join([list of stings])'''
print("*".join(['a' , 'b' , 'c']))   # now with split() , recover the list
print("a*b*c".split('*'))
print(len('Σε γνωρίζω από την κόψη'.split()))