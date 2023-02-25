from PyQt5 import QtWidgets, uic, QtGui, QtCore
from Notes import Ui_Form


class CriaObjetos(Ui_Form):
    def __init__(self):
        super(CriaObjetos, self).__init__()
        self.dicionario = {}

    def criar_button(self, name):
        """
        Cria um botão, No final da criação ele adiciona a self.dicionario.
        Nesse dicionário estará presente todos os botões criados por está função.
        :param name: ObjectName da nota
        :return: None
        """
        self.text_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_Button.sizePolicy().hasHeightForWidth())
        self.text_Button.setSizePolicy(sizePolicy)
        self.text_Button.setStyleSheet("QPushButton {\n"
                                       "    border: 1px solid rgb(0, 0, 0);\n"
                                       "    border-radius:  5px\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    border: 2px solid rgb(255, 255, 255)\n"
                                       "}")
        self.text_Button.setObjectName(name)
        self.verticalLayout_11.addWidget(self.text_Button)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_10.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_Button.setCheckable(True)
        self.dicionario[name] = {'botao': self.text_Button}  # O ObjectName também servirá como chave para o dicionário


app = QtWidgets.QApplication([])
file_ui = uic.loadUi('Notes.ui')

