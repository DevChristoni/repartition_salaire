def repartition_salaire() :
    print("\nRepartition de salaire :\n")
    print("Vous entrer votre salaire et nous essayons de le repartir comme suit :\n50% pour les charges fixes, 10% pour les loisirs et dons, 20% pour l'epargne et 20% pour les investissements.\n")
    
    while True :
        try :
            salaire = float(input("Veuillez entrer votre salaire svp :"))
            break
        except ValueError :
            print("Entrez une somme svp")
    
    charges_fixes = (salaire*50)/100
    loisirs_et_dons = (salaire*10)/100
    epargne = (salaire*20)/100
    investissement = (salaire*20)/100
    
    print(f"\nEn fonction de votre salaire, vous devez utilisez :\n\n{charges_fixes:.2f} francs pour les charges fixes (loyer, nourriture et transport).\n{loisirs_et_dons:.2f} francs pour les loisirs et dons.\n{epargne:.2f} francs pour l'epargne et {investissement:.2f} francs pour les investissements.\n\nMerci de nous avoir fait confiance. A bientot !\n")

def limite_depenses() :
    print("\nGestion du salaire:\n\nEntrer votre salaire. Par la suite, nous calculerons les sommes maximales ou minimales a utiliser au niveau des charges tels que :\n\n-Charges fixes (50% du salaire) : loyer,nourriture et transport\n-Loisirs et dons (10% du salaire)\n-Epargne (20% du salaire)\n-Investissements (20% du salaire)\n")
    while True :
        try :
            salaire = float(input("Veuillez entrer votre salaire :"))
            break
        except ValueError:
            print("Entrez une somme svp")
    
    charges_fixes = (salaire*50)/100
    loisirs_et_dons = (salaire*10)/100
    epargne = (salaire*20)/100
    investissement = (salaire*20)/100
    
    while True :
        print("\nDepenses charges fixes ( Tapez 0 a n'importe quel champ pour arreter avec les charges fixes) :\n")
        
        while True :
            try :
                loyer = float(input("Saisissez le montant de votre loyer :"))
                break
            except :
                print("Entrez une somme svp")
                
        if loyer==0 :
            break
        
        while True :
            try :
                nourriture = float(input("Saisissez le montant de la popote :"))
                break
            except ValueError:
                print("Entrez une somme svp")
                
        if nourriture==0 :
            break
        
        while True :
            try :
                transport = float(input("Saisissez le montant de votre transport :"))
                break
            except ValueError:
                print("Entrez une somme svp")
                
        if transport==0 :
            break
        
        somc = loyer+nourriture+transport
        
        if somc<=charges_fixes :
            print(f"\nVos depenses sont egales a {somc:.2f} francs, vous ne devez pas depassez {charges_fixes:.2f} francs : Les depenses sont bonnes !")
        else :
            print(f"\nVos depenses sont egales a {somc:.2f} francs, vous ne devez pas depassez {charges_fixes:.2f} francs : Les depenses sont excessives, veuillez corriger cela.")
       
    while True :
        print("\nDepenses Loisirs et dons ( Tapez 0 pour arreter avec les loisirs et dons) :\n")
        
        while True :
            try :
                ld = float(input("Saisissez le montant pour les loisirs et dons :"))
                break
            except ValueError:
                print("Entrez une somme svp")
        
        if ld == 0 :
            break
        if ld<=loisirs_et_dons :
            print(f"\nVos depenses sont egales a {ld:.2f} francs, vous ne devez pas depassez {loisirs_et_dons:.2f} francs : Les depenses sont bonnes !")
        else :
            print(f"\nVos depenses sont egales a {ld:.2f} francs, vous ne devez pas depassez {loisirs_et_dons:.2f} francs : Les depenses sont excessives, veuillez corriger cela.")

    while True :
        print("\nL'epargne ( Tapez 0 pour arreter avec l'epargne) :\n")
        
        while True :
            try :
                ep = float(input("Saisissez le montant pour l'epargne :"))
                break
            except ValueError :
                print("Entrez une somme svp")
        
        if ep == 0 :
            break
        if ep>=epargne :
            print(f"\nVotre epargne est de {ep:.2f} francs, vous devez epargner au minimum {epargne:.2f} francs : Votre montant d'epargne est bon !")
        else :
            print(f"\nVotre epargne est de {ep:.2f} francs, vous devez epargner au minimum {epargne:.2f} francs : Votre somme d'epargne n'est pas bonne, veuillez corriger cela.")

    while True :
        print("\nLes investissements ( Tapez 0 pour arreter avec les investissements) :\n")
        
        while True :
            try :
                inv = float(input("Saisissez le montant pour les investissements :"))
                break
            except ValueError:
                print("Entrez une somme svp")
                
        if inv == 0 :
            print("\nMerci et a bientot !")
            break
        if inv>=investissement :
             print(f"\nLe montant d'investissement est de {inv:.2f} francs, vous devez investir au minimum {investissement:.2f} francs : Votre montant pour l'investissement est bon !")
        else :
            print(f"\nVotre epargne est de {inv:.2f} francs, vous devez epargner au minimum {investissement:.2f} francs : Votre somme d'investissement n'est pas bonne, veuillez corriger cela.")

print("Bienvenue sur l'application de gestion de salaire, choisissez entre l'option 1,2 ou 3 pour effectuer les operations.\n\nOption 1 : Repartition de salaire\n\nOption 2 : Gestion du salaire\n\nOption 3 : Quitter\n\nTapez 1 pour l'option 1, 2 pour l'option 2 et 3 pour quitter\n")

while True :
    
    try :
        reponse = int(input("\nEntrez votre reponse ici pour choisir l'option 1 ou 2 ou 3 svp :"))
        if reponse == 1 :
            repartition_salaire()
            
        if reponse == 2 :
            limite_depenses()
            
        if reponse == 3 :
            print("Merci et a bientot !")
            break
    except ValueError :
        print("Veuillez entrer soit 1 ou 2 ou 3 svp")
        
    
    
            
   







