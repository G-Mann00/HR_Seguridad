from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmTrabajo import Ui_FrmTrabajo
from datos.Dt_Jobs import Dt_Jobs
from entidades.Jobs import Jobs


class CtrlFrmTrabajo(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmTrabajo()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatosTabla()


    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.BtnAgregar)
        self.ui.tw_registrosTrabajo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_nuevo.clicked.connect(self.limpiarDatos)
        self.ui.tw_registrosTrabajo.clicked.connect(self.filaSeleccionada)
        self.ui.btn_buscar.clicked.connect(self.buscarTrabajo)
        self.ui.btn_editar.clicked.connect(self.BtnEditar)
        self.ui.btn_eliminar.clicked.connect(self.BtnEliminar)
        pass


    def buscarTrabajo(self):
        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese un nombre de trabajo")
            return

        dTrabajo = Dt_Jobs()
        j = Jobs()
        j.job_title = self.ui.le_buscador.text()
        listaTrabajo = dTrabajo.buscar(j)
        if listaTrabajo == None:
            alert = QMessageBox.information(self, 'Alerta', "No se encontró el trabajo", QMessageBox.Ok)
            return

        self.ui.tw_registrosTrabajo.setRowCount(len(listaTrabajo))
        self.ui.tw_registrosTrabajo.setColumnCount(4)
        self.ui.tw_registrosTrabajo.verticalHeader().setVisible(False)
        row = 0
        for r in listaTrabajo:
            self.ui.tw_registrosTrabajo.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.job_id)))
            self.ui.tw_registrosTrabajo.setItem(row, 1, QtWidgets.QTableWidgetItem(r.job_title))
            self.ui.tw_registrosTrabajo.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r.min_salary)))
            self.ui.tw_registrosTrabajo.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r.max_salary)))
            row += 1


    def cargarDatosTabla(self):
        dTrabajo = Dt_Jobs()
        listaTrabajo = dTrabajo.listarTrabajo()
        if listaTrabajo == None:
            alert = QMessageBox.information(self, 'Alerta', "No hay ningun trabajo", QMessageBox.Ok)
            return

        self.ui.tw_registrosTrabajo.setRowCount(len(listaTrabajo))
        self.ui.tw_registrosTrabajo.setColumnCount(4)
        self.ui.tw_registrosTrabajo.verticalHeader().setVisible(False)
        row = 0
        for r in listaTrabajo:
            self.ui.tw_registrosTrabajo.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.job_id)))
            self.ui.tw_registrosTrabajo.setItem(row, 1, QtWidgets.QTableWidgetItem(r.job_title))
            self.ui.tw_registrosTrabajo.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r.min_salary)))
            self.ui.tw_registrosTrabajo.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r.max_salary)))
            row += 1


    def limpiarDatos(self):
        self.ui.le_id.setText("")
        self.ui.le_nombre.setText("")
        self.ui.le_salarioMin.setText("")
        self.ui.le_salarioMax.setText("")


    def filaSeleccionada(self):
        fila = self.ui.tw_registrosTrabajo.currentRow()
        id = self.ui.tw_registrosTrabajo.item(fila, 0).text()
        nombre = self.ui.tw_registrosTrabajo.item(fila, 1).text()
        minimo = self.ui.tw_registrosTrabajo.item(fila, 2).text()
        maximo = self.ui.tw_registrosTrabajo.item(fila, 3).text()

        self.ui.le_id.setText(id)
        self.ui.le_nombre.setText(nombre)
        self.ui.le_salarioMin.setText(minimo)
        self.ui.le_salarioMax.setText(maximo)
        self.ui.le_nombre.setFocus()


    def BtnAgregar(self):

        if self.ui.le_id.text() != "":
            alert = QMessageBox.information(self, 'Alerta', "Se encuentra en modo edicion", QMessageBox.Ok)
            return

        if self.ui.le_nombre.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe insertar un nombre", QMessageBox.Ok)
            return

        if self.ui.le_salarioMin.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe insertar un salario minimo", QMessageBox.Ok)
            return

        if self.ui.le_salarioMax.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe insertar un salario maximo", QMessageBox.Ok)
            return

        dTrabajo = Dt_Jobs()
        j = Jobs()
        j.job_title = self.ui.le_nombre.text()
        j.min_salary = float(self.ui.le_salarioMin.text())
        j.max_salary = float(self.ui.le_salarioMax.text())

        if not dTrabajo.insertarTrabajo(j):
            alert = QMessageBox.information(self, 'Alerta', "Error al insertar el trabajo", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Alerta', "Se insertó correctamente el trabajo", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatosTabla()


    def BtnEditar(self):
        if self.ui.le_id.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe seleccionar un trabajo", QMessageBox.Ok)
            return

        if self.ui.le_nombre.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe insertar un nombre", QMessageBox.Ok)
            return

        if self.ui.le_salarioMin.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe insertar un salario minimo", QMessageBox.Ok)
            return

        if self.ui.le_salarioMax.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe insertar un salario maximo", QMessageBox.Ok)
            return

        dTrabajo = Dt_Jobs()
        j = Jobs()
        j.job_id = self.ui.le_id.text()
        j.job_title = self.ui.le_nombre.text()
        j.min_salary = float(self.ui.le_salarioMin.text())
        j.max_salary = float(self.ui.le_salarioMax.text())

        if not dTrabajo.actualizarTrabajo(j):
            alert = QMessageBox.information(self, 'Alerta', "Error al insertar el trabajo", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Alerta', "Se actualizo correctamente el trabajo", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatosTabla()


    def BtnEliminar(self):
        if self.ui.le_id.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe seleccionar un trabajo", QMessageBox.Ok)
            return

        alert = QMessageBox.warning(self, "Alerta", f"¿Está seguro de eliminar el trabajo {self.ui.le_nombre.text()}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if alert == QMessageBox.No:
            return

        dTrabajo = Dt_Jobs()
        j = Jobs()
        j.job_id = self.ui.le_id.text()

        if not dTrabajo.eliminarTrabajo(j):
            alert = QMessageBox.information(self, 'Alerta', "Error al eliminar el trabajo", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Alerta', "Se elimino correctamente el trabajo", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatosTabla()
