# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QSound


class Ui_Printing(object):
    def __init__(self, change_screen):
        self.change_screen = change_screen
        self.sound_effect = QSound(":/sounds/3d printer sounds.wav")
        self.playing = False

    def toggle_sound_effect(self):
        if self.sound_effect.isFinished(): self.playing = False

        if not self.playing:
            self.sound_effect.play()
            self.playing = True
        else:
            self.sound_effect.stop()
            self.playing = False

    def stop_sound_effect(self):
        if self.playing:
            self.sound_effect.stop()
        self.playing = False

    def add_buttons(self):
        self.pushButton.clicked.connect(lambda: self.change_screen.open_uses())
        self.pushButton.clicked.connect(lambda: self.stop_sound_effect())

        self.pushButton_2.clicked.connect(lambda: self.change_screen.open_plastics())
        self.pushButton_2.clicked.connect(lambda: self.stop_sound_effect())

        self.pushButton_3.clicked.connect(lambda: self.toggle_sound_effect())

    def setupUi(self, Printing):
        Printing.setObjectName("Printing")
        Printing.resize(402, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Printing)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Printing)
        #       self.label.setPixmap(QtGui.QPixmap(":/sounds/3d printer sounds.wav"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("main_label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Printing)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Printing)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(Printing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Printing)
        self.add_buttons()
        QtCore.QMetaObject.connectSlotsByName(Printing)

    def retranslateUi(self, Printing):
        _translate = QtCore.QCoreApplication.translate
        Printing.setWindowTitle(_translate("Printing", "Form"))
        self.label.setText(_translate("Printing", "3D printing is cool. This app, which has taken 3.2 billion man-hours and $87 trillion USD to develop, will teach you literally everything you need to know about it."))
        self.pushButton.setText(_translate("Printing", "Uses"))
        self.pushButton_2.setText(_translate("Printing", "Plastics"))
        self.pushButton_3.setText(_translate("Printing", "Listen to a 3D printer"))


import resources.main_rc
