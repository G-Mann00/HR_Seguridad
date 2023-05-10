from vistas.FrmPrincipal import Ui_FrmPrincipal
#from controlador.CtrlFrmGestionUser import CtrlFrmGestionUser
from PyQt5 import QtWidgets


class CtrlFrmMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmPrincipal()
        self.ui.setupUi(self)
        #self.CtrlGU = CtrlFrmGestionUser()
        self.initControlGui()

    def initControlGui(self):
        print()
        #self.ui.actionGestion_de_Usuarios.triggered.connect(self.openGestionUser)

    #def openGestionUser(self):
        #self.CtrlGU.show()
        #self.close()
