from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication

from datos.Dt_Location import Dt_Location
from vistas.FrmDepartamentos import Ui_FrmDepartamentos
from datos.Dt_Departamentos import Dt_Departamentos
from datos.Dt_Region import Dt_Region
from entidades.Departments import Departments

class CtrlFrmDepartamentos(QtWidgets.QMainWindow):
    dDepartamento = Dt_Departamentos()
    departamento = Departments()
    dCiudad = Dt_Location()

    def __init__(self):
        self.listaRegion = [] #guardar la lista de regiones(incluido su id) y poder usarlo en guardar, editar.
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
        QApplication.instance().focusChanged.connect(self.validarIdentificador)
        self.ui.btn_editar.clicked.connect(self.btnEditar)
        self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        self.ui.le_buscador.textChanged.connect(self.refresh)
        pass

    def refresh(self):
        if self.ui.le_buscador.text() == "":
            self.cargarDatosTabla()

    def validarIdentificador(self,old_widget, now_widget):

        if self.ui.le_identificador is old_widget:

            if self.ui.le_identificador.text() == "":
                return

            if len(self.ui.le_identificador.text()) > 2:
                QMessageBox.warning(self, "Error", "El identificador no puede tener más de 2 caracteres")
                #self.ui.le_identificador.setFocus()
                return

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
        if self.ui.le_nombre.text() == "" or self.ui.cbx_localizacion.currentIndex() == 0 or self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return


        dDepartamento = Dt_Departamentos()
        d = Departments()
        d.department_id = self.ui.le_identificador.text()
        d.department_name = self.ui.le_nombre.text()
        index = self.ui.cbx_localizacion.currentIndex()
        d.region_id = self.listaRegion[self.ui.cbx_localizacion.currentIndex() - 1].region_id

        if dDepartamento.validarIdUnico(d):
            QMessageBox.information(self, "Érror", "Existe un registro con el mismo identificador")
            return

        if not dDepartamento.insertarDepartamento(d):
            QMessageBox.information(self, "Érror", "No se pudo guardar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se guardó el registro correctamente")
        self.limpiarDatos()
        self.cargarDatosTabla()

    def obtenerRegionId(self, nombreRegion):
        for r in self.listaRegion:
            if r.region_name == nombreRegion:
                return r.region_id
        return -1

    def btnEditar(self):
        if self.ui.le_nombre.text() == "" or self.ui.cbx_localizacion.currentIndex() == 0 or self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        dDepartamento = Dt_Departamentos()
        d = Departments()
        d.department_id = self.ui.le_identificador.text()
        d.department_name = self.ui.le_nombre.text()
        index = self.ui.cbx_localizacion.currentIndex()
        d.region_id = self.listaRegion[self.ui.cbx_localizacion.currentIndex() - 1].region_id

        if not dDepartamento.actualizarDepartamento(d):
            QMessageBox.information(self, "Érror", "No se pudo editar el registro")
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
        if self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el identificador")
            return

        dDepartamento = Dt_Departamentos()
        d = Departments()
        d.department_id = self.ui.le_identificador.text()
        d.department_name = self.ui.le_nombre.text()

        if not dDepartamento.buscarDepartamento(d):
            QMessageBox.warning(self, "Érror", "No se pudo encontrar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se encontró el registro correctamente")
        self.limpiarDatos()
        self.cargarDatosTabla()






