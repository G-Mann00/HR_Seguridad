from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmRol import Ui_FrmRol
from datos.Dt_tbl_rol import Dt_tbl_rol
from entidades.Tbl_rol import Tbl_rol
from negocios.Ng_Rol import Ng_Rol

class CtrlFrmRol(QtWidgets.QMainWindow):
    dRol = Dt_tbl_rol()
    rol = Tbl_rol()
    ngRol = Ng_Rol()

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
        self.ui.btn_buscar.clicked.connect(self.btnBuscar)
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
        if self.ui.le_nombreRol.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese los datos completos")
            return

        dRol = Dt_tbl_rol()
        r = Tbl_rol()
        r.rol = self.ui.le_nombreRol.text()
        r.estado = self.ui.checkBox.isChecked()

        if not dRol.agregarRol(r):
            QMessageBox.warning(self, "Érror", "No se pudo agregar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se agregó el registro correctamente")
        self.limpiarCampos()
        self.cargarDatosTabla()

    def btnEditar(self):
        if self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el identificador")
            return

        dRol = Dt_tbl_rol()
        r = Tbl_rol()
        r.id_rol = self.ui.le_identificador.text()
        r.rol = self.ui.le_nombreRol.text()
        r.estado = self.ui.checkBox.isChecked()

        alert = QMessageBox.warning(self, 'Alerta', f"¿Está seguro de editar el departamento {r.rol}?",
                                    QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not dRol.editarRol(r):
            QMessageBox.warning(self, "Érror", "No se pudo editar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se editó el registro correctamente")
        self.limpiarCampos()
        self.cargarDatosTabla()


    def btnEliminar(self):
        if self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el identificador")
            return

        dRol= Dt_tbl_rol()
        r = Tbl_rol()
        r.id_rol = self.ui.le_identificador.text()
        r.rol = self.ui.le_nombreRol.text()

        alert = QMessageBox.warning(self, 'Alerta', f"¿Está seguro de eliminar el departamento {r.rol}?",
                                    QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not dRol.eliminarRol(r):
            QMessageBox.warning(self, "Érror", "No se pudo eliminar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se eliminó el registro correctamente")
        self.limpiarCampos()
        self.cargarDatosTabla()

    def btnBuscar(self):
        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el nombre del rol")
            return

        self.rol.rol = self.ui.le_buscador.text()
        listaRoles = self.dRol.buscarRol(self.rol)

        self.ui.tw_registroRoles.setRowCount(len(listaRoles))
        self.ui.tw_registroRoles.setColumnCount(2)
        #self.ui.tw_registroRoles.verticalHeader().setVisible(False)
        row = 0
        for d in listaRoles:
            self.ui.tw_registroRoles.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d.id_rol)))
            self.ui.tw_registroRoles.setItem(row, 1, QtWidgets.QTableWidgetItem(d.rol))

            row += 1

    def validarVacios(self):
        if self.ui.le_nombreRol.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return False
        return True
