ingredients = {"farine", "sucre", "beur", "oeufs", "lait"}

questionUser = input("Entrez les ingredients que vous avez séparés par des virgules : ")
ingredientsUser = set(questionUser.split(", ")) 

ingredientsManquants = ingredients - ingredientsUser

ingredientsSupp = ingredientsUser - ingredients

print("\n--- Resultats des ingredients ---")
if ingredientsManquants:
    print(f"Vous manquez ces ingredients : {', '.join(ingredientsManquants)}")
else:
    print("Vous avez tous les ingredients necessaires")

if ingredientsSupp:
    print(f"Vos ingredients supplementaires : {', '.join(ingredientsSupp)}")
else:
    print("Vous avez tous les ingredients necessaires")