from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmLogin import Ui_FrmLogin
from controlador.CtrlFrmMainWindow import CtrlFrmMainWindow


class CtrlFrmLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmLogin()
        self.ui.setupUi(self)
        self.CtrlMW = CtrlFrmMainWindow()
        self.initControlGui()

    def initControlGui(self):
        self.ui.btn_entrar.clicked.connect(self.validarCredenciales)
        #self.ui.btnEntrar.clicked.connect(lambda: self.validarCredenciales())

    def validarCredenciales(self):
        user = self.ui.le_usuario.text()
        pwd = self.ui.le_contrasena.text()

        if user == "root" and pwd == "123":
            self.openMainWindow()
        else:
            alert = QMessageBox.information(self, 'Alerta', "Usuario y/o clave incorrectos", QMessageBox.Ok)

    def openMainWindow(self):
        self.CtrlMW.show()
        self.close()
