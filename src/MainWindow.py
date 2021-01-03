# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from SNMPEngine import *
from utilities import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Danjo's SNMP Tool")
        MainWindow.resize(705, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mibentry = QtWidgets.QLineEdit(self.centralwidget)
        self.mibentry.setObjectName("mibentry")
        self.gridLayout.addWidget(self.mibentry, 0, 3, 1, 1)
        self.setButton = QtWidgets.QPushButton(self.centralwidget)
        self.setButton.setObjectName("setButton")
        self.gridLayout.addWidget(self.setButton, 3, 3, 1, 1)
        self.valentry = QtWidgets.QLineEdit(self.centralwidget)
        self.valentry.setObjectName("valentry")
        self.gridLayout.addWidget(self.valentry, 2, 1, 1, 1)
        self.helpButton = QtWidgets.QPushButton(self.centralwidget)
        self.helpButton.setObjectName("helpButton")
        self.gridLayout.addWidget(self.helpButton, 5, 0, 1, 1)
        self.iplbl = QtWidgets.QLabel(self.centralwidget)
        self.iplbl.setObjectName("iplbl")
        self.gridLayout.addWidget(self.iplbl, 0, 0, 1, 1)
        self.miblbl = QtWidgets.QLabel(self.centralwidget)
        self.miblbl.setObjectName("miblbl")
        self.gridLayout.addWidget(self.miblbl, 0, 2, 1, 1)
        self.comlbl = QtWidgets.QLabel(self.centralwidget)
        self.comlbl.setObjectName("comlbl")
        self.gridLayout.addWidget(self.comlbl, 1, 0, 1, 1)
        self.comentry = QtWidgets.QLineEdit(self.centralwidget)
        self.comentry.setObjectName("comentry")
        self.gridLayout.addWidget(self.comentry, 1, 1, 1, 1)
        self.basicinfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.basicinfoButton.setObjectName("basicinfoButton")
        self.gridLayout.addWidget(self.basicinfoButton, 3, 1, 1, 1)
        self.vallbl = QtWidgets.QLabel(self.centralwidget)
        self.vallbl.setObjectName("vallbl")
        self.gridLayout.addWidget(self.vallbl, 2, 0, 1, 1)
        self.oidlbl = QtWidgets.QLabel(self.centralwidget)
        self.oidlbl.setObjectName("oidlbl")
        self.gridLayout.addWidget(self.oidlbl, 1, 2, 1, 1)
        self.ipentry = QtWidgets.QLineEdit(self.centralwidget)
        self.ipentry.setObjectName("ipentry")
        self.gridLayout.addWidget(self.ipentry, 0, 1, 1, 1)
        self.oidentry = QtWidgets.QLineEdit(self.centralwidget)
        self.oidentry.setObjectName("oidentry")
        self.gridLayout.addWidget(self.oidentry, 1, 3, 1, 1)
        self.getButton = QtWidgets.QPushButton(self.centralwidget)
        self.getButton.setObjectName("getButton")
        self.gridLayout.addWidget(self.getButton, 3, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 685, 349))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reslbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.reslbl.setText("")
        self.reslbl.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.reslbl.setObjectName("reslbl")
        self.horizontalLayout.addWidget(self.reslbl)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.basicinfoButton.clicked.connect(self.basicinfo)
        self.getButton.clicked.connect(self.get)
        self.setButton.clicked.connect(self.set)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Danjo's SNMP Tool", "Danjo's SNMP Tool"))
        self.setButton.setText(_translate("Danjo's SNMP Tool", "SET"))
        self.helpButton.setText(_translate("Danjo's SNMP Tool", "Help"))
        self.iplbl.setText(_translate("Danjo's SNMP Tool", "IP Address:"))
        self.miblbl.setText(_translate("Danjo's SNMP Tool", "MIB Path"))
        self.comlbl.setText(_translate("Danjo's SNMP Tool", "Community"))
        self.basicinfoButton.setText(_translate("Danjo's SNMP Tool", "Get Basic info"))
        self.vallbl.setText(_translate("Danjo's SNMP Tool", "New Value"))
        self.oidlbl.setText(_translate("Danjo's SNMP Tool", "OID"))
        self.getButton.setText(_translate("Danjo's SNMP Tool", "GET"))

    @pyqtSlot()
    def basicinfo(self):
        content = self.reslbl.text()
        if not checkemptystrings(self.ipentry.text()):
            towrite = basic_scan(self.ipentry.text())
            if content != '':
                self.reslbl.setText(content + '\n\n' + towrite)
            else:
                self.reslbl.setText(towrite)
        else:
            if content != '':
                self.reslbl.setText(content + '\n\n' + 'You must enter a IP to get information via SNMP!')
            else:
                self.reslbl.setText('You must enter an IP to get information via SNMP!')

    @pyqtSlot()
    def get(self):
        content = self.reslbl.text()
        ip = self.ipentry.text()
        mibpath = 'file:///' + self.mibentry.text()
        oid = self.oidentry.text()
        community = self.comentry.text()
        tempname = mibpath.split('/')
        mibname = tempname[-1]

        if not checkemptystrings(community, ip, mibname, mibpath, oid):
            if content != '':
                self.reslbl.setText(content + '\n\n' + get(community, ip, mibname, mibpath, oid))
            else:
                self.reslbl.setText(get(community, ip, mibname, mibpath, oid))
        else:
            if content != '':
                self.reslbl.setText(content + '\n\nSorry, you have to enter every required field in order to get an '
                                              'element!')
            else:
                self.reslbl.setText('Sorry, you have to enter every required field in order to get an element!')

    @pyqtSlot()
    def set(self):
        content = self.reslbl.text()

        community = self.comentry.text()
        ip_address = self.ipentry.text()
        mibpath = self.mibentry.text()
        oid = self.oidentry.text()
        new_val = self.valentry.text()
        tempname = mibpath.split('/')
        mibname = tempname[-1]

        if not checkemptystrings(community, ip_address, mibname, mibpath, oid):
            set(community, ip_address, mibname, mibpath, oid, new_val)
            if content != '':
                self.reslbl.setText(content + '\n\nSent SET request!\nResult via GET:' +
                                    get(community, ip_address, mibname, mibpath, oid))
            else:
                self.reslbl.setText('Sent SET request!\nResult via GET:' +
                                    get(community, ip_address, mibname, mibpath, oid))
        else:
            if content != '':
                self.reslbl.setText(content + '\n\n Sorry, you have to enter every required field in order to set a '
                                              'new value for an element!')
            else:
                self.reslbl.setText('Sorry, you have to enter every required field in order to get a new value for an '
                                    'element!')
