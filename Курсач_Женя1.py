
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

        
while True:

 class Medicaments:
     """ Медикаменты от головы """
     def citramon (self, event):
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.golova
         self.ui.background.setPixmap(QtGui.QPixmap('Цитрамон.png'))

     def ibyprofen (self, event): 
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.golova
         self.ui.background.setPixmap(QtGui.QPixmap('iby.png'))

     def tempalgin (self, event):
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.golova
         self.ui.background.setPixmap(QtGui.QPixmap('temp.png'))

     """ Обезболивающие """
     def naiz (self, event):
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.zneb
         self.ui.background.setPixmap(QtGui.QPixmap('naiz.png'))

     def nimisil (self, event):
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.zneb
         self.ui.background.setPixmap(QtGui.QPixmap('nimisil.png'))

     def keterol (self, event):
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.zneb
         self.ui.background.setPixmap(QtGui.QPixmap('Keterol.png'))


     """ Антиспетики """
     def AXD (self, event):
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.anti
         self.ui.background.setPixmap(QtGui.QPixmap('AXD.png'))

     def perekis (self, event):
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.anti
         self.ui.background.setPixmap(QtGui.QPixmap('perekis.png'))

     def spasitel (self, event):
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.back.mousePressEvent = self.anti
         self.ui.background.setPixmap(QtGui.QPixmap('Рят.png'))


 class Types_of_medicaments(Medicaments):
     """ Типы медикаментов """
     def golova(self, event): #от головы
         self.ui.back.show()
         self.ui.back.mousePressEvent = self.choose
         self.ui.background.setPixmap(QtGui.QPixmap('font.png'))

         self.ui.button1.show()
         self.ui.button1.setText('Цитрамон')
         self.ui.button1.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button1.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button1.clicked.connect(self.citramon)

         self.ui.button2.show()
         self.ui.button2.setText('Ібупрофен')
         self.ui.button2.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button2.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button2.clicked.connect(self.ibyprofen)

         self.ui.button3.show()
         self.ui.button3.setText('Темпалгін')
         self.ui.button3.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button3.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button3.clicked.connect(self.tempalgin)

     def zneb(self, event): #обезболивающие
         self.ui.back.show()
         self.ui.back.mousePressEvent = self.choose
         self.ui.background.setPixmap(QtGui.QPixmap('font.png'))

         self.ui.button1.show()
         self.ui.button1.setText('Найз')
         self.ui.button1.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button1.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button1.clicked.connect(self.naiz)

         self.ui.button2.show()
         self.ui.button2.setText('Кетерол')
         self.ui.button2.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button2.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button2.clicked.connect(self.keterol)

         self.ui.button3.show()
         self.ui.button3.setText('Німесил')
         self.ui.button3.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button3.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button3.clicked.connect(self.nimisil)

     def anti(self, event): #антисептики
         self.ui.back.show()
         self.ui.back.mousePressEvent = self.choose
         self.ui.background.setPixmap(QtGui.QPixmap('font.png'))

         self.ui.button1.show()
         self.ui.button1.setText('АХД 2000')
         self.ui.button1.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button1.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button1.clicked.connect(self.AXD)

         self.ui.button2.show()
         self.ui.button2.setText('Перекис водню')
         self.ui.button2.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button2.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button2.clicked.connect(self.perekis)

         self.ui.button3.show()
         self.ui.button3.setText('Рятівник')
         self.ui.button3.setStyleSheet('QPushButton {background-color: #C4C4C4; color: white;}')
         self.ui.button3.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button3.clicked.connect(self.spasitel)

 class About_app:
     """ Инфо про приложение """
     def info(self, event):
         self.ui.info.hide()
         self.ui.back.show()
         self.ui.background.setPixmap(QtGui.QPixmap('help_w.png'))
         self.ui.back.mousePressEvent = self.choose
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()

 class Pain_type_selection(About_app, Types_of_medicaments):
     """ Выбор типа боли """
     def choose(self, event):
         self.ui.info.show()
         self.ui.back.hide()

         self.ui.button1.show()
         self.ui.button1.setText('Головний біль')
         self.ui.button1.setStyleSheet('QPushButton {background-color: #A31414; color: white;}')
         self.ui.button1.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button1.clicked.connect(self.golova)

         self.ui.button2.show()
         self.ui.button2.setText('Знеболюючі')
         self.ui.button2.setStyleSheet('QPushButton {background-color: #1489A3; color: white;}')
         self.ui.button2.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button2.clicked.connect(self.zneb)

         self.ui.button3.show()
         self.ui.button3.setText('Антисептики')
         self.ui.button3.setStyleSheet('QPushButton {background-color: #A0A314; color: white;}')
         self.ui.button3.setFont(QtGui.QFont("Roboto", 18, QtGui.QFont.Medium))
         self.ui.button3.clicked.connect(self.anti)

         self.ui.start_button.hide()
         self.ui.background.setPixmap(QtGui.QPixmap('choose.png'))
         self.ui.info.mousePressEvent = self.info

 class Start(Pain_type_selection):
    """ Class-constructor """
    def __init__(self):
         self.ui = uic.loadUi('qt.ui')
         self.ui.background.setPixmap(QtGui.QPixmap('start.png'))
         self.ui.back.setPixmap(QtGui.QPixmap('Arrow 1.png'))
         self.ui.info.setPixmap(QtGui.QPixmap('help.png'))
         self.ui.start_button.clicked.connect(self.choose)
         self.ui.info.hide()
         self.ui.back.hide()
         self.ui.button1.hide()
         self.ui.button2.hide()
         self.ui.button3.hide()
         self.ui.show()




 if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Start()
    sys.exit(app.exec_())


