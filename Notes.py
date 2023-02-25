# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(567, 516)
        Form.setStyleSheet("background-color: rgb(222, 190, 62);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.botao_voltar = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_voltar.setFont(font)
        self.botao_voltar.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    border-radius: 5px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(186, 241, 249)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(53, 218, 255);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/Icons/189260.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_voltar.setIcon(icon)
        self.botao_voltar.setObjectName("botao_voltar")
        self.horizontalLayout_5.addWidget(self.botao_voltar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setStyleSheet("background-color: rgb(222, 190, 62);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.nome_arquivo_edit = QtWidgets.QLineEdit(self.page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nome_arquivo_edit.setFont(font)
        self.nome_arquivo_edit.setStyleSheet("border: opx solid rgb(0, 0, 0);")
        self.nome_arquivo_edit.setObjectName("nome_arquivo_edit")
        self.horizontalLayout_3.addWidget(self.nome_arquivo_edit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.criar_texto_edit = QtWidgets.QPlainTextEdit(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.criar_texto_edit.sizePolicy().hasHeightForWidth())
        self.criar_texto_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.criar_texto_edit.setFont(font)
        self.criar_texto_edit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.criar_texto_edit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(0, 0, 0)")
        self.criar_texto_edit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.criar_texto_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.criar_texto_edit.setTabChangesFocus(False)
        self.criar_texto_edit.setUndoRedoEnabled(True)
        self.criar_texto_edit.setReadOnly(False)
        self.criar_texto_edit.setPlainText("")
        self.criar_texto_edit.setOverwriteMode(False)
        self.criar_texto_edit.setObjectName("criar_texto_edit")
        self.verticalLayout_4.addWidget(self.criar_texto_edit)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.botao_salvar = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_salvar.sizePolicy().hasHeightForWidth())
        self.botao_salvar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.botao_salvar.setFont(font)
        self.botao_salvar.setStyleSheet("QPushButton {\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(0, 0, 0)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(186, 241, 249)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(53, 218, 255);\n"
"}")
        self.botao_salvar.setObjectName("botao_salvar")
        self.horizontalLayout_2.addWidget(self.botao_salvar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.botao_escrever = QtWidgets.QPushButton(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_escrever.sizePolicy().hasHeightForWidth())
        self.botao_escrever.setSizePolicy(sizePolicy)
        self.botao_escrever.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    border-radius: 30px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(186, 241, 249)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(53, 218, 255);\n"
"}")
        self.botao_escrever.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/caderno.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_escrever.setIcon(icon1)
        self.botao_escrever.setIconSize(QtCore.QSize(40, 40))
        self.botao_escrever.setAutoExclusive(False)
        self.botao_escrever.setObjectName("botao_escrever")
        self.verticalLayout_8.addWidget(self.botao_escrever)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem7)
        self.botao_ler = QtWidgets.QPushButton(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_ler.sizePolicy().hasHeightForWidth())
        self.botao_ler.setSizePolicy(sizePolicy)
        self.botao_ler.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(0, 0, 0);\n"
"    border-radius: 30px\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(186, 241, 249)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(53, 218, 255);\n"
"}")
        self.botao_ler.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/livro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_ler.setIcon(icon2)
        self.botao_ler.setIconSize(QtCore.QSize(40, 40))
        self.botao_ler.setObjectName("botao_ler")
        self.verticalLayout_8.addWidget(self.botao_ler)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_5)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setLineWidth(1)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_10.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.page_5)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setMidLineWidth(10)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 98, 89))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setStyleSheet("border: 1px solid color rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 127);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_7.addWidget(self.plainTextEdit_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.botao_voltar.setText(_translate("Form", "Voltar"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nome Do Arquivo:</span></p></body></html>"))
        self.botao_salvar.setText(_translate("Form", "Salvar"))
        self.plainTextEdit_2.setPlainText(_translate("Form", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
