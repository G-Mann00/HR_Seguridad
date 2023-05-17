from vistas.FrmPrincipal import Ui_FrmPrincipal
#from controlador.CtrlFrmGestionUser import CtrlFrmGestionUser
from PyQt5 import QtWidgets
from controlador.CtrlFrmAsignarPermisos import CtrlFrmAsignarPermisos
from controlador.CtrlFrmAsignarRoles import CtrlFrmAsignarRoles
from controlador.CtrlFrmRegion import CtrlFrmRegion
from controlador.CtrlFrmPais import CtrlFrmPais
import sys


class CtrlFrmMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmPrincipal()
        self.ui.setupUi(self)
        self.CtrlAP = CtrlFrmAsignarPermisos()
        self.CtrlAR = CtrlFrmAsignarRoles()
        #self.CtrlGU = CtrlFrmGestionUser()
        self.CtrlReg = CtrlFrmRegion()
        self.CtrlPais = CtrlFrmPais()
        self.initControlGui()

    def initControlGui(self):
        self.ui.btn_asignarFuncionesRol.triggered.connect(self.openFrmAsignarPermisos)
        self.ui.btn_asignarRol.triggered.connect(self.openFrmAsignarRoles)
        #self.ui.actionGestion_de_Usuarios.triggered.connect(self.openGestionUser)
        self.ui.btn_gestionRegion.triggered.connect(self.openFrmRegion)
        self.ui.btn_gestionPais.triggered.connect(self.openFrmPais)


    def openFrmAsignarPermisos(self):
        self.CtrlAP.show()
        self.close()

    def openFrmAsignarRoles(self):
        self.CtrlAR.show()
        self.close()

    #def openGestionUser(self):
        #self.CtrlGU.show()
        #self.close()

    def openFrmRegion(self):
        self.CtrlReg.show()
        #self.close()

    def openFrmPais(self):
        self.CtrlPais.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = CtrlFrmMainWindow()
    frm.show()
    sys.exit(app.exec_())