naam = "Sam"
print("Hallo ik ben " + naam) 

B = "Ik heb voor u 3 vragen."
vraag1 = "Waar woon ik?" 
vraag2 = "Hoe oud ben ik?"
vraag3 = "Heb ik een broertje of zusje?"
kies = "Is het A / B / C. Voer uw antwoord in."
Y = False
Ans = "U heeft het antwoord goed, ga verder naar de volgende vraag."
Fout = "U heeft fout beantwoord, u mag het opnieuw proberen."


print(B)


print(vraag1)
print("A = Amsterdam")
print("B = Rotterdam")
print("C = Zaandam")

X = input(kies)

if ( X == "A" ):
    print(Ans)
else:
    print(Fout)
