


from turtle import width
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import threading
import time


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


class Ui_MainWindow(object):
    

    def setupUi(self, MainWindow):
        #fenêtre par défault
        longueur=1080
        hauteur=720

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(longueur,hauteur)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.refreshCam()
    MainWindow.show()
    sys.exit(app.exec_())
    