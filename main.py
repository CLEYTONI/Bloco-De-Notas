# -*- coding: utf-8 -*-
from pyautogui import position
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QButtonGroup
from PyQt5.QtCore import pyqtSlot, QObject, pyqtSignal
import sys
import os
from criar_objetos import CriaObjetos


class Interface(QWidget, CriaObjetos):
    def __init__(self):
        super(Interface, self).__init__()
        self.setupUi(self)
        self.again = False
        self.page_edit = [False, None]  # Verifica se tá na pagina de edição de texto
        self.current_button = None
        self.total_de_notas = 0

        self.botao_escrever.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.botao_salvar.clicked.connect(self.adiciona_texto)
        self.botao_ler.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.botao_voltar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))

        self.abrir_texto()
        self.group.buttonClicked.connect(self.edita_notas)
        self.show()

    def adiciona_texto(self):
        '''
        adiciona arquivos novos.
        :return:None
        '''
        caminho = r'F:\Notes\Notas_Salvas\\'  # Caminho onde os arquivos serão adicionados
        nome_arquivo = self.nome_arquivo_edit.text()

        # Verifica se o nome do arquivo foi definido
        if nome_arquivo == '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle('Vazio')
            msg.setText('O campo "Nome do arquivo"\nnão pode fica vazio.')
            msg.exec_()
            return

        # adiciona a extensão ".txt" caso não seja informado
        nome_arquivo = f'{nome_arquivo}.txt' if not nome_arquivo[-4:] == '.txt' else nome_arquivo

        # Verifica se o arquivo informado já foi criado
        for raiz, diretorios, arquivos in os.walk(caminho):
            for arquivo in arquivos:
                if nome_arquivo == arquivo:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setWindowTitle('Existente')
                    msg.setText(f'O arquivo "{nome_arquivo[:-4]}" já existe.')
                    msg.exec_()
                    return
        # Se as exigências forem atendidas cria o arquivo
        self.total_de_notas += 1
        botao = self.criar_button('nota' + str(self.total_de_notas))
        conteudo = self.criar_texto_edit.toPlainText()
        with open(fr'{caminho}\{nome_arquivo}', 'w+') as file:
            file.write(conteudo)
            botao.setText(conteudo)
            self.dicionario['nota' + str(self.total_de_notas)] = nome_arquivo
        self.criar_texto_edit.clear()
        self.nome_arquivo_edit.clear()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Sucesso')
        msg.setText(f"""O arquivo "{nome_arquivo[:-4]}"\nfoi criado com sucesso.""")
        msg.exec_()

    def abrir_texto(self):
        """
        Vai verificar a quantidade de notas presente no caminho indicado
        e solicitar a função criar_button (Class Criar_Objetos) para criar a quantidade
        de botões necessária para cada nota.
        :return: None
        """
        # total_de_arquivos = 0
        caminho = r'F:\Notes\Notas_Salvas'  # Caminho onde as notas estão Salvas
        for raiz, diretorios, arquivos in os.walk(caminho):
            for posicao, arquivo in enumerate(arquivos):
                botao = self.criar_button('nota' + str(posicao))  # Solicita a criação de um botão (função criar_button)
                self.total_de_notas += 1
                with open(fr'{caminho}\{arquivo}', 'r') as file:  # lê o conteúdo do arquivo
                    texto = file.read()  # Guarda o conteúdo do arquivo numa variável
                    # Passa o conteúdo como texto do botão
                    botao.setText(texto)
                    self.dicionario['nota' + str(posicao)] = arquivo  # Salva o nome do arquivo
        self.again = True
        # return total_de_arquivos

    def verificar_nota(self, botao):
        print(f'O botão {botao.accessibleName()} foi clicado')

    def edita_notas(self, botao):
        self.current_button = botao
        self.stackedWidget.setCurrentWidget(self.page_3)
        self.plainTextEdit_2.setPlainText(botao.text())
        self.page_edit[0] = True
        self.page_edit[1] = self.dicionario[botao.accessibleName()]

    def mousePressEvent(self, x):
        if self.page_edit[0]:
            conteudo = self.plainTextEdit_2.toPlainText()
            with open(fr'F:\Notes\Notas_Salvas\{self.page_edit[1]}', 'w') as file:
                file.write(conteudo)
            self.stackedWidget.setCurrentWidget(self.page_5)
            self.current_button.setText(conteudo)
            self.plainTextEdit_2.clear()
            self.page_edit[0] = False
            self.page_edit[1] = None

        else:
            y, z = position()
            print(y, z)


if __name__ == '__main__':
    execute = QApplication(sys.argv)
    projeto = Interface()
    execute.exec_()
