# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SendMessageUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SendMessageForm(object):
    def setupUi(self, SendMessageForm):
        SendMessageForm.setObjectName("SendMessageForm")
        SendMessageForm.resize(416, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Core/Core/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SendMessageForm.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(SendMessageForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message_area = QtWidgets.QTextBrowser(SendMessageForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.message_area.setFont(font)
        self.message_area.setOpenExternalLinks(True)
        self.message_area.setObjectName("message_area")
        self.verticalLayout.addWidget(self.message_area)
        self.send_message_layout = QtWidgets.QHBoxLayout()
        self.send_message_layout.setObjectName("send_message_layout")
        self.message_input = QtWidgets.QLineEdit(SendMessageForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_input.sizePolicy().hasHeightForWidth())
        self.message_input.setSizePolicy(sizePolicy)
        self.message_input.setObjectName("message_input")
        self.send_message_layout.addWidget(self.message_input)
        self.send = QtWidgets.QPushButton(SendMessageForm)
        self.send.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send.sizePolicy().hasHeightForWidth())
        self.send.setSizePolicy(sizePolicy)
        self.send.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.send.setFont(font)
        self.send.setObjectName("send")
        self.send_message_layout.addWidget(self.send)
        self.verticalLayout.addLayout(self.send_message_layout)

        self.retranslateUi(SendMessageForm)
        self.send.clicked.connect(SendMessageForm.send_message) # type: ignore
        self.message_input.textChanged['QString'].connect(SendMessageForm.update_input_text) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SendMessageForm)

    def retranslateUi(self, SendMessageForm):
        _translate = QtCore.QCoreApplication.translate
        SendMessageForm.setWindowTitle(_translate("SendMessageForm", "Messaging"))
        self.send.setText(_translate("SendMessageForm", "Send"))
        self.send.setShortcut(_translate("SendMessageForm", "Return"))
from Resources import Resources