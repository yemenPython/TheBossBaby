# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default_mode.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(3, 0, 3, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.list_widget = QtWidgets.QListWidget(Form)
        self.list_widget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.list_widget.setStyleSheet("QListWidget {\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    background: transparent;\n"
"}")
        self.list_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list_widget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.list_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_widget.setAutoScroll(False)
        self.list_widget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.list_widget.setGridSize(QtCore.QSize(0, 58))
        self.list_widget.setWordWrap(True)
        self.list_widget.setObjectName("list_widget")
        self.gridLayout.addWidget(self.list_widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.list_widget.setSortingEnabled(True)
