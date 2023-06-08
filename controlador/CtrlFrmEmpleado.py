import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.uic.properties import QtCore

from entidades.Employees import Employees
from datos.Dt_Employees import Dt_Employees
from negocios.Ng_Employees import Ng_Employees
from vistas.FrmEmpleado import Ui_FrmEmpleado
from datos.Dt_Jobs import Dt_Jobs
from datos.Dt_Departamentos import Dt_Departamentos


class CtrlFrmEmpleado(QtWidgets.QMainWindow):
    empleado = Employees()
    dEmpleado = Dt_Employees()
    ngEmpleado = Ng_Employees()
    dJobs = Dt_Jobs()
    dDepartamento = Dt_Departamentos()
    modoEdicion = False
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmEmpleado()
        self.ui.setupUi(self)
        self.initControlGui()
    
    
    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.BtnAgregar)
        self.ui.tw_registrosEmpleado.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_nuevo.clicked.connect(self.limpiarDatos)
        self.ui.tw_registrosEmpleado.clicked.connect(self.filaSeleccionada)
        self.ui.btn_editar.clicked.connect(self.BtnEditar)
        self.ui.btn_eliminar.clicked.connect(self.BtnEliminar)
        self.ui.btn_buscar.clicked.connect(self.BtnBuscar)
        self.ui.le_buscador.textChanged.connect(self.refresh)
        
        self.cargarDatosTabla()
        self.cargarComboBoxTrabajo()
        self.cargarComboBoxManager()
        self.cargarComboBoxDepartamento()
    
    
    def refresh(self):
        if self.ui.le_buscador.text() == "":
            self.cargarDatosTabla()
    
    def filaSeleccionada(self):
        if len(self.ui.tw_registrosEmpleado.selectedItems()) > 0:
            row = self.ui.tw_registrosEmpleado.selectedItems()[0].row()
            self.ui.le_id.setText(self.ui.tw_registrosEmpleado.item(row, 0).text())
            self.ui.le_primerNombre.setText(self.ui.tw_registrosEmpleado.item(row, 1).text())
            self.ui.le_ultimoNombre.setText(self.ui.tw_registrosEmpleado.item(row, 2).text())
            self.ui.le_correo.setText(self.ui.tw_registrosEmpleado.item(row, 3).text())
            self.ui.le_confirmarCorreo.setText(self.ui.tw_registrosEmpleado.item(row, 3).text())
            self.ui.le_telefono.setText(self.ui.tw_registrosEmpleado.item(row, 4).text())
            fecha = self.ui.tw_registrosEmpleado.item(row, 5).text()
            qfecha = QDate.fromString(fecha, "yyyy-MM-dd")
            self.ui.de_fechaContratacion.setDate(qfecha)
            self.ui.cbx_trabajo.setCurrentText(self.ui.tw_registrosEmpleado.item(row, 6).text())
            self.ui.le_salario.setText(self.ui.tw_registrosEmpleado.item(row, 7).text())
            self.ui.cbx_manager.setCurrentText(self.ui.tw_registrosEmpleado.item(row, 8).text())
            self.ui.cbx_departamento.setCurrentText(self.ui.tw_registrosEmpleado.item(row, 9).text())
        
        self.modoEdicion = True
    
    def cargarComboBoxTrabajo(self):
        self.listaTrabajo = self.dJobs.listarTrabajo()
        self.ui.cbx_trabajo.clear()
        self.ui.cbx_trabajo.addItem("---Seleccione---")
        for r in self.listaTrabajo:
            self.ui.cbx_trabajo.addItem(r.job_title, r.job_id)
    
    def cargarComboBoxManager(self):
        self.listaManagers = self.dEmpleado.listarManagers()
        self.ui.cbx_manager.clear()
        self.ui.cbx_manager.addItem("---Seleccione---")
        for r in self.listaManagers:
            nombreCompleto = f"{r.first_name} {r.last_name}"
            self.ui.cbx_manager.addItem(nombreCompleto, r.employee_id)
    
    def cargarComboBoxDepartamento(self):
        self.listaDepartamento = self.dDepartamento.listarDepartamentos()
        self.ui.cbx_departamento.clear()
        self.ui.cbx_departamento.addItem("---Seleccione---")
        for r in self.listaDepartamento:
            print(r.id_department, "Hola")
            self.ui.cbx_departamento.addItem(r.department_name, r.id_department)
    
    def cargarDatosTabla(self):
        listaEmpleados = self.dEmpleado.listarEmpleados()
        
        self.ui.tw_registrosEmpleado.setRowCount(len(listaEmpleados))
        self.ui.tw_registrosEmpleado.setColumnCount(10)
        self.ui.tw_registrosEmpleado.verticalHeader().setVisible(False)
        row = 0
        for r in listaEmpleados:
            self.ui.tw_registrosEmpleado.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.employee_id)))
            self.ui.tw_registrosEmpleado.setItem(row, 1, QtWidgets.QTableWidgetItem(r.first_name))
            self.ui.tw_registrosEmpleado.setItem(row, 2, QtWidgets.QTableWidgetItem(r.last_name))
            self.ui.tw_registrosEmpleado.setItem(row, 3, QtWidgets.QTableWidgetItem(r.email))
            self.ui.tw_registrosEmpleado.setItem(row, 4, QtWidgets.QTableWidgetItem(r.phone_number))
            self.ui.tw_registrosEmpleado.setItem(row, 5, QtWidgets.QTableWidgetItem(str(r.hire_date)))
            self.ui.tw_registrosEmpleado.setItem(row, 6, QtWidgets.QTableWidgetItem(str(r.job)))
            self.ui.tw_registrosEmpleado.setItem(row, 7, QtWidgets.QTableWidgetItem(str(r.salary)))
            self.ui.tw_registrosEmpleado.setItem(row, 8, QtWidgets.QTableWidgetItem(str(r.manager)))
            self.ui.tw_registrosEmpleado.setItem(row, 9, QtWidgets.QTableWidgetItem(str(r.department)))
            row += 1
    
    def limpiarDatos(self):
        self.ui.le_id.setText("")
        self.ui.le_primerNombre.setText("")
        self.ui.le_ultimoNombre.setText("")
        self.ui.le_correo.setText("")
        self.ui.le_confirmarCorreo.setText("")
        self.ui.le_telefono.setText("")
        self.ui.de_fechaContratacion.setDate(datetime.datetime.now())
        self.ui.cbx_trabajo.setCurrentIndex(0)
        self.ui.le_salario.setText("")
        self.ui.cbx_manager.setCurrentIndex(0)
        self.ui.cbx_departamento.setCurrentIndex(0)
        self.modoEdicion = False
    
    def BtnAgregar(self):
        
        if self.modoEdicion:
            QMessageBox.warning(self, "Error", "Te encuentras en modo edición")
            return
        
        if self.ui.le_primerNombre.text() == "" or self.ui.le_ultimoNombre.text() == "" or self.ui.le_correo.text() == "" or self.ui.le_confirmarCorreo.text() == "" or self.ui.le_telefono.text() == "" or self.ui.cbx_trabajo.currentIndex() == 0 or self.ui.le_salario.text() == "" or self.ui.cbx_departamento.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return
        
        if self.ui.le_correo.text() != self.ui.le_confirmarCorreo.text():
           QMessageBox.warning(self, "Error", "Los correos no coinciden")
           return

        if len(self.ui.le_telefono.text()) > 12:
            QMessageBox.warning(self, "Error", "El numero de telefono es muy largo (Maximo 12 caracteres)")
            return

        self.empleado.first_name = self.ui.le_primerNombre.text()
        self.empleado.last_name = self.ui.le_ultimoNombre.text()
        self.empleado.email = self.ui.le_correo.text()
        self.empleado.phone_number = self.ui.le_telefono.text()
        self.empleado.hire_date = self.ui.de_fechaContratacion.date().toString('yyyy-MM-dd')
        self.empleado.job_id = self.ui.cbx_trabajo.currentData()
        self.empleado.salary = float(self.ui.le_salario.text())
        self.empleado.manager_id = self.ui.cbx_manager.currentData()
        self.empleado.department_id = self.ui.cbx_departamento.currentData()
        
        resultado = self.ngEmpleado.insertarEmpleado(self.empleado)
        match resultado:
            case -1:
                QMessageBox.warning(self, "Error", "No se ha podido agregar al empleado", QMessageBox.Ok)
            case 1:
                QMessageBox.information(self, "Éxito", "Se ha agregado el país correctamente", QMessageBox.Ok)
                self.limpiarDatos()
                self.cargarDatosTabla()
            case 2:
                QMessageBox.warning(self, "Error", "El identificador ya existe", QMessageBox.Ok)
            case 3:
                QMessageBox.warning(self, "Error", "El correo ya existe", QMessageBox.Ok)
       
        
    def BtnEditar(self):
        
        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "No se ha seleccionado un registro")
            return
        
        if self.ui.le_primerNombre.text() == "" or self.ui.le_ultimoNombre.text() == "" or self.ui.le_correo.text() == "" or self.ui.le_confirmarCorreo.text() == "" or self.ui.le_telefono.text() == "" or self.ui.cbx_trabajo.currentIndex() == 0 or self.ui.le_salario.text() == 0 or self.ui.cbx_manager.currentIndex() == 0 or self.ui.cbx_departamento.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return
        
        if self.ui.le_correo.text() != self.ui.le_confirmarCorreo.text():
           QMessageBox.warning(self, "Error", "Los correos no coinciden")
           return

        if len(self.ui.le_telefono.text()) > 12:
            QMessageBox.warning(self, "Error", "El numero de telefono es muy largo (Maximo 12 caracteres)")
            return

        self.empleado.employee_id = self.ui.le_id.text()
        self.empleado.first_name = self.ui.le_primerNombre.text()
        self.empleado.last_name = self.ui.le_ultimoNombre.text()
        self.empleado.email = self.ui.le_correo.text()
        self.empleado.phone_number = self.ui.le_telefono.text()
        self.empleado.hire_date = self.ui.de_fechaContratacion.date().toString('yyyy-MM-dd')
        self.empleado.job_id = self.ui.cbx_trabajo.currentData()
        self.empleado.salary = float(self.ui.le_salario.text())
        self.empleado.manager_id = self.ui.cbx_manager.currentData()
        self.empleado.department_id = self.ui.cbx_departamento.currentData()
        print(self.empleado.department_id, "Soy el department id")
        
        if not self.ngEmpleado.actualizarEmpleado(self.empleado):
            QMessageBox.warning(self, "Error", "No se pudo editar al empleado")
            return

        QMessageBox.information(self, "Éxito", "Se editó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()
    
    def BtnEliminar(self):
        
        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún registro")
            return
        
        self.empleado.employee_id = self.ui.le_id.text()
        self.empleado.first_name = self.ui.le_primerNombre.text()
        self.empleado.last_name = self.ui.le_ultimoNombre.text()
        
        alert = QMessageBox.warning(self, 'Alerta', f"¿Está seguro de eliminar al empleado {self.empleado.first_name} {self.empleado.last_name}?", QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return
        
        if not self.ngEmpleado.eliminarEmpleado(self.empleado):
            QMessageBox.warning(self, "Error", "No se pudo eliminar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se eliminó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()
    
    def BtnBuscar(self):
        
        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el nombre del empleado")
            return
        
        self.empleado.first_name = self.ui.le_buscador.text()
        
        listaEmpleados = self.dEmpleado.buscarEmpleado(self.empleado)
        self.ui.tw_registrosEmpleado.setRowCount(len(listaEmpleados))
        self.ui.tw_registrosEmpleado.setColumnCount(10)
        self.ui.tw_registrosEmpleado.verticalHeader().setVisible(False)
        row = 0
        for r in listaEmpleados:
            self.ui.tw_registrosEmpleado.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.employee_id)))
            self.ui.tw_registrosEmpleado.setItem(row, 1, QtWidgets.QTableWidgetItem(r.first_name))
            self.ui.tw_registrosEmpleado.setItem(row, 2, QtWidgets.QTableWidgetItem(r.last_name))
            self.ui.tw_registrosEmpleado.setItem(row, 3, QtWidgets.QTableWidgetItem(r.email))
            self.ui.tw_registrosEmpleado.setItem(row, 4, QtWidgets.QTableWidgetItem(r.phone_number))
            self.ui.tw_registrosEmpleado.setItem(row, 5, QtWidgets.QTableWidgetItem(str(r.hire_date)))
            self.ui.tw_registrosEmpleado.setItem(row, 6, QtWidgets.QTableWidgetItem(r.job))
            self.ui.tw_registrosEmpleado.setItem(row, 7, QtWidgets.QTableWidgetItem(str(r.salary)))
            self.ui.tw_registrosEmpleado.setItem(row, 8, QtWidgets.QTableWidgetItem(r.manager))
            self.ui.tw_registrosEmpleado.setItem(row, 9, QtWidgets.QTableWidgetItem(r.department))
            row += 1
