#AUTEUR: Charles PAGANEL

#but du programme : Programme sur linux Ubuntu 20.04 pour tester les coordinations contrôle commande vers mouvements moteurs pour
#contrôle téléopéré

#import RPI.GPIO as GPIO
import time
import threading
import keyboard
import numpy as np
DIR1=1       #pin pour la chenille droite
DIR2=2      #pin pour la chenille gauche
STEP1=3      #pin pour la chenille droite
STEP2=4     #pin pour la chenille gauche
CW=1  #horaire par rapport a la face droite
CCW=0 #horaire par rapport a la face gauche 

global vitesseDroite
global vitesseGauche
vitesseDroite=1
vitesseGauche=1
"""
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(STEP1,GPIO.OUT)
    GPIO.setup(DIR1,GPIO.OUT)
    GPIO.setup(STEP2,GPIO.OUT)
    GPIO.setup(DIR2,GPIO.OUT)
    ## sens de rotation initial ( les 2 voies vers l'avant)
    GPIO.output(DIR1,CW)
    GPIO.output(DIR2,CCW)
    #les moteurs sont montés 2 a 2 sur des faces qui s'opposent, sinon on aurait 2 fois CW
"""
def mouvementJoystick():
    ##avancer
    ##reculer
    print('')

def mouvementChenille():#prend en entrée une vitesse de la chenille droite selon l'ihm
#et une vitesse de la chenille gauche selon l'IHM le tout dans un thread
#avec des vitesse entières pour l instant portées de -1000 a 1000 sans le zéro
    if ((vitesseDroite and vitesseGauche)!=0):
        delaiDroit=1/vitesseDroite#avec delaiDroit différent de 0
        delaiGauche=1/vitesseGauche#avec delaiGauche différent de 0
        while True:
            #setup de la direction
            #time.sleep(1.0)
            if (np.sign(vitesseDroite)==1):#si la vitesse de la chenille droite est positive
                #GPIO.output(DIR1,CW)
                print("la chenille droite avance")
            else:
                #GPIO.output(DIR1,CCW)
                print("la chenille droite recule")
            if (np.sign(vitesseGauche)==1):#si la vitesse de la chenille droite est positive
                #GPIO.output(DIR2,CW)
                print("la chenille gauche avance")
            else:
                #GPIO.output(DIR2,CCW)
                print("la chenille gauche recule")
            #envoi des données de vitesse
            #pour la chenille droite
            #GPIO.output(STEP1,GPIO.HIGH)
            time.sleep(abs(delaiDroit))
            #GPIO.output(STEP1,GPIO.LOW)
            time.sleep(abs(delaiDroit))
            #pour la chenille gauche
            #GPIO.output(STEP2,GPIO.HIGH)
            time.sleep(abs(delaiGauche))
            #GPIO.output(STEP2,GPIO.LOW)
            time.sleep(abs(delaiGauche))

x=threading.Thread(target=mouvementChenille)
x.start()

while True:
    if keyboard.is_pressed("e"):
        #print("appui sur e, on augmente la vitesse de la chenille droite ")
        vitesseDroite=vitesseDroite+100
        
    if keyboard.is_pressed("d"):
        #print("appui sur d, on diminue la vitesse de la chenille droite ")
        vitesseDroite=vitesseDroite-100

    if keyboard.is_pressed("a"):
        #print("appui sur a, on augmente la vitesse de la chenille gauche ")
        vitesseGauche=vitesseGauche+100
        
    if keyboard.is_pressed("q"):
        #print("appui sur q, on diminue la vitesse de la chenille gauche ")
        vitesseGauche=vitesseGauche-100

    #print(vitesseDroite)
    #print(vitesseGauche)