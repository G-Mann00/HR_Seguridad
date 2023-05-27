from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmRol import Ui_FrmRol
from datos.Dt_Tbl_rol import Dt_Tbl_rol

class CtrlFrmRol(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmRol()
        self.ui.setupUi(self)
        self.initControlGui()

    def initControlGui(self):
        #self.ui.btn_entrar.clicked.connect(self.validarCredenciales)
        print()
    def limpiarCampos(self):
        self.ui.le_buscador.setText("")
        self.ui.le_identificador.setText("")
        self.ui.le_nombreRol.setText("")
        self.ui.checkBox.setChecked(False)

    def cargarDatos(self):
        listRols = self.dtr.listRol()
        i = len(listRols)
        self.ui.tw_registrosRol.setRowCount(i)
        tablerow = 0
        for row in listRols:
            self.ui.tw_registroRoles.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row._id_rol)))
            self.ui.tw_registroRoles.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row._nombre))
            self.ui.tw_registroRoles.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row._descripcion))
            tablerow = tablerow + 1

    def btnAgregar(self):
        nombre = self.ui.le_nombreRol.text()
        if nombre == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return
        self.dtr.insertRol(nombre)
        self.cargarDatos()
        self.limpiarCampos()

    def btnEditar(self):
        id = self.ui.le_identificador.text()
        nombre = self.ui.le_nombreRol.text()
        if nombre == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return
        self.dtr.updateRol(id, nombre)
        self.cargarDatos()
        self.limpiarCampos()

    def btnEliminar(self):
        id = self.ui.le_identificador.text()
        self.dtr.deleteRol(id)
        self.cargarDatos()
        self.limpiarCampos()