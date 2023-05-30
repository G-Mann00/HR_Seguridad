from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmAsignarOpciones import Ui_FrmAsignarOpciones
#Datos
from datos.Dt_tbl_rol import Dt_tbl_rol
from datos.Dt_tbl_opcion import Dt_tbl_opcion
from datos.Dt_tbl_RolOpcion import Dt_tbl_RolOpcion
#Entidades
from entidades.VwRolOpcion import VwRolOpcion
#Negocios
from negocios.Ng_RolOpcion import Ng_RolOpcion


class CtrlFrmAsignarOpciones(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmAsignarOpciones()
        self.ui.setupUi(self)
        self.initControlGui()
    dtRol = Dt_tbl_rol()
    dtOpcion = Dt_tbl_opcion()
    dtRO = Dt_tbl_RolOpcion()
    ngRolOpcion = Ng_RolOpcion()
    RolOpcion = VwRolOpcion()

    def initControlGui(self):
        #Llena los comboBox y tabla
        self.cargarCbxRol()
        self.cargarCbxOpcion()
        self.cargarTblRolOpcion()
        # Llena los comboBox al hacer click en un row
        self.ui.tw_registrosRolOpcion.clicked.connect(self.filaSeleccionada)
        # CRUD
        self.ui.btn_asignar_2.clicked.connect(self.btnAsignar)
        self.ui.btn_eliminar_2.clicked.connect(self.btnEliminar)
        self.ui.btn_buscar_2.clicked.connect(self.btnBuscar)
        #Limpia todos los campos
        self.limpiarCampos()

    def limpiarCampos(self):
        self.ui.cbx_rol.setCurrentIndex(-1)
        self.ui.cbx_opcion.setCurrentIndex(-1)

    def cargarCbxRol(self):
        self.listaRol = self.dtRol.llenarCbxRol()
        self.ui.cbx_rol.addItem("")
        for row in self.listaRol:
            self.ui.cbx_rol.addItem(row.rol, row.id_rol)

    def cargarCbxOpcion(self):
        self.listaOpcion = self.dtOpcion.llenarCbxOpcion()
        self.ui.cbx_opcion.addItem("")
        for row in self.listaOpcion:
            self.ui.cbx_opcion.addItem(row.opcion, row.id_opcion)

    def cargarTblRolOpcion(self):
        self.listRolOpcion = self.dtRO.listRolOpcion()
        i = len(self.listRolOpcion)
        self.ui.tw_registrosRolOpcion.setRowCount(i)
        contador = 0
        for row in self.listRolOpcion:
            self.ui.tw_registrosRolOpcion.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(row._id_RolOpcion)))
            self.ui.tw_registrosRolOpcion.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(row._id_rol)))
            self.ui.tw_registrosRolOpcion.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(row._id_opcion)))
            self.ui.tw_registrosRolOpcion.setItem(contador, 3, QtWidgets.QTableWidgetItem(str(row._rol)))
            self.ui.tw_registrosRolOpcion.setItem(contador, 4, QtWidgets.QTableWidgetItem(str(row._opcion)))
            contador = contador + 1
        self.ui.tw_registrosRolOpcion.setColumnHidden(0, True)
        self.ui.tw_registrosRolOpcion.setColumnHidden(1, True)
        self.ui.tw_registrosRolOpcion.setColumnHidden(2, True)

    def filaSeleccionada(self):
        if len(self.ui.tw_registrosRolOpcion.selectedItems()) > 0:
            row = self.ui.tw_registrosRolOpcion.selectedItems()[0].row()
            self.ui.cbx_rol.setCurrentText(self.ui.tw_registrosRolOpcion.item(row, 3).text())
            self.ui.cbx_opcion.setCurrentText(self.ui.tw_registrosRolOpcion.item(row, 4).text())

    def btnAsignar(self):

        # Recuperando el id_rol y id_opcion
        self.RolOpcion.id_rol = self.ui.cbx_rol.currentData()
        self.RolOpcion.id_opcion = self.ui.cbx_opcion.currentData()
        self.listRolOpcion = self.dtRO.listRolOpcion()

        if self.ui.cbx_rol.currentIndex() == -1 or self.ui.cbx_opcion.currentIndex() == -1:
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        # Validando IdUnico
        for row in self.listRolOpcion:
            if str(self.RolOpcion.id_rol) == str(row.id_rol) and str(self.RolOpcion.id_opcion) == str(row.id_opcion):
                QMessageBox.warning(self, "Error", "Este rol ya tiene esta opcion")
                return

        resultado = self.ngRolOpcion.insertarRolOpcion(self.RolOpcion)
        match resultado:
            case -1:
                QMessageBox.warning(self, "Error", "No se ha podido agregar el UserRol", QMessageBox.Ok)
            case 1:
                QMessageBox.information(self, "Éxito", "Se ha agregado el UserRol correctamente", QMessageBox.Ok)
                self.limpiarCampos()
                self.cargarTblRolOpcion()
            case 2:
                QMessageBox.warning(self, "Error", "El Usuario ya tiene ese Rol", QMessageBox.Ok)

    def btnEliminar(self):

        self.listRolOpcion = self.dtRO.listRolOpcion()
        self.RolOpcion.id_rol = self.ui.cbx_rol.currentData()
        self.RolOpcion.id_opcion = self.ui.cbx_opcion.currentData()

        # Verifica que todos los datos esten ingresados
        if self.ui.cbx_rol.currentIndex() == -1 or self.ui.cbx_opcion.currentIndex() == -1:
            QMessageBox.warning(self, "Error", "Ingrese todos los datos a borrar")
            return

        # Verifica que no se borren los accessos del Administrador
        if self.RolOpcion.id_rol == 1:
            QMessageBox.warning(self, "Error", "No puedes borrar las opciones de un Administrador")
            return

        # Verifica que el rol tenga al menos accesso a una opcion
        rolContador = 0
        for row in self.listRolOpcion:
            if str(self.RolOpcion.id_rol) == str(row.id_rol):
                rolContador += 1
        if rolContador == 1:
            QMessageBox.warning(self, "Error", "Un rol debe tener por lo menos una opcion")
            return

        for row in self.listRolOpcion:
            if str(self.RolOpcion.id_rol) == str(row.id_rol) and str(self.RolOpcion.id_opcion) == str(row.id_opcion):
                self.RolOpcion.id_RolOpcion = row.id_RolOpcion
                self.RolOpcion.rol = row.rol
                self.RolOpcion.opcion = row.opcion

        alert = QMessageBox.warning(self, 'Alerta', f"¿Está seguro de eliminar {str(self.RolOpcion.opcion)} de {str(self.RolOpcion.rol)}?", QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not self.ngRolOpcion.eliminarRolOpcion(self.RolOpcion):
            QMessageBox.warning(self, "Error", "No se pudo eliminar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se eliminó el registro")
        self.cargarTblRolOpcion()
        self.limpiarCampos()

    def btnBuscar(self):
        if self.ui.le_buscador_2.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el rol")
            self.limpiarCampos()
            self.cargarTblRolOpcion()
            return

        self.RolOpcion.rol = self.ui.le_buscador_2.text()
        self.listRolOpcion = self.dtRO.listRolOpcion()

        row = 0
        for r in self.listRolOpcion:
            if str(self.RolOpcion.rol) == str(r.rol):
                self.ui.tw_registrosRolOpcion.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r._id_RolOpcion)))
                self.ui.tw_registrosRolOpcion.setItem(row, 1, QtWidgets.QTableWidgetItem(str(r._id_rol)))
                self.ui.tw_registrosRolOpcion.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r._id_opcion)))
                self.ui.tw_registrosRolOpcion.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r._rol)))
                self.ui.tw_registrosRolOpcion.setItem(row, 4, QtWidgets.QTableWidgetItem(str(r._opcion)))
                row += 1

        self.ui.tw_registrosRolOpcion.setRowCount(row)
        self.ui.tw_registrosRolOpcion.setColumnHidden(0, True)
        self.ui.tw_registrosRolOpcion.setColumnHidden(1, True)
        self.ui.tw_registrosRolOpcion.setColumnHidden(2, True)