from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from vistas.FrmDependiente import Ui_FrmDependiente
from entidades.Dependents import Dependents
from datos.Dt_Dependents import Dt_Dependents
from negocios.Ng_Dependents import Ng_Dependent
from datos.Dt_Employees import Dt_Employees


class CtrlFrmDependiente(QtWidgets.QMainWindow):
    d = Dependents()
    dDependent = Dt_Dependents()
    ngDependent = Ng_Dependent()
    dEmpleado = Dt_Employees()
    modoEdicion = False

    def __init__(self):
        self.listaDependiente = []
        super().__init__()
        self.ui = Ui_FrmDependiente()
        self.ui.setupUi(self)
        self.initControlGui()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.BtnAgregar)
        self.ui.tw_registrosDependiente.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_nuevo.clicked.connect(self.limpiarDatos)
        self.ui.tw_registrosDependiente.clicked.connect(self.filaSeleccionada)
        self.ui.btn_editar.clicked.connect(self.BtnEditar)
        self.ui.btn_eliminar.clicked.connect(self.BtnEliminar)
        self.ui.btn_buscar.clicked.connect(self.BtnBuscar)
        self.ui.le_buscador.textChanged.connect(self.refresh)

        self.cargarDatosTabla()
        self.cargarComboBoxEmpleado()

    def refresh(self):
        if self.ui.le_buscador.text() == "":
            self.cargarDatosTabla()

    def filaSeleccionada(self):
        if len(self.ui.tw_registrosDependiente.selectedItems()) > 0:
            row = self.ui.tw_registrosDependiente.selectedItems()[0].row()
            self.ui.le_id.setText(self.ui.tw_registrosDependiente.item(row, 0).text())
            self.ui.le_primerNombre.setText(self.ui.tw_registrosDependiente.item(row, 1).text())
            self.ui.le_ultimoNombre.setText(self.ui.tw_registrosDependiente.item(row, 2).text())
            self.ui.le_relacion.setText(self.ui.tw_registrosDependiente.item(row, 3).text())
            self.ui.cbx_empleado.setCurrentText(self.ui.tw_registrosDependiente.item(row, 4).text())
        self.modoEdicion = True

    def cargarComboBoxEmpleado(self):
        self.listaEmpleados = self.dEmpleado.listarEmpleados()
        self.ui.cbx_empleado.clear()
        self.ui.cbx_empleado.addItem("---Seleccione---")
        for r in self.listaEmpleados:
            nombreCompleto = f"{r.first_name} {r.last_name}"
            self.ui.cbx_empleado.addItem(nombreCompleto, r.employee_id)

    def cargarDatosTabla(self):
        listaDependientes = self.dDependent.listarDependientes()
        self.ui.tw_registrosDependiente.setRowCount(len(listaDependientes))
        self.ui.tw_registrosDependiente.setColumnCount(5)
        self.ui.tw_registrosDependiente.verticalHeader().setVisible(False)
        row = 0

        for r in listaDependientes:
            self.ui.tw_registrosDependiente.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.dependent_id)))
            self.ui.tw_registrosDependiente.setItem(row, 1, QtWidgets.QTableWidgetItem(r.first_name))
            self.ui.tw_registrosDependiente.setItem(row, 2, QtWidgets.QTableWidgetItem(r.last_name))
            self.ui.tw_registrosDependiente.setItem(row, 3, QtWidgets.QTableWidgetItem(r.relationship))
            self.ui.tw_registrosDependiente.setItem(row, 4, QtWidgets.QTableWidgetItem(r.employee_name))
            row += 1

    def limpiarDatos(self):
        self.ui.le_id.setText("")
        self.ui.le_primerNombre.setText("")
        self.ui.le_ultimoNombre.setText("")
        self.ui.le_relacion.setText("")
        self.ui.cbx_empleado.setCurrentText("")
        self.modoEdicion = False

    def BtnAgregar(self):

        if self.modoEdicion:
            QMessageBox.warning(self, "Error", "Te encuentras en modo edición")
            return

        if self.ui.le_primerNombre.text() == "" or self.ui.le_ultimoNombre.text() == "" or self.ui.le_relacion.text() == "" or self.ui.cbx_empleado.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        self.d.first_name = self.ui.le_primerNombre.text()
        self.d.last_name = self.ui.le_ultimoNombre.text()
        self.d.relationship = self.ui.le_relacion.text()
        self.d.employee_id = self.ui.cbx_empleado.currentData()

        resultado = self.ngDependent.insertarDependiente(self.d)
        match resultado:
            case -1:
                QMessageBox.warning(self, "Error", "No se ha podido agregar al dependiente", QMessageBox.Ok)
            case 1:
                QMessageBox.information(self, "Éxito", "Se ha agregado al dependiente correctamente", QMessageBox.Ok)
                self.limpiarDatos()
                self.cargarDatosTabla()
            case 2:
                QMessageBox.warning(self, "Error", "El identificador ya existe", QMessageBox.Ok)

    def BtnEditar(self):

        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "Te encuentras en modo edición")
            return

        if self.ui.le_primerNombre.text() == "" or self.ui.le_ultimoNombre.text() == "" or self.ui.le_relacion.text() == "" or self.ui.cbx_empleado.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        self.d.dependent_id = self.ui.le_id.text()
        self.d.first_name = self.ui.le_primerNombre.text()
        self.d.last_name = self.ui.le_ultimoNombre.text()
        self.d.relationship = self.ui.le_relacion.text()
        self.d.employee_id = self.ui.cbx_empleado.currentData()

        if not self.ngDependent.actualizarDependiente(self.d):
            QMessageBox.warning(self, "Error", "No se pudo editar el registro")
            return

        QMessageBox.information(self, "Éxito", "Se editó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()

    def BtnEliminar(self):

        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún registro")
            return

        self.d.dependent_id = self.ui.le_id.text()
        self.d.first_name = self.ui.le_primerNombre.text()
        self.d.last_name = self.ui.le_ultimoNombre.text()

        alert = QMessageBox.warning(self, 'Alerta',
                                    f"¿Está seguro de eliminar el dependiente {self.d.first_name} {self.d.last_name}?",
                                    QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not self.ngDependent.eliminarDependiente(self.d):
            QMessageBox.warning(self, "Error", "No se pudo eliminar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se eliminó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()

    def BtnBuscar(self):
        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el nombre del país")
            return

        self.d.first_name = self.ui.le_buscador.text()
        listaDependientes = self.dDependent.buscarDependiente(self.d)

        self.ui.tw_registrosDependiente.setRowCount(len(listaDependientes))
        self.ui.tw_registrosDependiente.setColumnCount(5)
        self.ui.tw_registrosDependiente.verticalHeader().setVisible(False)
        row = 0

        for r in listaDependientes:
            self.ui.tw_registrosDependiente.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.dependent_id)))
            self.ui.tw_registrosDependiente.setItem(row, 1, QtWidgets.QTableWidgetItem(r.first_name))
            self.ui.tw_registrosDependiente.setItem(row, 2, QtWidgets.QTableWidgetItem(r.last_name))
            self.ui.tw_registrosDependiente.setItem(row, 3, QtWidgets.QTableWidgetItem(r.relationship))
            self.ui.tw_registrosDependiente.setItem(row, 4, QtWidgets.QTableWidgetItem(r.employee_name))
            row += 1

