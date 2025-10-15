from math import *
from random import *
from time import *
from ion import *
a = 0
b = 0
c = True
reponse = "question"
question = "reponse"

while True :
  while a == b :
    a = randint(1,34) #remplacez 34 par votre nombre de question
    if a == 1 : 
      question = "departement n 1?" #remplacez Département n 1 par votre question
      reponse = "Ain" #remplacez Ain par votre réponse
      b = 1
    if a == 2 :
      question = "departement n 2?" #pareil que le paragraphe d'avant
      reponse = "Aisne" #pareil que le paragraphe d'avant
      b = 2
    if a == 3 :
      question = "departement n 3?"
      reponse = "Allier"
      b = 3
    if a == 4 :
      question = "departement n 4?"
      reponse = "Alpes-de-Haute-Provence"
      b = 4
    if a == 5 :
      question = "departement n 5?"
      reponse = "Hautes-Alpes"
      b = 5
    if a == 6 :
      question = "departement n 6?"
      reponse = "Alpes-Maritimes"
      b = 6
    if a == 7 :
      question = "departement n 7?"
      reponse = "Ardeche"
      b = 7
    if a == 8 :
      question = "departement n 8?"
      reponse = "Ardennes"
      b = 8
    if a == 9 :
      question = "departement n 9?"
      reponse = "Ariege"
      b = 9
    if a == 10 :
      question = "departement n 10?"
      reponse = "Aube"
      b = 10
    if a == 11 :
      question = "departement n 11?"
      reponse = "Aude"
      b = 11
    if a == 12 :
      question = "departement n 12?"
      reponse = "Aveyron"
      b = 12
    if a == 13 :
      question = "departement n 13?"
      reponse = "Bouches-du-Rhone"
      b = 13
    if a == 14 :
      question = "departement n 14?"
      reponse = "Calvados"
      b = 14
    if a == 15 :
      question = "departement n 15?"
      reponse = "Cantal"
      b = 15
    if a == 16 :
      question = "departement n 16?"
      reponse = "Charente"
      b = 16
    if a == 17 :
      question = "departement n 17?"
      reponse = "Charente-Maritime"
      b = 17
    if a == 18 :
      question = "departement n 18?"
      reponse = "Cher"
      b = 18
    if a == 19 :
      question = "departement n 19?"
      reponse = "Correze"
      b = 19
    if a == 20 :
      question = "departements n 20?"
      reponse = "2A: Corse-du-Sud ,2B: Haute-Corse"
      b = 20
    if a == 21 :
      question = "departement n 21?"
      reponse = "Cote-d Or"
      b = 21
    if a == 22 :
      question = "departement n 22?"
      reponse = "Cotes-d Armor"
      b = 22
    if a == 23 :
      question = "departement n 23?"
      reponse = "Creuse"
      b = 23
    if a == 24 :
      question = "departement n 24?"
      reponse = "Dordogne"
      b = 24
    if a == 25 :
      question = "departement n 25?"
      reponse = "Doubs"
      b = 25
    if a == 26 :
      question = "departement n 26?"
      reponse = "Drome"
      b = 26
    if a == 27 :
      question = "departement n 27?"
      reponse = "Eure"
      b = 27
    if a == 28 :
      question = "departement n 28?"
      reponse = "Eure-et-Loir"
      b = 28
    if a == 29 :
      question = "departement n 29?"
      reponse = "Finistere"
      b = 29
    if a == 30 :
      question = "departement n 30?"
      reponse = "Gard"
      b = 30
    if a == 31 :
      question = "departement n 31?"
      reponse = "Haute-Garonne"
      b = 31
    if a == 32 :
      question = "departement n 32?"
      reponse = "Gers"
      b = 32
    if a == 33 :
      question = "departement n 33?"
      reponse = "Gironde"
      b = 33
    if a == 34 :
      question = "departement n 34?"
      reponse = "Herault"
      b = 34
    if a == 35 :
      question = "departement n 35?"
      reponse = "Ille-et-Vilaine"
      b = 35
    if a == 36 :
      question = "departement n 36?"
      reponse = "Indre"
      b = 36
    if a == 37 :
      question = "departement n 37?"
      reponse = "Indre-et-Loire"
      b = 37
    if a == 38 :
      question = "departement n 38?"
      reponse = "Isere"
      b = 38
    if a == 39 :
      question = "departement n 39?"
      reponse = "Jura"
      b = 39
    if a == 40 :
      question = "departement n 40?"
      reponse = "Landes"
      b = 40
    if a == 41 :
      question = "departement n 41?"
      reponse = "Loire-et-Cher"
      b = 41
    if a == 42 :
      question = "departement n 42?"
      reponse = "Loire"
      b = 42
    
    print(question)
    while keydown(KEY_OK) == True :
      sleep(0.1)
    while keydown(KEY_OK) == False :
      sleep(0.1)
    print(reponse)
    while keydown(KEY_OK) == True :
      sleep(0.1)
    sleep(0.5)