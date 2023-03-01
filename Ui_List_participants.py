# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_List_participants.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_List_participants(object):
    def setupUi(self, List_participants):
        List_participants.setObjectName("List_participants")
        List_participants.resize(1150, 600)
        self.gridLayout_3 = QtWidgets.QGridLayout(List_participants)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tree_participants_list = QtWidgets.QTreeWidget(List_participants)
        self.tree_participants_list.setObjectName("tree_participants_list")
        self.tree_participants_list.headerItem().setText(0, "1")
        self.gridLayout_3.addWidget(self.tree_participants_list, 6, 0, 1, 7)
        self.pushButton_delete_participant = QtWidgets.QPushButton(List_participants)
        self.pushButton_delete_participant.setObjectName("pushButton_delete_participant")
        self.gridLayout_3.addWidget(self.pushButton_delete_participant, 3, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_find_participant = QtWidgets.QPushButton(List_participants)
        self.pushButton_find_participant.setObjectName("pushButton_find_participant")
        self.gridLayout_2.addWidget(self.pushButton_find_participant, 0, 2, 1, 1)
        self.lineEdit_find_participant = QtWidgets.QLineEdit(List_participants)
        self.lineEdit_find_participant.setObjectName("lineEdit_find_participant")
        self.gridLayout_2.addWidget(self.lineEdit_find_participant, 0, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 8, 0, 1, 2)
        self.pushButton_create_participant = QtWidgets.QPushButton(List_participants)
        self.pushButton_create_participant.setObjectName("pushButton_create_participant")
        self.gridLayout_3.addWidget(self.pushButton_create_participant, 3, 0, 1, 1)
        self.pushButton_export_xls = QtWidgets.QPushButton(List_participants)
        self.pushButton_export_xls.setObjectName("pushButton_export_xls")
        self.gridLayout_3.addWidget(self.pushButton_export_xls, 7, 3, 1, 1)
        self.pushButton_edit_participant = QtWidgets.QPushButton(List_participants)
        self.pushButton_edit_participant.setObjectName("pushButton_edit_participant")
        self.gridLayout_3.addWidget(self.pushButton_edit_participant, 3, 1, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(List_participants)
        self.pushButton_close.setObjectName("pushButton_close")
        self.gridLayout_3.addWidget(self.pushButton_close, 8, 6, 1, 1)
        self.label_find_event = QtWidgets.QLabel(List_participants)
        self.label_find_event.setObjectName("label_find_event")
        self.gridLayout_3.addWidget(self.label_find_event, 7, 0, 1, 2)
        self.label_username_login_role = QtWidgets.QLabel(List_participants)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_username_login_role.setFont(font)
        self.label_username_login_role.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_username_login_role.setObjectName("label_username_login_role")
        self.gridLayout_3.addWidget(self.label_username_login_role, 0, 5, 1, 2)
        self.label_participants_list = QtWidgets.QLabel(List_participants)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_participants_list.setFont(font)
        self.label_participants_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_participants_list.setObjectName("label_participants_list")
        self.gridLayout_3.addWidget(self.label_participants_list, 0, 2, 1, 3)
        self.label = QtWidgets.QLabel(List_participants)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 3, 3, 1, 4)

        self.retranslateUi(List_participants)
        self.pushButton_create_participant.clicked.connect(List_participants.show) # type: ignore
        self.pushButton_delete_participant.clicked.connect(List_participants.show) # type: ignore
        self.pushButton_export_xls.clicked.connect(List_participants.showMaximized) # type: ignore
        self.pushButton_find_participant.clicked.connect(self.tree_participants_list.expandAll) # type: ignore
        self.pushButton_edit_participant.clicked.connect(List_participants.show) # type: ignore
        self.pushButton_close.clicked.connect(List_participants.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(List_participants)
        List_participants.setTabOrder(self.tree_participants_list, self.pushButton_create_participant)
        List_participants.setTabOrder(self.pushButton_create_participant, self.pushButton_edit_participant)
        List_participants.setTabOrder(self.pushButton_edit_participant, self.lineEdit_find_participant)
        List_participants.setTabOrder(self.lineEdit_find_participant, self.pushButton_find_participant)
        List_participants.setTabOrder(self.pushButton_find_participant, self.pushButton_export_xls)
        List_participants.setTabOrder(self.pushButton_export_xls, self.pushButton_close)
        List_participants.setTabOrder(self.pushButton_close, self.pushButton_delete_participant)

    def retranslateUi(self, List_participants):
        _translate = QtCore.QCoreApplication.translate
        List_participants.setWindowTitle(_translate("List_participants", "Event"))
        self.pushButton_delete_participant.setText(_translate("List_participants", "Удалить участника"))
        self.pushButton_find_participant.setText(_translate("List_participants", "Найти"))
        self.lineEdit_find_participant.setPlaceholderText(_translate("List_participants", "Поиск участника"))
        self.pushButton_create_participant.setText(_translate("List_participants", "Создать участника"))
        self.pushButton_export_xls.setText(_translate("List_participants", "Export xls"))
        self.pushButton_edit_participant.setText(_translate("List_participants", "Редактировать участника"))
        self.pushButton_close.setText(_translate("List_participants", "Закрыть"))
        self.label_find_event.setText(_translate("List_participants", "Фильтры поиска участника:"))
        self.label_username_login_role.setText(_translate("List_participants", "username_login_role"))
        self.label_participants_list.setText(_translate("List_participants", "Общий список всех участников"))
        self.label.setText(_translate("List_participants", "Внимание! Удаление участника повлечет удаление всех его документов из БД."))
