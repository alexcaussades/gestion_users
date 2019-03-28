#copy AlexCaussades alecaussades <at> gmail.com

import os
import datetime
import socket
import time

chemin = '/home/'+ os.getlogin() +'/Bureau/test.txt' #version linux

def loading():
    print("Mise en place de l'instance....")
    print ("Chargement des fichiers de configuration...")

def good():
    print ("Tout est prêt Allons-y !")


x = datetime.datetime.now()
y = x.strftime("%x %X")
speudo = input ("Entrée le speudo du jouer : ")
speudoInfo = speudo #demarage de l'instance




dic = {"bn": "Ban", "to": "Time Out", "sr": "Search", "srf": "recherche" } #dictionaire serveur

class Global():
    def __init__(self, speudo=speudo):
        self.speudo = speudo  
    
    def Action(self, speudo=speudo):
        self.speudo = speudo
        print ("l'action sur le joueur {0} a bien était éffectuer !".format(self.speudo))
    
    def Ban(self, speudo=speudo):
        self.speudo = speudo
        f = open(chemin, 'a')
        f.write("Date: " + y + ", Name: " + os.getlogin() + ", ban: " + self.speudo + ", Raison: " + self.raison + "\r")
        print ("Ajout Effectuer pour le {0} de {1}".format(dic.get('bn'), self.speudo))

    def To(self, speudo=speudo):
        self.speudo = speudo
        f = open(chemin, 'a')
        f.write("Date: " + y + ", Name: " + os.getlogin() + ", timeOut: " + self.speudo + ", Raison: " + self.raison + "\r")
        print ("Ajout Effectuer pour le {0} de {1}".format(dic.get('to'), self.speudo))

    def Raison(self, speudo=speudo):
        self.speudo = speudo
        raison = input ("Entrée la raison : ")
        self.raison = raison

    def Recherche(self, speudo=speudo):
        self.speudo = speudo
        print('Lancement de la {0}'.format(dic.get('srf')))
        time.sleep(1.5)
        f = open(chemin, 'r', encoding="utf-8")
        for i in f:
            if self.speudo in i:
                print(str(i))


loading()
time.sleep(0.5)
good()
time.sleep(0.5)
speudoInfo = Global(speudo=speudo)
bn = "Ban"
to = "Time_Out"
sr = "Search"

i = bn + to + sr

while i :

        a = input ("Entrée votre option (1) {0}, (2) {1}, (3) {2} :  ".format(bn, to, sr))
            
        if a == str(1):
            speudoInfo.Raison(speudo=speudo)
            speudoInfo.Ban(speudo=speudo)
            speudoInfo.Action(speudo=speudo)
            break

        elif  a == str(2):
            speudoInfo.Raison(speudo=speudo)
            speudoInfo.To(speudo=speudo)
            speudoInfo.Action(speudo=speudo)
            break

        else :
            speudoInfo.Recherche(speudo=speudo)
            break
