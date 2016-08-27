# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_portal_usr.ui'
#
# Created: Sat Aug 27 03:53:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mostrador(object):
    def setupUi(self, mostrador):
        mostrador.setObjectName("mostrador")
        mostrador.resize(659, 462)
        self.label = QtGui.QLabel(mostrador)
        self.label.setGeometry(QtCore.QRect(10, 10, 641, 81))
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(mostrador)
        self.lineEdit.setGeometry(QtCore.QRect(40, 160, 181, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox = QtGui.QGroupBox(mostrador)
        self.groupBox.setGeometry(QtCore.QRect(260, 100, 261, 80))
        self.groupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 221, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_2 = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.label_2 = QtGui.QLabel(mostrador)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 181, 41))
        self.label_2.setFrameShape(QtGui.QFrame.Box)
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setMargin(0)
        self.label_2.setObjectName("label_2")
        self.listView = QtGui.QListView(mostrador)
        self.listView.setGeometry(QtCore.QRect(20, 200, 621, 251))
        self.listView.setObjectName("listView")
        self.pushButton = QtGui.QPushButton(mostrador)
        self.pushButton.setGeometry(QtCore.QRect(530, 130, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(mostrador)
        QtCore.QMetaObject.connectSlotsByName(mostrador)

    def retranslateUi(self, mostrador):
        mostrador.setWindowTitle(QtGui.QApplication.translate("mostrador", "ui_portal_usr", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mostrador", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#20197f;\">Bienvenido al Revisor de Noticias!</span></p><p align=\"center\"><span style=\" font-size:12pt; font-style:italic;\">Filtre según contenido o publicaciones</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("mostrador", "Estado Noticias", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("mostrador", "Publicadas", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("mostrador", "No Publicadas", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mostrador", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-style:italic;\">Filtro por Contenido</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("mostrador", "Volver", None, QtGui.QApplication.UnicodeUTF8))

