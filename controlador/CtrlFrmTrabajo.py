from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmTrabajo import Ui_FrmTrabajo
from datos.Dt_Jobs import Dt_Jobs
from entidades.Jobs import Jobs
from negocios.Ng_Jobs import Ng_Jobs


class CtrlFrmTrabajo(QtWidgets.QMainWindow):
    dJobs = Dt_Jobs()
    nJobs = Ng_Jobs()
    job = Jobs() # nos va permitir validar si estamos en modo edición o no

    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmTrabajo()
        self.ui.setupUi(self)
        self.initControlGui()


    def initControlGui(self):
        self.cargarDatosTabla()
        self.ui.btn_agregar.clicked.connect(self.BtnAgregar)
        # self.ui.tw_registrosTrabajo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_nuevo.clicked.connect(self.limpiarDatos)
        self.ui.tw_registrosTrabajo.clicked.connect(self.filaSeleccionada)
        self.ui.btn_buscar.clicked.connect(self.buscarTrabajo)
        self.ui.btn_editar.clicked.connect(self.BtnEditar)
        self.ui.btn_eliminar.clicked.connect(self.BtnEliminar)
        pass

    def le_buscadorChanged(self):
        if self.ui.le_buscador.text() == "":
            self.cargarDatosTabla()

    def buscarTrabajo(self):
        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese un nombre de trabajo")
            return

        self.job.job_title = self.ui.le_buscador.text()
        listaTrabajo = self.dJobs.filtrarTrabajo(self.job)

        if listaTrabajo == None:
            alert = QMessageBox.information(self, 'Alerta', "No se encontró el trabajo", QMessageBox.Ok)
            return

        self.ui.tw_registrosTrabajo.setRowCount(len(listaTrabajo))
        self.ui.tw_registrosTrabajo.setColumnCount(4)
        # self.ui.tw_registrosTrabajo.verticalHeader().setVisible(False)
        row = 0
        for r in listaTrabajo:
            self.ui.tw_registrosTrabajo.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.job_id)))
            self.ui.tw_registrosTrabajo.setItem(row, 1, QtWidgets.QTableWidgetItem(r.job_title))
            self.ui.tw_registrosTrabajo.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r.min_salary)))
            self.ui.tw_registrosTrabajo.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r.max_salary)))
            row += 1


    def cargarDatosTabla(self):
        listaTrabajo = self.dJobs.listarTrabajo()

        if listaTrabajo == None:
            alert = QMessageBox.information(self, 'Alerta', "No hay ningun trabajo", QMessageBox.Ok)
            return

        self.ui.tw_registrosTrabajo.setRowCount(len(listaTrabajo))
        self.ui.tw_registrosTrabajo.setColumnCount(4)
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
        self.ui.le_nombre.setFocus()


    def filaSeleccionada(self):
        fila = self.ui.tw_registrosTrabajo.currentRow()
        self.job.job_id = self.ui.tw_registrosTrabajo.item(fila, 0).text()
        nombre = self.ui.tw_registrosTrabajo.item(fila, 1).text()
        minimo = self.ui.tw_registrosTrabajo.item(fila, 2).text()
        maximo = self.ui.tw_registrosTrabajo.item(fila, 3).text()

        self.ui.le_id.setText(self.job.job_id)
        self.ui.le_nombre.setText(nombre)
        self.ui.le_salarioMin.setText(minimo)
        self.ui.le_salarioMax.setText(maximo)
        self.ui.le_nombre.setFocus()

        #self.job.job_id = id
        self.job.job_title = nombre
        self.job.min_salary = float(minimo)
        self.job.max_salary = float(maximo)


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

        self.job.job_title = self.ui.le_nombre.text()
        self.job.min_salary = float(self.ui.le_salarioMin.text())
        self.job.max_salary = float(self.ui.le_salarioMax.text())


        resultado = self.nJobs.insertarTrabajo(self.job)

        match resultado:
            case -1:
                alert = QMessageBox.information(self, 'Alerta', "Error al insertar el trabajo", QMessageBox.Ok)

            case 1:
                QMessageBox.information(self, 'Gestion de Trabajos', "Se insertó correctamente el trabajo", QMessageBox.Ok)
                self.limpiarDatos()
                self.cargarDatosTabla()

            case 2:
                alert = QMessageBox.information(self, 'Alerta', "Ya existe el trabajo", QMessageBox.Ok)


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

        if self.ui.le_nombre.text() == self.job.job_title:
            alert = QMessageBox.information(self, 'Alerta', "El nombre de trabajo es el mismo. No se ha modificado nada", QMessageBox.Ok)
            return

        self.job.job_id = self.ui.le_id.text()
        self.job.job_title = self.ui.le_nombre.text()
        self.job.min_salary = float(self.ui.le_salarioMin.text())
        self.job.max_salary = float(self.ui.le_salarioMax.text())

        if not self.nJobs.actualizarTrabajo(self.job):
            alert = QMessageBox.information(self, 'Alerta', "Error al actualizar el trabajo", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Gestion de Trabajos', "Se actualizó correctamente el trabajo", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatosTabla()


    def BtnEliminar(self):
        if self.ui.le_id.text() == "":
            alert = QMessageBox.information(self, 'Alerta', "Debe seleccionar un trabajo", QMessageBox.Ok)
            return

        alert = QMessageBox.warning(self, "Alerta", f"¿Está seguro de eliminar el trabajo {self.ui.le_nombre.text()}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if alert == QMessageBox.No:
            return

        self.job.job_id = self.ui.le_id.text()

        if not self.dJobs.eliminarTrabajo(self.job):
            alert = QMessageBox.information(self, 'Alerta', "Error al eliminar el trabajo", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Alerta', "Se eliminó correctamente el trabajo", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatosTabla()