from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmRegion import Ui_FrmRegion
from datos.Dt_Region import Dt_Region
from entidades.Region import Region


class CtrlFrmRegion(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmRegion()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatos()


    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.btnAgregar)
        self.ui.tw_registroRegion.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_limpiar.clicked.connect(self.limpiarDatos)
        self.ui.tw_registroRegion.clicked.connect(self.filaSeleccionada)
        self.ui.btn_buscar.clicked.connect(self.buscarRegion)
        self.ui.btn_editar.clicked.connect(self.btnEditar)
        self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        pass

    def buscarRegion(self):
        if self.ui.le_buscar.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese un nombre de región")
            return

        dRegion = Dt_Region()
        r = Region()
        r.region_name = self.ui.le_buscar.text()
        listaRegion = dRegion.buscar(r)
        if listaRegion == None:
            alert = QMessageBox.information(self, 'Alerta', "No se encontró la región", QMessageBox.Ok)
            return

        self.ui.tw_registroRegion.setRowCount(len(listaRegion))
        self.ui.tw_registroRegion.setColumnCount(2)
        self.ui.tw_registroRegion.verticalHeader().setVisible(False)
        row = 0
        for r in listaRegion:
            self.ui.tw_registroRegion.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.region_id)))
            self.ui.tw_registroRegion.setItem(row, 1, QtWidgets.QTableWidgetItem(r.region_name))
            row += 1


    def cargarDatos(self):
        dRegion = Dt_Region()
        listaRegion = dRegion.listarRegion()
        if listaRegion == None:
            alert = QMessageBox.information(self, 'Alerta', "No hay ninguna región", QMessageBox.Ok)
            return

        self.ui.tw_registroRegion.setRowCount(len(listaRegion))
        self.ui.tw_registroRegion.setColumnCount(2)
        self.ui.tw_registroRegion.verticalHeader().setVisible(False)
        row = 0
        for r in listaRegion:
            self.ui.tw_registroRegion.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.region_id)))
            self.ui.tw_registroRegion.setItem(row, 1, QtWidgets.QTableWidgetItem(r.region_name))
            row += 1

    def limpiarDatos(self):
        self.ui.le_identificador.setText("")
        self.ui.le_nombre.setText("")
        self.ui.le_nombre.setFocus()

    def filaSeleccionada(self):
        fila = self.ui.tw_registroRegion.currentRow()
        id = self.ui.tw_registroRegion.item(fila, 0).text()
        nombre = self.ui.tw_registroRegion.item(fila, 1).text()
        self.ui.le_identificador.setText(id)
        self.ui.le_nombre.setText(nombre)
        self.ui.le_nombre.setFocus()


    def btnAgregar(self):
        if self.ui.le_identificador.text() != "":
            alert = QMessageBox.information(self, 'Alerta', "Se encuentra en modo edicion", QMessageBox.Ok)
            return

        if self.ui.le_nombre.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe ingresar un nombre", QMessageBox.Ok)
            return

        dRegion = Dt_Region()
        r = Region()
        r.region_name = self.ui.le_nombre.text()

        if not dRegion.insertarRegion(r):
            alert = QMessageBox.information(self, 'Alerta', "Error al insertar la región", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Alerta', "Se insertó correctamente la región", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatos()

    def btnEditar(self):
        if self.ui.le_identificador.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe seleccionar una región", QMessageBox.Ok)
            return

        if self.ui.le_nombre.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe ingresar un nombre", QMessageBox.Ok)
            return

        dRegion = Dt_Region()
        r = Region()
        r.region_id = self.ui.le_identificador.text()
        r.region_name = self.ui.le_nombre.text()

        if not dRegion.actualizarRegion(r):
            alert = QMessageBox.information(self, 'Alerta', "Error al actualizar la región", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Alerta', "Se actualizó correctamente la región", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatos()

    def btnEliminar(self):
        if self.ui.le_identificador.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe seleccionar una región", QMessageBox.Ok)
            return

        alert = QMessageBox.warning(self, "Alerta", f"¿Está seguro de eliminar la región {self.ui.le_nombre.text()}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if alert == QMessageBox.No:
            return

        dRegion = Dt_Region()
        r = Region()
        r.region_id = self.ui.le_identificador.text()

        if not dRegion.eliminarRegion(r):
            alert = QMessageBox.information(self, 'Alerta', "Error al eliminar la región", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Alerta', "Se eliminó correctamente la región", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatos()






