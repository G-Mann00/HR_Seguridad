from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmAsignarPermisos import Ui_FrmAsignarPermisos


class CtrlFrmAsignarPermisos(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmAsignarPermisos()
        self.ui.setupUi(self)
        self.initControlGui()

    def initControlGui(self):
        #self.ui.btn_entrar.clicked.connect(self.validarCredenciales)
        print()
