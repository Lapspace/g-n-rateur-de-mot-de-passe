import random

#caractere

lettre = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombre = "0123456789"
syboles = "@#$&*/\?"

caractere = lettre + lettre.lower() + nombre + syboles
caractere_no_syboles = lettre + lettre.lower() + nombre

while True:
    longueurmdp = int(input("Entrez la longueur du mot de passe :"))
    nombredemdp = int(input("Entrez le nombre de mot de passe a afficher :"))
    caractere_speciaux_ask = str(input("Faut il mettre des caractere speciaux dans le mot de passe ? :"))
    if caractere_speciaux_ask == 'oui' :
        for i in range(0,nombredemdp):
            mdp = ""
            for i in range(0,longueurmdp):
                cmdp = random.choice(caractere)
                mdp =mdp + cmdp
            print('votre mot de passe est :', mdp)

    elif caractere_speciaux_ask == 'non':
        for i in range(0,nombredemdp):
            mdp = ""
            for i in range(0,longueurmdp):
                cmdp = random.choice(caractere_no_syboles)
                mdp =mdp + cmdp
            print('votre mot de passe est :', mdp)

    elif caractere_speciaux_ask != 'oui' or 'non':
        print (ERREUR)