from vistas.FrmPrincipal import Ui_FrmPrincipal
#from controlador.CtrlFrmGestionUser import CtrlFrmGestionUser
from PyQt5 import QtWidgets
#from controlador.CtrlFrmAsignarOpciones import CtrlFrmAsignarOpciones
#from controlador.CtrlFrmAsignarRoles import CtrlFrmAsignarRoles
from controlador.CtrlFrmRegion import CtrlFrmRegion
from controlador.CtrlFrmPais import CtrlFrmPais
from controlador.CtrlFrmLocation import CtrlFrmLocation
from controlador.CtrlFrmTrabajo import CtrlFrmTrabajo
from controlador.CtrlFrmDepartamentos import CtrlFrmDepartamentos
import sys


class CtrlFrmMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmPrincipal()
        self.ui.setupUi(self)
        #self.CtrlAP = CtrlFrmAsignarOpciones()
        #self.CtrlAR = CtrlFrmAsignarRoles()
        #self.CtrlGU = CtrlFrmGestionUser()
        self.CtrlReg = CtrlFrmRegion()
        #self.CtrlPais = CtrlFrmPais()
        #self.CtrlLoc = CtrlFrmLocation()
        self.CtrlJob = CtrlFrmTrabajo()
        self.CtrlDep = CtrlFrmDepartamentos()
        self.initControlGui()

    def initControlGui(self):
        self.ui.btn_asignarFuncionesRol.triggered.connect(self.openFrmAsignarPermisos)
        self.ui.btn_asignarRol.triggered.connect(self.openFrmAsignarRoles)
        #self.ui.actionGestion_de_Usuarios.triggered.connect(self.openGestionUser)
        self.ui.btn_gestionRegion.triggered.connect(self.openFrmRegion)
        self.ui.btn_gestionPais.triggered.connect(self.openFrmPais)
        self.ui.btn_gestionLocalizacion.triggered.connect(self.openFrmLocation)
        self.ui.btn_gestionTrabajos.triggered.connect(self.openFrmTrabajo)
        self.ui.btn_gestionDepartamentos.triggered.connect(self.openFrmDepartamentos)

    def openFrmLocation(self):
        self.CtrlLoc.show()

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

    def openFrmTrabajo(self):
        self.CtrlJob.show()

    def openFrmDepartamentos(self):
        self.CtrlDep.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = CtrlFrmMainWindow()
    frm.show()
    sys.exit(app.exec_())