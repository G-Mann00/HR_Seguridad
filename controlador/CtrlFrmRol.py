from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmRol import Ui_FrmRol
from datos.Dt_tbl_rol import Dt_tbl_rol
from entidades.Tbl_rol import Tbl_rol

class CtrlFrmRol(QtWidgets.QMainWindow):
    dRol = Dt_tbl_rol()
    rol = Tbl_rol()


    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmRol()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatosTabla()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.btnAgregar)
        self.ui.tw_registroRoles.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.tw_registroRoles.clicked.connect(self.filaSeleccionada)
        self.ui.btn_editar.clicked.connect(self.btnEditar)
        self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        #self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        #self.ui.le_buscador.textChanged.connect(self.refresh)
        pass
    def limpiarCampos(self):
        self.ui.le_buscador.setText("")
        self.ui.le_identificador.setText("")
        self.ui.le_nombreRol.setText("")
        self.ui.checkBox.setChecked(False)

    def cargarDatosTabla(self):
        dRol = Dt_tbl_rol()
        listaRoles = dRol.listarRol()
        self.ui.tw_registroRoles.setRowCount(len(listaRoles))
        self.ui.tw_registroRoles.setColumnCount(2)
        row = 0
        for r in listaRoles:
            self.ui.tw_registroRoles.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.id_rol)))
            self.ui.tw_registroRoles.setItem(row, 1, QtWidgets.QTableWidgetItem(str(r.rol)))
            row += 1

    def filaSeleccionada(self):
        if len(self.ui.tw_registroRoles.selectedItems()) > 0:
            row = self.ui.tw_registroRoles.selectedItems()[0].row()
            self.ui.le_identificador.setText(self.ui.tw_registroRoles.item(row, 0).text())
            self.ui.le_nombreRol.setText(self.ui.tw_registroRoles.item(row, 1).text())
            #self.ui.checkBox.setCurrentText(self.ui.tw_registroRoles.item(row, 2).text())
        self.ui.le_identificador.setEnabled(False)

    def btnAgregar(self):
        nombre = self.ui.le_nombreRol.text()
        if nombre == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return
        self.tr.insertRol(nombre)
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