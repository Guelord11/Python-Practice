# Number comparison Tool

nbre1 = float(input("Entrez le premier nombre : "))
nbre2 = float(input("Entrez le deuxieme nombre : "))

if nbre1 == nbre2 :
    print(f"Les deux nombres sont égaux")
elif nbre1 > nbre2 :
    print(f"{nbre1} est supérieur à {nbre2}")
else :
    print(f"{nbre1} est inférieur à {nbre2}")

#Vérifier s'il y a un nombre nul

if nbre1 == 0 or nbre2 == 0:
    print(f"Au moins un nombre est égal à 0")
else:
    print(f"Les deux nombres ne sont pas nuls")