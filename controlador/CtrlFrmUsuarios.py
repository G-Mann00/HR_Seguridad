from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from datos.conexion import Conexion
from entidades.VwGestionUsuario import VwGestionUsuario
from vistas.FrmUsuarios import Ui_Form
from datos.Dt_tbl_user import Dt_tbl_user
from entidades.Tbl_user import tbl_user

class CtrlFrmUsuarios(QtWidgets.QMainWindow):
    dUser = Dt_tbl_user()
    usuario = tbl_user()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatosTabla()

    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.btnAgregar)
        self.ui.tw_registroUsuarios.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.tw_registroUsuarios.clicked.connect(self.filaSeleccionada)
        self.ui.btn_editar.clicked.connect(self.btnEditar)
        self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        self.ui.le_buscador.textChanged.connect(self.refresh)
        self.ui.le_identificador.textChanged.connect(self.validarIdentificador)

        pass


    def limpiarCampos(self):
        self.ui.le_buscador.setText("")
        self.ui.le_identificador.setText("")
        self.ui.le_usuario.setText("")
        self.ui.le_pwd.setText("")
        self.ui.le_nombre.setText("")
        self.ui.le_apellido.setText("")
        self.ui.le_email.setText("")
        #self.ui.le_contrasenaTemp.setText("")
        self.ui.cb_estado.setChecked(False)

    def cargarDatosTabla(self):
        dUser = Dt_tbl_user()
        listaUsuarios = dUser.listUsuarios()
        self.ui.tw_registroUsuarios.setRowCount(len(listaUsuarios))
        self.ui.tw_registroUsuarios.setColumnCount(6)
        row = 0
        for r in listaUsuarios:
            self.ui.tw_registroUsuarios.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r._id_user)))
            self.ui.tw_registroUsuarios.setItem(row, 1, QtWidgets.QTableWidgetItem(str(r._user)))
            self.ui.tw_registroUsuarios.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r._pwd)))
            self.ui.tw_registroUsuarios.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r._nombres)))
            self.ui.tw_registroUsuarios.setItem(row, 4, QtWidgets.QTableWidgetItem(str(r._apellidos)))
            self.ui.tw_registroUsuarios.setItem(row, 5, QtWidgets.QTableWidgetItem(str(r._email)))
            row += 1

    def filaSeleccionada(self):
        if len(self.ui.tw_registroUsuarios.selectedItems()) > 0:
            row = self.ui.tw_registroUsuarios.selectedItems()[0].row()
            self.ui.le_identificador.setText(self.ui.tw_registroUsuarios.item(row, 0).text())
            self.ui.le_usuario.setText(self.ui.tw_registroUsuarios.item(row, 1).text())
            self.ui.le_pwd.setText(self.ui.tw_registroUsuarios.item(row, 2).text())
            self.ui.le_nombre.setText(self.ui.tw_registroUsuarios.item(row, 3).text())
            self.ui.le_apellido.setText(self.ui.tw_registroUsuarios.item(row, 4).text())
            self.ui.le_email.setText(self.ui.tw_registroUsuarios.item(row, 5).text())


    def btnBuscar(self):
        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese un dato")
            return

        usuario = tbl_user()
        self.usuario.user = self.ui.le_buscador.text()
        listaUsuarios= self.dUser.buscarUsuario(self.user)

        self.ui.tw_registroUsuarios.setRowCount(len(listaUsuarios))
        self.ui.tw_registroUsuarios.setColumnCount(3)
        row = 0
        for r in listaUsuarios:
            self.ui.tw_registroUsuarios.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r._id_user)))
            self.ui.tw_registroUsuarios.setItem(row, 1, QtWidgets.QTableWidgetItem(str(r._user)))
            self.ui.tw_registroUsuarios.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r._pwd)))
            self.ui.tw_registroUsuarios.setItem(row, 3, QtWidgets.QTableWidgetItem(str(r._nombres)))
            self.ui.tw_registroUsuarios.setItem(row, 4, QtWidgets.QTableWidgetItem(str(r._apellidos)))
            self.ui.tw_registroUsuarios.setItem(row, 5, QtWidgets.QTableWidgetItem(str(r._email)))
            row += 1

    def refresh(self):
        self.cargarDatosTabla()
        self.ui.le_buscador.setText("")
        self.ui.le_identificador.setText("")
        self.ui.le_usuario.setText("")
        self.ui.le_pwd.setText("")
        self.ui.le_nombre.setText("")
        self.ui.le_apellido.setText("")
        self.ui.le_email.setText("")
        self.ui.cb_estado.setChecked(False)

    def btnAgregar(self):
        if self.ui.le_usuario.text() == "" or self.ui.le_pwd.text() == "" or self.ui.le_nombre.text() == "" or self.ui.le_apellido.text() == "" or self.ui.le_email.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        self.user.user = self.ui.le_usuario.text()
        self.user.pwd = self.ui.le_pwd.text()
        self.user.nombres = self.ui.le_nombre.text()
        self.user.apellidos = self.ui.le_apellido.text()
        self.user.email = self.ui.le_email.text()
        self.user.estado = self.ui.cb_estado.isChecked()

        if self.dUser.agregarUsuario(self.user):
            QMessageBox.information(self, "Exito", "Usuario agregado correctamente")
            self.cargarDatosTabla()
            self.limpiarCampos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo agregar el usuario")

    def btnEditar(self):
        if self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Seleccione un usuario")
            return

        if self.ui.le_usuario.text() == "" or self.ui.le_pwd.text() == "" or self.ui.le_nombre.text() == "" or self.ui.le_apellido.text() == "" or self.ui.le_email.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        self.user.id_user = self.ui.le_identificador.text()
        self.user.user = self.ui.le_usuario.text()
        self.user.pwd = self.ui.le_pwd.text()
        self.user.nombres = self.ui.le_nombre.text()
        self.user.apellidos = self.ui.le_apellido.text()
        self.user.email = self.ui.le_email.text()
        self.user.estado = self.ui.cb_estado.isChecked()

        if self.dUser.editarUsuario(self.user):
            QMessageBox.information(self, "Exito", "Usuario editado correctamente")
            self.cargarDatosTabla()
            self.limpiarCampos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo editar el usuario")

    def btnEliminar(self):
        if self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Seleccione un usuario")
            return

        self.user.id_user = self.ui.le_identificador.text()

        if self.dUser.eliminarUsuario(self.user):
            QMessageBox.information(self, "Exito", "Usuario eliminado correctamente")
            self.cargarDatosTabla()
            self.limpiarCampos()
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el usuario")

    def validarIdentificador(self):
        if self.ui.le_identificador.text() == "":
            return True

        self.user.id_user = self.ui.le_identificador.text()

        if self.dUser.validarIdentificador(self.user):
            return True
        else:
            return False