from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmAsignarRoles import Ui_FrmAsignarRoles
from datos.Dt_tbl_UserRol import Dt_tbl_UserRol
from datos.Dt_tbl_rol import Dt_tbl_rol
from datos.Dt_tbl_user import Dt_tbl_user

class CtrlFrmAsignarRoles(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmAsignarRoles()
        self.ui.setupUi(self)
        self.initControlGui()
    dtrol = Dt_tbl_rol()
    dtus = Dt_tbl_user()
    dtur = Dt_tbl_UserRol()

    def initControlGui(self):
        self.cargarCbxRol()
        self.cargarCbxUser()
        self.cargarTblUserRol()
        self.limpiarCampos()

    def limpiarCampos(self):
        self.ui.le_buscador.setText("")
        self.ui.cbx_usuario.setCurrentIndex(-1)
        self.ui.cbx_rol.setCurrentIndex(-1)

    def cargarTblUserRol(self):
        self.listUserRol = self.dtur.listUsuarioRol()
        i = len(self.listUserRol)
        self.ui.tw_registrosUsuarioRol.setRowCount(i)
        contador = 0
        for row in self.listUserRol:
            #self.ui.tw_registrosUsuarioRol.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(row._idUserRol)))
            self.ui.tw_registrosUsuarioRol.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(row._user)))
            self.ui.tw_registrosUsuarioRol.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(row._rol)))
            contador = contador + 1

    def cargarCbxRol(self):
        self.listaRol = self.dtrol.llenarCbxRol()
        for row in self.listaRol:
            self.ui.cbx_rol.addItem(row.rol, row.id_rol)

    def cargarCbxUser(self):
        self.listaUser = self.dtus.llenarCbxUser()
        for row in self.listaUser:
            self.ui.cbx_usuario.addItem(row._user, row._id_user)


