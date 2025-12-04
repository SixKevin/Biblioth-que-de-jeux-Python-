import random
import time

# ==========================================
# JEU 1 : LE JUSTE NOMBRE
# ==========================================
def le_juste_nombre():
    print("\n" + "="*40)
    print(" BIENVENUE AU JEU DU JUSTE NOMBRE ")
    print("="*40)
    time.sleep(1)

    nombre_a_deviner = random.randint(1, 100)
    essais = 0

    print("Je pense à un nombre entre 1 et 100.")
    time.sleep(1)

    # Configuration des tentatives
    max_essais = None
    reponse = input("Voulez-vous limiter le nombre de tentatives ? (oui/non) : ").strip().lower()
    
    if reponse == "oui":
        while True:
            try:
                max_essais = int(input("Combien de tentatives voulez-vous ? : "))
                break
            except ValueError:
                print("Veuillez entrer un chiffre valide.")

    # Boucle du jeu
    while True:
        # Vérification des vies restantes
        if max_essais is not None and essais >= max_essais:
            print(f"\n Désolé, vous avez épuisé vos {max_essais} tentatives.")
            print(f"Le nombre était : {nombre_a_deviner}")
            break

        entree = input("\nEntrez votre proposition : ").strip()

        if not entree.isdigit():
            print("⚠️ Veuillez entrer un nombre valide.")
            continue

        proposition = int(entree)
        essais += 1

        if proposition < nombre_a_deviner:
            print(" C'est plus !")
        elif proposition > nombre_a_deviner:
            print(" C'est moins !")
        else:
            print(f"\n🎉 Félicitations ! Vous avez trouvé le nombre {nombre_a_deviner} en {essais} essais.")
            break
    
    input("\nAppuyez sur Entrée pour revenir au menu...")

# ==========================================
# JEU 2 : TIC TAC TOE (Morpion)
# ==========================================
def tic_tac_toe():
    print("\n" + "="*40)
    print(" BIENVENUE AU TIC TAC TOE ")
    print("="*40)
    
    plateau = [' ' for _ in range(9)]

    def afficher_plateau():
        print("\n")
        print(f" {plateau[0]} | {plateau[1]} | {plateau[2]} ")
        print("-----------")
        print(f" {plateau[3]} | {plateau[4]} | {plateau[5]} ")
        print("-----------")
        print(f" {plateau[6]} | {plateau[7]} | {plateau[8]} ")
        print("\n")

    def verifier_victoire(symbole):
        victoires = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        for combo in victoires:
            if plateau[combo[0]] == plateau[combo[1]] == plateau[combo[2]] == symbole:
                return True
        return False

    def plateau_plein():
        return ' ' not in plateau

    def coup_robot():
        # 1. Gagner si possible
        for i in range(9):
            if plateau[i] == ' ':
                plateau[i] = 'O'
                if verifier_victoire('O'): return
                plateau[i] = ' ' # Annuler si pas victoire
        
        # 2. Bloquer le joueur
        for i in range(9):
            if plateau[i] == ' ':
                plateau[i] = 'X'
                if verifier_victoire('X'):
                    plateau[i] = 'O'
                    return
                plateau[i] = ' '

        # 3. Prendre le centre
        if plateau[4] == ' ':
            plateau[4] = 'O'
            return

        # 4. Prendre un coin ou autre
        cases_libres = [i for i in range(9) if plateau[i] == ' ']
        if cases_libres:
            plateau[random.choice(cases_libres)] = 'O'

    # Instructions
    print("Vous êtes X, le robot est O.")
    print("Les cases sont numérotées de 0 à 8 (0 en haut à gauche, 8 en bas à droite).")
    time.sleep(2)

    while True:
        afficher_plateau()
        
        # Tour du Joueur
        while True:
            try:
                choix = int(input("Votre coup (0-8) : "))
                if 0 <= choix <= 8 and plateau[choix] == ' ':
                    plateau[choix] = 'X'
                    break
                else:
                    print("Case invalide ou occupée.")
            except ValueError:
                print("Entrez un chiffre entre 0 et 8.")

        if verifier_victoire('X'):
            afficher_plateau()
            print(" VOUS AVEZ GAGNÉ !")
            break
        if plateau_plein():
            afficher_plateau()
            print(" ÉGALITÉ !")
            break

        # Tour du Robot
        print("Le robot réfléchit...")
        time.sleep(1)
        coup_robot()

        if verifier_victoire('O'):
            afficher_plateau()
            print(" LE ROBOT A GAGNÉ !")
            break
        if plateau_plein():
            afficher_plateau()
            print(" ÉGALITÉ !")
            break
            
    input("\nAppuyez sur Entrée pour revenir au menu...")

# ==========================================
# JEU 3 : PIERRE FEUILLE CISEAUX
# ==========================================
def pierre_feuille_ciseaux():
    print("\n" + "="*40)
    print(" PIERRE - FEUILLE - CISEAUX ")
    print("="*40)

    reponse = input("Voulez-vous lire les règles ? (oui/non) : ").lower()
    if reponse == "oui":
        print("\nRègles : Pierre bat Ciseaux, Ciseaux bat Feuille, Feuille bat Pierre.")
        time.sleep(2)

    options = ['pierre', 'feuille', 'ciseaux']
    score_joueur = 0
    score_ordi = 0

    while True:
        print(f"\n Score : Vous {score_joueur} - {score_ordi} Ordi")
        choix_joueur = input("Votre choix (pierre, feuille, ciseaux) ou 'quitter' : ").lower().strip()

        if choix_joueur == 'quitter':
            print(f"\nFIN DU JEU ! Score final : Vous {score_joueur} - {score_ordi} Ordi")
            break

        if choix_joueur not in options:
            print(" Choix invalide.")
            continue

        print("L'ordinateur réfléchit...")
        time.sleep(1)
        choix_ordi = random.choice(options)
        print(f" L'ordinateur a choisi : {choix_ordi}")

        if choix_joueur == choix_ordi:
            print(" Égalité !")
        elif (choix_joueur == 'pierre' and choix_ordi == 'ciseaux') or \
             (choix_joueur == 'ciseaux' and choix_ordi == 'feuille') or \
             (choix_joueur == 'feuille' and choix_ordi == 'pierre'):
            print(" Vous gagnez la manche !")
            score_joueur += 1
        else:
            print(" L'ordinateur gagne la manche !")
            score_ordi += 1
    
    input("\nAppuyez sur Entrée pour revenir au menu...")

# ==========================================
# MENU PRINCIPAL
# ==========================================
def menu_principal():
    while True:
        # Nettoyer un peu l'affichage avec des sauts de ligne
        print("\n" * 2) 
        print("╔════════════════════════════════════╗")
        print("║      BIBLIOTHÈQUE DE JEUX          ║")
        print("╠════════════════════════════════════╣")
        print("║ 1. Deviner le nombre               ║")
        print("║ 2. Tic Tac Toe (Morpion)           ║")
        print("║ 3. Pierre Feuille Ciseaux          ║")
        print("║ 4. Quitter                         ║")
        print("╚════════════════════════════════════╝")

        choix = input("Entrez le numéro du jeu : ").strip()

        if choix == '1':
            le_juste_nombre()
        elif choix == '2':
            tic_tac_toe()
        elif choix == '3':
            pierre_feuille_ciseaux()
        elif choix == '4':
            print("\nMerci d'avoir joué ! À bientôt.")
            break
        else:
            print("\n Choix invalide, veuillez réessayer.")
            time.sleep(1)

# Lancement du programme
if __name__ == "__main__":
    menu_principal()

    


    

    


    



    
