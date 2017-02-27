# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nfatodfa.ui'
#
# Created: Tue Feb 21 22:45:09 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from package import nfatodfa


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class NFA2DFA(QtGui.QMainWindow):
    def __init__(self):
        super(NFA2DFA, self).__init__()
        self.setupUi(self)
        self.show_app()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(385, 230)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(385, 230))
        MainWindow.setMaximumSize(QtCore.QSize(385, 230))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 91, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 91, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 70, 281, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 30, 95, 32))
        self.pushButton.setStatusTip(_fromUtf8(""))

        self.pushButton.clicked.connect(self.select_input_file)
        
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 100, 95, 32))

        self.pushButton_2.clicked.connect(self.select_output_file)
        
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(-10, 140, 421, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 160, 95, 32))

        self.pushButton_3.clicked.connect(self.execute)
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 385, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Projet Traduction des Langages", None))
        self.label.setText(_translate("MainWindow", "Entrée NFA", None))
        self.label_2.setText(_translate("MainWindow", "Sortie DFA", None))
        self.pushButton.setText(_translate("MainWindow", "Sélectionner", None))
        self.pushButton_2.setText(_translate("MainWindow", "Sélectionner", None))
        self.pushButton_3.setText(_translate("MainWindow", "Exécuter", None))

    def select_input_file(self):
        self.infile = \
            QtGui.QFileDialog.getOpenFileName(self, "Select input file")

    def select_output_file(self):
        self.outfile = \
            QtGui.QFileDialog.getSaveFileName(self, "Select output file", '', "Text files (*.txt)")

    def display_info(self, info):
        QtGui.QMessageBox.information(self.centralwidget, "Informations", info)

    def display_error(self, error):
        QtGui.QMessageBox.critical(self.centralwidget, "Error!", error)
    
    def execute(self):
        try:
            test1 = open(self.infile, 'r')
        except FileNotFoundError as e:
                self.display_error(e.strerror)
                self.display_error("Fichiers inexistants! Verifiez à nouveau!")
        else:
            nfatodfa.main(self.infile, self.outfile)
            self.display_info("Transformation de NFA en DFA faite avec succès")

    def show_app(self):
        self.show()


class Application(object):

    def __init__(self):
        self.app = QtGui.QApplication(["NFA2DFA"])

    def execution(self):
        self.app.exec_()


def main():
    application = Application()
    ui = NFA2DFA()
    application.execution()


