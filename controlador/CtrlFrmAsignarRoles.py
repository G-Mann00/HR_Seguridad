from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.FrmAsignarRoles import Ui_FrmAsignarRoles
from datos.Dt_tbl_UserRol import Dt_tbl_UserRol
from datos.Dt_tbl_rol import Dt_tbl_rol
from datos.Dt_tbl_user import Dt_tbl_user
from negocios.Ng_UserRol import Ng_UserRol
from entidades.VwUserRol import VwUserRol

class CtrlFrmAsignarRoles(QtWidgets.QMainWindow):
    dtrol = Dt_tbl_rol()
    dtus = Dt_tbl_user()
    dtur = Dt_tbl_UserRol()
    ngUserRol = Ng_UserRol()
    UserRol = VwUserRol()

    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmAsignarRoles()
        self.ui.setupUi(self)
        self.initControlGui()

    def initControlGui(self):
        # Llena los comboBox y Tabla
        self.cargarCbxRol()
        self.cargarCbxUser()
        self.cargarTblUserRol()
        self.ui.tw_registrosUsuarioRol.clicked.connect(self.filaSeleccionada)
        #CRUD
        self.ui.btn_actualizar.clicked.connect(self.btnActualizar)
        self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        # Limpia todos los campos
        self.limpiarCampos()

    def limpiarCampos(self):
        self.ui.le_buscador.setText("")
        self.ui.cbx_usuario.setCurrentIndex(-1)
        self.ui.cbx_rol.setCurrentIndex(-1)

    def cargarTblUserRol(self):
        self.listUserRol = self.dtur.listUsuarioRol()
        i = len(self.listUserRol)
        self.ui.tw_registrosUsuarioRol.setRowCount(i)
        contador = 0
        for row in self.listUserRol:
            self.ui.tw_registrosUsuarioRol.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(row._idUserRol)))
            self.ui.tw_registrosUsuarioRol.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(row._id_user)))
            self.ui.tw_registrosUsuarioRol.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(row._id_rol)))
            self.ui.tw_registrosUsuarioRol.setItem(contador, 3, QtWidgets.QTableWidgetItem(str(row._user)))
            self.ui.tw_registrosUsuarioRol.setItem(contador, 4, QtWidgets.QTableWidgetItem(str(row._rol)))
            contador = contador + 1
        # Esconde las columnas que no necesito mostrar
        self.ui.tw_registrosUsuarioRol.setColumnHidden(0, True)
        self.ui.tw_registrosUsuarioRol.setColumnHidden(1, True)
        self.ui.tw_registrosUsuarioRol.setColumnHidden(2, True)

    def cargarCbxRol(self):
        self.listaRol = self.dtrol.llenarCbxRol()
        self.ui.cbx_rol.addItem("")
        for row in self.listaRol:
            self.ui.cbx_rol.addItem(row.rol, row.id_rol)

    def cargarCbxUser(self):
        self.listaUser = self.dtus.llenarCbxUser()
        self.ui.cbx_usuario.addItem("")
        for row in self.listaUser:
            self.ui.cbx_usuario.addItem(row._user, row._id_user)

    def filaSeleccionada(self):
        if len(self.ui.tw_registrosUsuarioRol.selectedItems()) > 0:
            row = self.ui.tw_registrosUsuarioRol.selectedItems()[0].row()
            self.ui.cbx_rol.setCurrentText(self.ui.tw_registrosUsuarioRol.item(row, 4).text())
            self.ui.cbx_usuario.setCurrentText(self.ui.tw_registrosUsuarioRol.item(row, 3).text())

    #CRUD
    # Actualizar solo agrega, sin validar datos por el momento
    def btnActualizar(self):

        # Verifica que no tenga campos vacios
        if self.ui.cbx_rol.currentIndex() == -1 or self.ui.cbx_usuario.currentIndex() == -1:
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        # Encontrando el id_user y id_rol
        self.UserRol.id_user = self.ui.cbx_usuario.currentData()
        self.UserRol.id_rol = self.ui.cbx_rol.currentData()

        # Asignando el id_UserRol de id_user
        self.listUserRol = self.dtur.listUsuarioRol()
        for row in self.listUserRol:
            if str(self.UserRol.id_user) == str(row.id_user):
                self.UserRol.id_UserRol = row.id_UserRol

        print(self.UserRol.id_UserRol)
        # Mandando objeto a capa negocios
        resultado = self.ngUserRol.actualizarUserRol(self.UserRol)
        match resultado:
            case -1:
                QMessageBox.warning(self, "Error", "No se ha podido agregar el UserRol", QMessageBox.Ok)
            case 1:
                QMessageBox.information(self, "Éxito", "Se ha agregado el UserRol correctamente", QMessageBox.Ok)
                self.limpiarCampos()
                self.cargarTblUserRol()
            case 2:
                QMessageBox.warning(self, "Error", "El Usuario ya tiene ese Rol", QMessageBox.Ok)

    def btnBuscar(self):
        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el usuario")
            self.limpiarCampos()
            self.cargarTblUserRol()
            return

        self.UserRol.user = self.ui.le_buscador.text()
        self.listUserRol = self.dtur.listUsuarioRol()

        row = 0
        for r in self.listUserRol:
            if str(self.UserRol.user) == str(r.user):
                self.ui.tw_registrosUsuarioRol.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r._idUserRol)))
                self.ui.tw_registrosUsuarioRol.setItem(row, 1, QtWidgets.QTableWidgetItem(str(r._user)))
                self.ui.tw_registrosUsuarioRol.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r._id_rol)))
                self.ui.tw_registrosUsuarioRol.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r._user)))
                self.ui.tw_registrosUsuarioRol.setItem(row, 4, QtWidgets.QTableWidgetItem(str(r._rol)))
                row += 1

        self.ui.tw_registrosUsuarioRol.setRowCount(row)
        self.ui.tw_registrosUsuarioRol.setColumnHidden(0, True)
        self.ui.tw_registrosUsuarioRol.setColumnHidden(1, True)
        self.ui.tw_registrosUsuarioRol.setColumnHidden(2, True)
