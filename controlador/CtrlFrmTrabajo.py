from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmTrabajo import Ui_FrmTrabajo
from datos.Dt_Jobs import Dt_Jobs
from entidades.Jobs import Jobs
from negocios.Ng_Jobs import Ng_Jobs


class CtrlFrmTrabajo(QtWidgets.QMainWindow):
    dJobs = Dt_Jobs()
    nJobs = Ng_Jobs()
    job = Jobs()  # nos va permitir validar si estamos en modo edición o no
    modoEdicion = False

    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmTrabajo()
        self.ui.setupUi(self)
        self.initControlGui()

    def initControlGui(self):
        self.cargarDatosTabla()
        self.ui.btn_agregar.clicked.connect(self.BtnAgregar)
        self.ui.tw_registrosTrabajo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_nuevo.clicked.connect(self.limpiarDatos)
        self.ui.tw_registrosTrabajo.clicked.connect(self.filaSeleccionada)
        self.ui.btn_buscar.clicked.connect(self.buscarTrabajo)
        self.ui.btn_editar.clicked.connect(self.BtnEditar)
        self.ui.btn_eliminar.clicked.connect(self.BtnEliminar)
        self.ui.le_buscador.textChanged.connect(self.refresh)
        pass

    def refresh(self):
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
        self.ui.tw_registrosTrabajo.verticalHeader().setVisible(False)
        row = 0
        for r in listaTrabajo:
            self.ui.tw_registrosTrabajo.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.job_id)))
            self.ui.tw_registrosTrabajo.setItem(row, 1, QtWidgets.QTableWidgetItem(r.job_title))
            self.ui.tw_registrosTrabajo.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r.min_salary)))
            self.ui.tw_registrosTrabajo.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r.max_salary)))
            row += 1

    def cargarDatosTabla(self):
        listaTrabajo = self.dJobs.listarTrabajo()

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
        self.ui.le_nombre.setFocus()
        self.modoEdicion = False

    def filaSeleccionada(self):
        if len(self.ui.tw_registrosTrabajo.selectedItems()) > 0:
            row = self.ui.tw_registrosTrabajo.selectedItems()[0].row()
            self.ui.le_id.setText(self.ui.tw_registrosTrabajo.item(row, 0).text())
            self.ui.le_nombre.setText(self.ui.tw_registrosTrabajo.item(row, 1).text())
            self.ui.le_salarioMin.setText(self.ui.tw_registrosTrabajo.item(row, 2).text())
            self.ui.le_salarioMax.setText(self.ui.tw_registrosTrabajo.item(row, 3).text())

        self.modoEdicion = True

    def BtnAgregar(self):

        if self.modoEdicion:
            QMessageBox.warning(self, "Error", "Te encuentras en modo edición")
            return

        if self.ui.le_nombre.text() == "" or self.ui.le_salarioMin.text() == "" or self.ui.le_salarioMax.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        self.job.job_title = self.ui.le_nombre.text()
        self.job.min_salary = float(self.ui.le_salarioMin.text())
        self.job.max_salary = float(self.ui.le_salarioMax.text())

        if self.job.max_salary < self.job.min_salary:
            QMessageBox.warning(self, "Error", "Ingrese correctamente los salarios")
            return

        resultado = self.nJobs.insertarTrabajo(self.job)
        match resultado:
            case -1:
                alert = QMessageBox.information(self, 'Alerta', "Error al insertar el trabajo", QMessageBox.Ok)

            case 1:
                QMessageBox.information(self, 'Gestion de Trabajos', "Se insertó correctamente el trabajo",
                                        QMessageBox.Ok)
                self.limpiarDatos()
                self.cargarDatosTabla()

            case 2:
                alert = QMessageBox.information(self, 'Alerta', "Ya existe el trabajo", QMessageBox.Ok)

    def BtnEditar(self):

        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "No se ha seleccionado un registro")
            return

        if self.ui.le_nombre.text() == "" or self.ui.le_salarioMin.text() == "" or self.ui.le_salarioMax.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        self.job.job_id = self.ui.le_id.text()
        self.job.job_title = self.ui.le_nombre.text()
        self.job.min_salary = float(self.ui.le_salarioMin.text())
        self.job.max_salary = float(self.ui.le_salarioMax.text())

        if self.job.max_salary < self.job.min_salary:
            QMessageBox.warning(self, "Error", "Ingrese correctamente los salarios")
            return

        if not self.nJobs.actualizarTrabajo(self.job):
            alert = QMessageBox.information(self, 'Alerta', "Error al actualizar el trabajo", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Gestion de Trabajos', "Se actualizó correctamente el trabajo", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatosTabla()

    def BtnEliminar(self):

        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún registro")
            return

        self.job.job_id = self.ui.le_id.text()
        self.job.job_title = self.ui.le_nombre.text()

        alert = QMessageBox.warning(self, "Alerta", f"¿Está seguro de eliminar el trabajo {self.job.job_title}?",
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not self.dJobs.eliminarTrabajo(self.job):
            alert = QMessageBox.information(self, 'Alerta', "Error al eliminar el trabajo", QMessageBox.Ok)
            return

        QMessageBox.information(self, 'Alerta', "Se eliminó correctamente el trabajo", QMessageBox.Ok)
        self.limpiarDatos()
        self.cargarDatosTabla()
