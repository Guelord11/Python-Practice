carnetAdresse = {}

def menu():
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Rechercher un contact par nom")
    print("4. Modifier les détails d'un contact")
    print("5. Supprimer un contact")
    print("6. Quitter")

while True:
    menu()
    choix = input("Choisissez une option (1-6) : ")

    if choix == '1':
        nom = input("Entrez le nom du contact : ")
        numero = input("Entrez le numéro de téléphone du contact : ")
        adresse = input("Entrez l'adresse du contact : ")
        carnetAdresse[nom] = {"numero": numero, "adresse": adresse}
        print(f"Contact {nom} ajouté avec succès.")

    elif choix == '2':
        if not carnetAdresse:
            print("Le carnet d'adresses est vide.")
        else:
            print("Contacts dans le carnet d'adresses :")
            for key, details in carnetAdresse.items():
                print(f"{key}: {details}")

    elif choix == '3':
        nom = input("Entrez le nom du contact à rechercher : ")
        if nom in carnetAdresse:
            print(f"Contact trouvé : {nom}: {carnetAdresse[nom]}")
        else:
            print("Contact non trouvé.")
    
    elif choix == '4':
        nom = input("Entrez le nom du contact à modifier : ")
        if nom in carnetAdresse:
            print("Laissez vide pour conserver la valeur actuelle")
            nouveau_numero = input(f"Nouveau numéro (actuel: {carnetAdresse[nom]['numero']}) : ")
            nouvelle_adresse = input(f"Nouvelle adresse (actuelle: {carnetAdresse[nom]['adresse']}) : ")
            
            if nouveau_numero.strip():
                carnetAdresse[nom]['numero'] = nouveau_numero
            if nouvelle_adresse.strip():
                carnetAdresse[nom]['adresse'] = nouvelle_adresse
            
            print(f"Contact {nom} modifié avec succès.")
        else:
            print("Contact non trouvé.")
    
    elif choix == '5':
        nom = input("Entrez le nom du contact à supprimer : ")
        if nom in carnetAdresse:
            del carnetAdresse[nom]
            print(f"Contact {nom} supprimé avec succès.")
        else:
            print("Contact non trouvé.")
    
    elif choix == '6':
        print("Au revoir !")
        break
    
    else:
        print("Option invalide. Veuillez choisir une option entre 1 et 6.")
        
print("Programme terminé.")
