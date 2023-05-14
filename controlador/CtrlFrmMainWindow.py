from vistas.FrmPrincipal import Ui_FrmPrincipal
#from controlador.CtrlFrmGestionUser import CtrlFrmGestionUser
from PyQt5 import QtWidgets
from controlador.CtrlFrmAsignarPermisos import CtrlFrmAsignarPermisos
from controlador.CtrlFrmAsignarRoles import CtrlFrmAsignarRoles


class CtrlFrmMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmPrincipal()
        self.ui.setupUi(self)
        self.CtrlAP = CtrlFrmAsignarPermisos()
        self.CtrlAR = CtrlFrmAsignarRoles()
        #self.CtrlGU = CtrlFrmGestionUser()
        self.initControlGui()

    def initControlGui(self):
        self.ui.btn_asignarFuncionesRol.triggered.connect(self.openFrmAsignarPermisos)
        self.ui.btn_asignarRol.triggered.connect(self.openFrmAsignarRoles)
        #self.ui.actionGestion_de_Usuarios.triggered.connect(self.openGestionUser)

    def openFrmAsignarPermisos(self):
        self.CtrlAP.show()
        self.close()

    def openFrmAsignarRoles(self):
        self.CtrlAR.show()
        self.close()

    #def openGestionUser(self):
        #self.CtrlGU.show()
        #self.close()
