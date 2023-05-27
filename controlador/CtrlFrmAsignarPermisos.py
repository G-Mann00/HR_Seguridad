from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmAsignarPermisos import Ui_FrmAsignarPermisos
from datos.Dt_tbl_rol import Dt_tbl_rol


class CtrlFrmAsignarPermisos(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmAsignarPermisos()
        self.ui.setupUi(self)
        self.initControlGui()
    dtrol = Dt_tbl_rol()

    def initControlGui(self):
        self.cargarCbxRol()
        self.limpiarCampos()

    def limpiarCampos(self):
        self.ui.cbx_rol.setCurrentIndex(-1)

    def cargarCbxRol(self):
        self.listaRol = self.dtrol.llenarCbxRol()
        for row in self.listaRol:
            self.ui.cbx_rol.addItem(row.rol, row.id_rol)