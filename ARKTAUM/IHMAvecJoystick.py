

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import threading
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget,QGridLayout,QMainWindow,QApplication
import sys
from enum import Enum

global DirectionActuelle
global VitesseActuelle

global DIR
global DIR2
global STEP
global STEP2
global CW
global CCW

DIR=1       #pin pour la chenille droite
DIR2=2      #pin pour la chenille gauche
STEP=3      #pin pour la chenille droite
STEP2=4     #pin pour la chenille gauche
CW=1  #horaire par rapport a la face droite
CCW=0 #horaire par rapport a la face gauche 

class Direction(Enum):
    Left=0
    Right=1
    Up=2
    Down=3
    Static=4

DirectionActuelle=Direction(4)
VitesseActuelle=0

cap=cv2.VideoCapture(0)

def threaded(fn):#preparation du thread qui refresh l'image de la caméra a mettre dans la classe
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args,kwargs=kwargs).start()
    return wrapper

def ThreadVideo():
    while True:
        ret,img=cap.read()
        time.sleep(0.3)
        #cv2.imshow('Video',img)
        cv2.imwrite('TestsZ3/ARKTAUM/ImageVideo.jpg',img)
        #Ui_MainWindow.label_7.setPixmap(QtGui.QPixmap("TestsZ3/ARKTAUM/ImageVideo.jpg"))
        if(cv2.waitKey(10)& 0xFF==ord('b')):
            break


