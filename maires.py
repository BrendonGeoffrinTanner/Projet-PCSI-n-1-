# Crée par Margaux et Brendon

fichier = open("maires.txt", "r")

grande_liste = []
for line in fichier:
  liste_ligne = line.strip()
  petite_liste = liste_ligne.split(";")
  grande_liste.append(petite_liste)

fichier.close()

#________________________________________________________
def nb_maires():                                            # nb maire
  nombre = len(grande_liste)                                # On crée une variable qui est egal au nombre de ligne dans le fichier
  return nombre
print("Il y a",nb_maires(),"maires en France")              # On affiche le nombre de maires


#________________________________________________________
def plus_jeune_maire():                                     # On crée une fonction qui va trouver l'age du plus jeune maire
  date_de_naissance = []                                    # On crée une variable ou l'on va stocker les dates sous forme de liste
  plus_jeune = ["0","0","00"]                               # On met la date par defaut a 0/0/00
  jeune_date = []                                           # On crée une variable qui va donner la date de naissance du plus jeune maire
  age = 0                                                   # On met l'age par defaut à 0
  for i in range(len(grande_liste)):                        # On calcule quel est la date la plus proche de nous
    date_de_naissance.append(grande_liste[i][8])            # La liste date de naissance prend la valeur de la lige n°i
    date = date_de_naissance[i].split("/")                  # On isole les Jours, Mois, Année
    jour = date[0]                                          # Création de la variable jour
    mois = date[1]                                          # Création de la variable mois
    annee = date[2]                                         # Création de la variable année
    if annee >= plus_jeune[2]:                              # On vérifie si l'année est plus grande que celle deja enregistrer
      if mois >= plus_jeune[1]:                             # On vérifie si le mois est plus grande que celuis deja enregistrer
        if jour >= plus_jeune[0]:                           # On vérifie si le jour est plus grande que celuis deja enregistrer
          plus_jeune = date                                 # Nous enregistrons la valeur
          jeune_date = grande_liste[i][8]
          age = 2021 - (int(plus_jeune[2]) + 1900)          # On calcule l'age grace ca son année de naissance
  return age                                                # Nous retournons la valeur de son age

print("Le plus jeune maire a",plus_jeune_maire(),"ans")     # Nous affichons la réponse


#________________________________________________________
def age_moyen():                                            # Nous créons la fonction qui cherche l'age moyen des maires
  compt = 0                                                 # On met en place un compteur
  numerateur = 0                                            # On met en place la somme de tout les ages
  moyenne_age = 0                                           # La variables qui prendra la valeur de l'age moyen
  age = 0                                                   # La variable qui prendra la valeur de l'age
  date_de_naissance = []                                    # La liste qui prendra la valeurs de la date de naissance
  for i in range(len(grande_liste)):                        # On parcourt le document
    date_de_naissance.append(grande_liste[i][8])            # La liste prend la valeurs de la date de naissance de la ligne i
    date = date_de_naissance[i].split("/")                  # on separe la date en format (Jour,Mois,Année)
    annee = int(date[2])                                    # On garde la valeur de l'année
    annee = int(annee) + 1900                               # On trouve l'année compléte
    age = 2021 - int(annee)                                 # On calcule l'age
    compt = compt + 1                                       # On ajoute plus un au compteur (qui compte le nombre de personne)
    numerateur = numerateur + age                           # On fais la somme de tout les ages
  moyenne_age = numerateur / compt                          # On calcule la moyenne
  return int(moyenne_age)                                   # On retourne la valeur de l'age moyen

print("La moyenne d'age est de",age_moyen(),"ans")          # On affiche la valeur de l'age moyen


#________________________________________________________
def age_moyen100k():                                        # On crée la fonction qui va calculer la moyenne d'age des maires de plus de 100 000 habitants
  compt = 0                                                 # On met en place un compteur
  numerateur = 0                                            # La somme de tout les ages
  moyenne_age = 0                                           # La moyenne d'age
  age = 0                                                   # l'age du maire
  date_de_naissance = []                                    # Liste qui prendra pour valeur la date de naissance
  for i in range(len(grande_liste)):                        # On parcours la liste
    date_de_naissance.append(grande_liste[i][8])            # La date de naissance prend la valeur de la date
    date = date_de_naissance[i].split("/")                  # on separe la date en format (Jour,Mois,Année)
    annee = int(date[2])                                    # On garde la valeur de l'année
    if int(grande_liste[i][4]) > 100000:                    # On regarde si la ville a plus de 100 000 habitants
      annee = int(annee) + 1900                             # On trouve l'année complete
      age = 2021 - int(annee)                               # On calcule l'age
      compt = compt + 1                                     # On ajoute plus 1 au compteur
      numerateur = numerateur + age                         # On ajoute la valeur de l'age a la somme
  moyenne_age = numerateur / compt                          # On calcule la moyenne
  return int(moyenne_age)                                   # On retourne cette valeur

print("Pour les communes de plus de 100 000 habitant la moyenne d'age est de",age_moyen100k(),"ans")    # On affiche la valeur


#________________________________________________________
def nom_maire():                                            # On crée la fonction qui va chercher les noms de maire
  comptAurelien = 0                                         # On met en place le compteur qui va compter le nombre de maire qui s'apelle Aurélien
  comptAlexis = 0                                           # On met en place le compteur qui va compter le nombre de maies qui s'apelle Alexis
  for i in range(len(grande_liste)):                        # On parcours la liste
    if str(grande_liste[i][6]) == "Aurélien":               # On regarde si le maire s'apelle Aurélien
      comptAurelien = comptAurelien + 1                     # Si oui on ajoute + 1 au compteur
    elif str(grande_liste[i][6]) == "Alexis":               # On regarde si le maire s'apelle Alexis
      comptAlexis = comptAlexis + 1                         # Si oui on ajoute + 1 au compteur
  print("Il y a",comptAlexis,"maires qui porte le nom Alexis et",comptAurelien,"maires qui porte le nom Aurélien")  # On affiche la réponse
nom_maire()                                                 # On execute la fonction



'''
__Ceci est la partie de l'exercice ou nous avons bloqué __

def plus_jeune_departement():                                       # On crée une fonction qui va chercher le département avec les plus jeune maires
  departement = []
  departement.append(grande_liste[0])
  for i in range(len(grande_liste)):
    if str(departement) == str(grande_liste[i][0]):
      departement.append(grande_liste[i][0])
  print(len(departement))

plus_jeune_departement()




def profession_maire():                                             # On crée une fonction qui va chercher la profession la plus représentez chez les maires (Normalement c'est maire ¯\_(ツ)_/¯ )
    profession = []
    profession.append(grande_liste[8])
    for i in range(len(grande_liste)):
      if str(profession) == str(grande_liste[i][8]):
        profession.append(grande_liste[i][8])
    print(len(profession))

  profession_maire()

'''
