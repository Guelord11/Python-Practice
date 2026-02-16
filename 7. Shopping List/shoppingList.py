listeShopping = []

def afficherMenu():
    print("\n--- Menu Liste Shopping ---")
    print("1. Afficher la liste de shopping")
    print("2. Ajouter un élément à la liste de shopping")
    print("3. Supprimer un élément de la liste de shopping")
    print("4. Quitter")

while True:
    afficherMenu()

    choix = input("Choisissez une option (1-4) : ")

    if choix == '1':
        if not listeShopping:
            print("La liste de shopping est vide.")
        else:
            print("Liste de shopping :")
            for index, item in enumerate(listeShopping):
                print(f"{index + 1}. {item}")
    
    elif choix == '2':
        nouvel_item = input("Entrez l'élément à ajouter : ")
        listeShopping.append(nouvel_item)
        print(f"{nouvel_item} a été ajouté à la liste de shopping.")
    
    elif choix == '3':
        item_a_supprimer = input("Entrez l'élément à supprimer : ")
        if item_a_supprimer in listeShopping:
            listeShopping.remove(item_a_supprimer)
            print(f"{item_a_supprimer} a été supprimé de la liste de shopping.")
        else:
            print(f"{item_a_supprimer} n'est pas dans la liste de shopping.")
    
    elif choix == '4':
        print("Au revoir ! Faites de beaux achats !")
        break

    else:
        print("Option invalide. Veuillez choisir une option entre 1 et 4.")