class Ui_MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.joystick=Joystick(self)
        _widget=QWidget()
        _layout=QGridLayout(_widget)
        _layout.addWidget(self.joystick)
        self.setCentralWidget(_widget)

    def setupUi(self, MainWindow):
        #fenêtre par défault
        longueur=1080
        hauteur=720

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(longueur,hauteur)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.joystick=Joystick(self.centralwidget)
        self.joystick.setGeometry(QtCore.QRect(int(longueur/2)-50, int(hauteur/2), 41, 241))
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(int(longueur/3), int(hauteur/2), 41, 241))
        self.verticalSlider.setMinimum(-1000)
        self.verticalSlider.setMaximum(1000)
        self.verticalSlider.setProperty("value", 1)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(int(longueur/3)*2,int(hauteur/2), 41, 241))
        self.verticalSlider_2.setMinimum(-1000)
        self.verticalSlider_2.setMaximum(1000)
        self.verticalSlider_2.setProperty("value", 1)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(int(longueur/5), 520, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(int(longueur/5)*4, 520, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 540, 81, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 550, 81, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(int(longueur/5), 350, 131, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(int(longueur/5)*4, 350, 131, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(int(longueur/4), int(hauteur/24), 581, 301))
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap('TestsZ3/ARKTAUM/ImageVideo.jpg'))
        self.label_7.setScaledContents(True)
        self.label_7.setStyleSheet("border: 3px solid black;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(int(longueur/7)*3, int(hauteur/10)*9, 300, 65))
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap('TestsZ3/ARKTAUM/LogoARKTAUM.JPG'))
        self.label_8.setScaledContents(True)
        self.label_8.setStyleSheet("border: 3px solid black;")
        self.label_8.setObjectName("label_8")
        #couleur de l'arriere plan
        MainWindow.setStyleSheet("background-color: rgb(96,96,96);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contrôle téléopéré ARKTAUM"))
        self.label.setText(_translate("MainWindow", "Vitesse Gauche:"))
        self.label_2.setText(_translate("MainWindow", "Vitesse Droite:"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Curseur vitesse Gauche"))
        self.label_6.setText(_translate("MainWindow", "Curseur vitesse Droite"))

    @threaded
    def refreshCam(self):#thread pour le refresh de la caméra
            while True:
                time.sleep(0.3)
                self.label_7.setPixmap(QtGui.QPixmap('TestsZ3/ARKTAUM/ImageVideo.jpg'))
                self.label_7.setScaledContents(True)




x=threading.Thread(target=ThreadVideo)
x.start()


## Joystick dépendant de la fenetre principale
class Joystick(QWidget):

    global VitesseActuelle
    global DirectionActuelle

    def __init__(self, parent):
        super(Joystick,self).__init__(parent)

        self.setMinimumSize(210,210)
        self.movingOffset=QPoint(0,0)
        self.grabCenter=False
        self.__maxDistance=70

    def paintEvent(self, event):
        painter=QPainter(self)
        bounds=QRect(-self.__maxDistance, -self.__maxDistance,self.__maxDistance*2,self.__maxDistance*2).translated(self._center())
        painter.drawEllipse(bounds)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self._centerEllipse())

    def _centerEllipse(self):
        if self.grabCenter:
            return QRectF(-30,-30,60,60).translated(self.movingOffset)
        return QRectF(-30,-30,60,60).translated(self._center())

    def _center(self):
        return QPoint(self.width()/2,self.height()/2)

    def _boundJoystick(self,point):
        limitLine=QLineF(self._center(),point)
        if (limitLine.length()>self.__maxDistance):
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()

    def joystickDirection(self):

        global VitesseActuelle
        global DirectionActuelle
        
        if not self.grabCenter:
            return 0
        normVector=QLineF(self._center(),self.movingOffset)
        currentDistance=normVector.length()
        angle=normVector.angle()

        distance=min(currentDistance/self.__maxDistance,1.0)
        VitesseActuelle=distance*1200 #1200 etant le nombre de ticks par seconde de la vitesse max limitée du robot

        if 45<=angle<135:
            DirectionActuelle=Direction.Up
            return(Direction.Up,distance)
        elif 135<=angle<225:
            DirectionActuelle=Direction.Left
            return(Direction.Left,distance)
        elif 225<=angle<315:
            DirectionActuelle=Direction.Down
            return(Direction.Down,distance)
        DirectionActuelle=Direction.Right
        return(Direction.Right,distance)
        

    def mousePressEvent(self,ev):
        self.grabCenter=self._centerEllipse().contains(ev.pos())
        return super().mousePressEvent(ev)

    def mouseReleaseEvent(self, event):
        self.grabCenter=False
        self.movingOffset=QPointF(0,0)
        self.update()


    def mouseMoveEvent(self,event):
        if self.grabCenter:
            print("Mouvement")
            self.movingOffset=self._boundJoystick(event.pos())
            self.update()
        print(self.joystickDirection())


##threads des fonctions de navigation

def directionThread(fn2):#preparation du thread qui refresh l'image de la caméra a mettre dans la classe
    def wrapperDirection(*args, **kwargs):
        threading.Thread(target=fn2, args=args,kwargs=kwargs).start()
    return wrapperDirection

def vitesseThread(fn3):#preparation du thread qui refresh l'image de la caméra a mettre dans la classe
    def wrapperVitesse(*args, **kwargs):
        threading.Thread(target=fn3, args=args,kwargs=kwargs).start()
    return wrapperVitesse

##FONCTIONS DE NAVIGATION
class Navigation(object):#a appeler dès le setup de la fenêtre principale

    """
    def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(STEP,GPIO.OUT)
        GPIO.setup(DIR,GPIO.OUT)
        GPIO.setup(STEP2,GPIO.OUT)
        GPIO.setup(DIR2,GPIO.OUT)
        ## sens de rotation initial ( les 2 voies vers l'avant)
        GPIO.output(DIR,CW)
        GPIO.output(DIR2,CCW)
        #les moteurs sont montés 2 a 2 sur des faces qui s'opposent, sinon on aurait 2 fois CW
    """

    @threaded
    ##fonction de choix directionnel
    def direction(self):

        
        global DirectionActuelle
        global DIR
        global DIR2
        global CW
        global CCW
        while True:
            if (DirectionActuelle==Direction.Up):
                DIR=CW
                DIR2=CCW
                if (DirectionActuelle!=Direction.Up):
                    break
            ##meme chose pour les autres directions
            if (DirectionActuelle==Direction.Left):
                DIR=CW
                DIR2=CW
                if (DirectionActuelle!=Direction.Left):
                    break
            if (DirectionActuelle==Direction.Right):
                DIR=CCW
                DIR2=CCW
                if (DirectionActuelle!=Direction.Right):
                    break
            if (DirectionActuelle==Direction.Down):
                DIR=CCW
                DIR2=CW
                if (DirectionActuelle!=Direction.Down):
                    break

    @threaded
    #fonction de choix de pallier de vitesse
    def vitesse(self):
        global VitesseActuelle
        while True:
            if (VitesseActuelle<100):
                time.sleep(1/VitesseActuelle)
                #GPIO.output(STEP,GPIO.HIGH)
                #GPIO.output(STEP2,GPIO.HIGH)
                time.sleep(1/VitesseActuelle)
                #GPIO.output(STEP,GPIO.LOW)
                #GPIO.output(STEP2,GPIO.LOW)
                if (VitesseActuelle>=100):
                    break
            if (100<=VitesseActuelle<=400):
                time.sleep(1/VitesseActuelle)
                #GPIO.output(STEP,GPIO.HIGH)
                #GPIO.output(STEP2,GPIO.HIGH)
                time.sleep(1/VitesseActuelle)
                #GPIO.output(STEP,GPIO.LOW)
                #GPIO.output(STEP2,GPIO.LOW)
                if ((VitesseActuelle<=100) or (VitesseActuelle>401)):
                    break
            if (400<VitesseActuelle<=800):
                time.sleep(1/VitesseActuelle)
                #GPIO.output(STEP,GPIO.HIGH)
                #GPIO.output(STEP2,GPIO.HIGH)
                time.sleep(1/VitesseActuelle)
                #GPIO.output(STEP,GPIO.LOW)
                #GPIO.output(STEP2,GPIO.LOW)
                if ((VitesseActuelle<=400) or (VitesseActuelle>801)):
                    break
            if (800<VitesseActuelle<=1200):
                time.sleep(1/VitesseActuelle)
                #GPIO.output(STEP,GPIO.HIGH)
                #GPIO.output(STEP2,GPIO.HIGH)
                time.sleep(1/VitesseActuelle)
                #GPIO.output(STEP,GPIO.LOW)
                #GPIO.output(STEP2,GPIO.LOW)
                if (VitesseActuelle<=800):
                    break
            
            


##test d'affichage de changement de données de navigation

def printActuel():
    while 1:
        time.sleep(1)
        print(DirectionActuelle)
        print(VitesseActuelle)
    
z=threading.Thread(target=printActuel)
z.start()

## fin de test d'affichage 


if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.refreshCam()
        #app.setStyle(QStyleFactory.create("Cleanlooks"))
    
    """ui.setWindowTitle('Joystick ')

    cw=QWidget()
    ml=QGridLayout()
    cw.setLayout(ml)
    ui.setCentralWidget(cw)

    joystick=Joystick(None)

    ml.addWidget(joystick,400,400)

    ui.show()
    """

    MainWindow.show()
    app.exec_()
    
    


    #if(sys.flags.interactive !=1):#or not hasattr(QtCore, 'PYQT_VERSION'):
    #    QApplication.instance().exec_()