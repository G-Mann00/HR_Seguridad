from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmAsignarRoles import Ui_FrmAsignarRoles
from datos.Dt_tbl_UserRol import Dt_tbl_UserRol

class CtrlFrmAsignarRoles(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmAsignarRoles()
        self.ui.setupUi(self)
        self.initControlGui()

    def initControlGui(self):
        #self.ui.btn_entrar.clicked.connect(self.validarCredenciales)
        print()
    def limpiarCampos(self):
        self.ui.le_buscador.setText("")
        self.ui.cbx_usuario.setCurrentIndex(-1)
        self.ui.cbx_rol.setCurrentIndex(-1)

    def cargarDatos(self):
        listUserRols = self.dtu.listUserRol()
        i = len(listUserRols)
        self.ui.tw_registrosUsuarioRol.setRowCount(i)
        tablerow = 0
        for row in listUserRols:
            self.ui.tw_registrosUsuarioRol.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_user)))
            self.ui.tw_registrosUsuarioRol.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._id_rol))
            tablerow = tablerow + 1

    #def llenarComboBox(self):