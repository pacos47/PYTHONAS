'''print syntax : print(αυτα , χωρισμένα με τον <διαχωριστή> , και στο τελος <χαρακτηρες τελους>)
οπου αυτά=ορίσματα πχ ενα string , μία λιστα κλπ, 
print(ορίσματα , sep='δ' end='ε')'''
# παραδειγμα τυπωσε αριθμους
print(1,2,3,7)   # , between  args
print("Η τιμή της θερμοκρασίας εναι : " , 20)
#separator example : tab    , Absense of separator-> space
print(10,20,30,sep="\t")
# συνήθης τερματικός χαρακτήρας το new line ='\n' που ετσι κιαλλιώς τον βαζει μόνο του
print(10,20,30,sep="\t", end='stop here!\n')
''' print with placeholders denoted by the escape character %, followed by the type (ex %s=string ,
%d=digit etc...  and after that %( tuple to denote the corresponding values)'''
print("Η τιμή της θερμοκρασίας σε βαθμούς %s εναι : %f " %("Κελσίου",35.7) ) #%f Sfor floating
# or with var....and accuracy for ex 1.2 ie 1 = at LEAST one digit at the integer part &2 decimals
temp= 32.876545
print("Η τιμή της θερμοκρασίας σε βαθμούς %s εναι : %1.2f " %("Κελσίου",temp) )
#FORMAT    replace % with {} placeholders and .format() method
print("Η τιμή της θερμοκρασίας σε βαθμούς {} εναι : {:1.2f} ".format("Κελσίου",temp)) 
# note : in {} stands for TYPE, so we could place :s in the first placehoder (redundant as "Κελσιου=str)
print("Η τιμή της θερμοκρασίας σε βαθμούς {:s} εναι : {:10.2f} ".format("Κελσίου",temp)) #10=total here!
# δεξιά στοίχιση
print('{:>10}'.format("test"))
# δεξιά στοίχιση
print('{:>10}'.format("test"))
# αριστερή στοίχιση
print('{:10}'.format("test"))
