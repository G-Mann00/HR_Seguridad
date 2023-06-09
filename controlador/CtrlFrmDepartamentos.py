from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication

from datos.Dt_Location import Dt_Location
from vistas.FrmDepartamentos import Ui_FrmDepartamentos
from datos.Dt_Departamentos import Dt_Departamentos
from entidades.Departments import Departments
from negocios.Ng_Departamento import Ng_Departamentos

class CtrlFrmDepartamentos(QtWidgets.QMainWindow):
    dDepartamento = Dt_Departamentos()
    departamento = Departments()
    dCiudad = Dt_Location()
    ngDepartamento = Ng_Departamentos()

    def __init__(self):
        self.listaRegion = []
        super().__init__()
        self.ui = Ui_FrmDepartamentos()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatosTabla()
        self.cargarDatosCombobox()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.btnAgregar)
        self.ui.tw_registroDepartamentos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_limpiar.clicked.connect(self.limpiarDatos)
        self.ui.tw_registroDepartamentos.clicked.connect(self.filaSeleccionada)
        #QApplication.instance().focusChanged.connect(self.validarIdentificador)
        self.ui.btn_editar.clicked.connect(self.btnEditar)
        self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        self.ui.le_buscador.textChanged.connect(self.refresh)
        pass

    def refresh(self):
        if self.ui.le_buscador.text() == "":
            self.cargarDatosTabla()

    def filaSeleccionada(self):
        if len(self.ui.tw_registroDepartamentos.selectedItems()) > 0:
            row = self.ui.tw_registroDepartamentos.selectedItems()[0].row()
            self.ui.le_identificador.setText(self.ui.tw_registroDepartamentos.item(row, 0).text())
            self.ui.le_nombre.setText(self.ui.tw_registroDepartamentos.item(row, 1).text())
            self.ui.cbx_localizacion.setCurrentText(self.ui.tw_registroDepartamentos.item(row, 2).text())
        self.ui.le_identificador.setEnabled(False)

    def cargarDatosCombobox(self):
        dLocalizacion = Dt_Location()
        listaDepartamentos = dLocalizacion.listarLocations()
        self.listaCiudad = self.dCiudad.listarLocations()
        self.ui.cbx_localizacion.clear()
        self.ui.cbx_localizacion.addItem("---Seleccione---")
        for r in self.listaCiudad:
            self.ui.cbx_localizacion.addItem(r.city)

    def cargarDatosTabla(self):
        dDepartamento = Dt_Departamentos()
        listaDepartamentos = dDepartamento.listarDepartamentos()
        self.ui.tw_registroDepartamentos.setRowCount(len(listaDepartamentos))

        if listaDepartamentos == None:
            alert = QMessageBox.information(self, 'Alerta', "No hay ningún departamento", QMessageBox.Ok)
            return

        self.ui.tw_registroDepartamentos.setRowCount(len(listaDepartamentos))
        self.ui.tw_registroDepartamentos.setColumnCount(3)
        self.ui.tw_registroDepartamentos.verticalHeader().setVisible(False)
        row = 0
        for d in listaDepartamentos:
            self.ui.tw_registroDepartamentos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d.id_department)))
            self.ui.tw_registroDepartamentos.setItem(row, 1, QtWidgets.QTableWidgetItem(d.department_name))
            self.ui.tw_registroDepartamentos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(d.city)))
            row += 1

    def limpiarDatos(self):
        self.ui.le_identificador.setText("")
        self.ui.le_nombre.setText("")
        self.ui.cbx_localizacion.setCurrentIndex(0)
        self.ui.le_identificador.setEnabled(True)

    def btnAgregar(self):
        if self.ui.le_nombre.text() == "" and self.ui.cbx_localizacion.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Ingrese los datos completos")
            return

        dDepartamento = Dt_Departamentos()
        d = Departments()
        d.department_id = self.ui.le_identificador.text()
        d.department_name = self.ui.le_nombre.text()
        index = self.ui.cbx_localizacion.currentIndex()
        d.city = self.listaCiudad[index - 1].city

        if not dDepartamento.insertarDepartamento(d):
            QMessageBox.warning(self, "Érror", "No se pudo agregar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se agregó el registro correctamente")
        self.limpiarDatos()
        self.cargarDatosTabla()

    def obtenerRegionId(self, nombreRegion):
        for r in self.listaRegion:
            if r.region_name == nombreRegion:
                return r.region_id
        return -1

    def btnEditar(self):
        if self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el identificador")
            return

        dDepartamento = Dt_Departamentos()
        d = Departments()
        d.department_id = self.ui.le_identificador.text()
        d.department_name = self.ui.le_nombre.text()
        index = self.ui.cbx_localizacion.currentIndex()
        d.city = self.listaCiudad[index - 1].city

        alert = QMessageBox.warning(self, 'Alerta', f"¿Está seguro de editar el departamento {d.department_name}?",
                                    QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not dDepartamento.actualizarDepartamento(d):
            QMessageBox.warning(self, "Érror", "No se pudo editar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se editó el registro correctamente")
        self.limpiarDatos()
        self.cargarDatosTabla()

    def btnEliminar(self):
        if self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el identificador")
            return

        dDepartamento = Dt_Departamentos()
        d = Departments()
        d.department_id = self.ui.le_identificador.text()
        d.department_name = self.ui.le_nombre.text()

        alert = QMessageBox.warning(self, 'Alerta', f"¿Está seguro de eliminar el departamento {d.department_name}?",
                                    QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not dDepartamento.eliminarDepartamento(d):
            QMessageBox.warning(self, "Érror", "No se pudo eliminar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se eliminó el registro correctamente")
        self.limpiarDatos()
        self.cargarDatosTabla()

    def btnBuscar(self):
        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el nombre del departamento")
            return

        self.departamento.department_name = self.ui.le_buscador.text()
        listaDepartamento = self.dDepartamento.buscarDepartamento(self.departamento)

        self.ui.tw_registroDepartamentos.setRowCount(len(listaDepartamento))
        self.ui.tw_registroDepartamentos.setColumnCount(3)
        self.ui.tw_registroDepartamentos.verticalHeader().setVisible(False)
        row = 0
        for d in listaDepartamento:
            self.ui.tw_registroDepartamentos.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d.id_department)))
            self.ui.tw_registroDepartamentos.setItem(row, 1, QtWidgets.QTableWidgetItem(d.department_name))
            self.ui.tw_registroDepartamentos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(d.city)))
            row += 1





