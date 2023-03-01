# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Create_organization.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Create_organization(object):
    def setupUi(self, Create_organization):
        Create_organization.setObjectName("Create_organization")
        Create_organization.setWindowModality(QtCore.Qt.NonModal)
        Create_organization.resize(500, 180)
        Create_organization.setMinimumSize(QtCore.QSize(500, 180))
        Create_organization.setMaximumSize(QtCore.QSize(500, 180))
        self.gridLayout = QtWidgets.QGridLayout(Create_organization)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.label_username_login_role = QtWidgets.QLabel(Create_organization)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_username_login_role.setFont(font)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout.addWidget(self.label_username_login_role, 0, 1, 1, 2)
        self.label_create_organization = QtWidgets.QLabel(Create_organization)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_create_organization.setFont(font)
        self.label_create_organization.setAlignment(QtCore.Qt.AlignCenter)
        self.label_create_organization.setObjectName("label_create_organization")
        self.gridLayout.addWidget(self.label_create_organization, 1, 0, 1, 3)
        self.lineEdit_organization_inn = QtWidgets.QLineEdit(Create_organization)
        self.lineEdit_organization_inn.setObjectName("lineEdit_organization_inn")
        self.gridLayout.addWidget(self.lineEdit_organization_inn, 4, 0, 1, 1)
        self.lineEdit_organization_name = QtWidgets.QLineEdit(Create_organization)
        self.lineEdit_organization_name.setText("")
        self.lineEdit_organization_name.setObjectName("lineEdit_organization_name")
        self.gridLayout.addWidget(self.lineEdit_organization_name, 3, 0, 1, 3)
        self.lineEdit_phone_number = QtWidgets.QLineEdit(Create_organization)
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")
        self.gridLayout.addWidget(self.lineEdit_phone_number, 4, 2, 1, 1)
        self.lineEdit_organization_kpp = QtWidgets.QLineEdit(Create_organization)
        self.lineEdit_organization_kpp.setObjectName("lineEdit_organization_kpp")
        self.gridLayout.addWidget(self.lineEdit_organization_kpp, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 1)
        self.pushButton_OK = QtWidgets.QPushButton(Create_organization)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 5, 2, 1, 1)
        self.pushButton_Cancel = QtWidgets.QPushButton(Create_organization)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 5, 1, 1, 1)

        self.retranslateUi(Create_organization)
        QtCore.QMetaObject.connectSlotsByName(Create_organization)
        Create_organization.setTabOrder(self.lineEdit_organization_name, self.lineEdit_organization_inn)
        Create_organization.setTabOrder(self.lineEdit_organization_inn, self.lineEdit_organization_kpp)
        Create_organization.setTabOrder(self.lineEdit_organization_kpp, self.lineEdit_phone_number)

    def retranslateUi(self, Create_organization):
        _translate = QtCore.QCoreApplication.translate
        Create_organization.setWindowTitle(_translate("Create_organization", "Event"))
        self.label_username_login_role.setText(_translate("Create_organization", "username_login_role"))
        self.label_create_organization.setText(_translate("Create_organization", "Создание новой организации"))
        self.lineEdit_organization_inn.setPlaceholderText(_translate("Create_organization", "ИНН"))
        self.lineEdit_organization_name.setPlaceholderText(_translate("Create_organization", "Наименование организации..."))
        self.lineEdit_phone_number.setPlaceholderText(_translate("Create_organization", "Телефон..."))
        self.lineEdit_organization_kpp.setPlaceholderText(_translate("Create_organization", "КПП"))
        self.pushButton_OK.setText(_translate("Create_organization", "ОК"))
        self.pushButton_Cancel.setText(_translate("Create_organization", "Отмена"))
