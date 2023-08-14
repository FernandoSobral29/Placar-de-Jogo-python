TimeA = input("Qual o time A? ")
GolsTimeA = input("Quantos gols o time A fez? ")
TimeB = input("Qual o time B? ")
GolsTimeB = input("Quantos gols o time B fez? ")

print (f"O {TimeA} fez {GolsTimeA} gols!")
print (f"O {TimeB} fez {GolsTimeB} gols!\n")

if GolsTimeA == GolsTimeB:
    print ("O resultado foi empate!")

elif GolsTimeA > GolsTimeB:
    print (f"O {TimeA} venceu!")
    
elif GolsTimeA < GolsTimeB:
    print (f"O {TimeB} venceu!")
