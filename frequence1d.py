from random import * #import des modules
F=[0,0,0,0,0,0] #définition de la liste

#___________________________________________________________________
n=int(input("nombre de lancers : ")) #demande du nombre de lancers


for i in range(n) : 
    i=+1
    res=randint(1,6)                     #lancers de dés
    print(res)
    for j in range(7) :
        k=j-1               #analyse et incrementation
        if j==res:
            F[k]=F[k]+1
        j=+1
print([F]) #affichage de la liste, le premier chiffre est le nombre de fois que 1 est tombé, etc etc

#___________________________________________________________________

for a in range(6):#affichage des résultats
    b=a+1
    c=str(b)

    O=F[a]
    a=+1
    prct=(100*int(O))
    prct=prct/n
    print("le nombre "+ c +" est tombé :"+str(O)+" fois, sa fréquence est de " +str(O)+"/"+str(n)+" ou :"+str(prct)+"%")
    