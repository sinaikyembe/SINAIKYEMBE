# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:36:21 2023

@author: ianis
"""

a=1 #variable entier
b=3.5#variable reel
nom="sinai" #chaine de charactere
led=True # boolen
x,y=6,8
print(x)
print(y)
print(y**2) # 2 montre la puissance
nbr1=10
nbr2=2
cos1=nbr1/nbr2
cos2=nbr1//nbr2
print(cos1)
print(cos2)
# les operateurs de comparaison
# <=, >=, == ,> ,<,!=
print(nbr1<nbr2)
print(nbr1<=nbr2)
# les operateurs logique
# et=and, ou=or,non=not
# avec and le resultat est vrai losque le deux condition sont vrai
# avec or le resultat est vrai losque l'une de reponse est vrai 
# avec not le resultat est vrai lorsque la reponse est vrai
print("je suis not", not nbr1 > nbr2)
# les structures de données sequencielle
# les tuples et les listes , string ce sont le structure de données sequentielle
# les tuples ne sont pas modifiable
# les listes sont modifiable
# le indexing, les slecing
# quelques methodes ou operations a appliquer sur les listes
tuple_nom=("sinai","ianis","consollate",34,65.7,4,39)
print(tuple_nom) 
# indecing
print(tuple_nom[3])# afficher un element du tuple appartir de son indice
#print(tuple_nom[10])
# la methode len()# elle permet de connaitre les nobre d'element
nbr_element=len(tuple_nom)
print(nbr_element)
print("le dernier element",tuple_nom[6])
#ou encore
print(tuple_nom[-7])
jour_semaine=("lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche")
# slesing
#afficher les jours ouvrable de la semaine anglaise
print(jour_semaine[0:5])
print(jour_semaine[:5])
print(jour_semaine[-7:-2])
#afficher les jours weekend
print(jour_semaine[5:])
tuple_nombre=(0,1,2,3,4,5,6,7,8,9,10)
# afficher que les nombre pair
print(tuple_nombre[2::2])
prenom="sinai"
print(prenom[0:4])
# notion de boucles sur les structure de données sequencielle
# boucle for
for i in jour_semaine:
    print(i)
for i in tuple_nombre[2::2]:
    print(i) 
# les if sur les structure de données sequencielle
if 11 in tuple_nombre:
    print("je sui là ")
else:
    print("je suis pas là") 
if not "lundi" in jour_semaine:  
    print("je ne suis pas là")
else:
    print("je suis là")
# les methodes sur les listes
liste_telephone=["techno","itel","iphone","lenovo","enes","vivo"]
# indexing 
print(liste_telephone[2])
# slesing
print(liste_telephone[0:4])
# boucle
for i in liste_telephone:
    print(i)

if "techno" in liste_telephone:
    print("tu m'as trouver")
else:
    print("tu m'as pas trouver")
# nombre d'element
print(len(liste_telephone))
# remplacer un element de la liste par un autre 
liste_telephone[3]="oppo"
print(liste_telephone)
# ajouter un element dans une liste on utilise la methode append()
liste_telephone.append("etel")
print(liste_telephone)
# la methode insert permet d'ajouter un element à un indice precis
liste_telephone.insert (4,"inphinix")
print(liste_telephone)
liste_telephone.reverse()
print(liste_telephone)






        
    

    

