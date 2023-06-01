from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from datos.conexion import Conexion
from entidades.VwGestionUsuario import VwGestionUsuario
from vistas.FrmUsuarios import Ui_Form
from datos.Dt_tbl_user import Dt_tbl_user
from entidades.Tbl_user import tbl_user

class CtrlFrmUsuarios(QtWidgets.QMainWindow):
    dUser = Dt_tbl_user()
    user = tbl_user()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarDatosTabla()

    def initControlGui(self):
        # self.ui.btn_agregar.clicked.connect(self.btnAgregar)
        self.ui.tw_registroUsuarios.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_limpiar.clicked.connect(self.limpiarCampos)
        self.ui.tw_registroUsuarios.clicked.connect(self.filaSeleccionada)
        # self.ui.btn_editar.clicked.connect(self.btnEditar)
        # self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        # self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        # self.ui.le_buscador.textChanged.connect(self.refresh)
        # self.ui.le_identificador.textChanged.connect(self.validarIdentificador)

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
            self.ui

    def btnBuscar(self):

        if self.ui.le_buscador.text() == "":
            QMessageBox.warning(self, "Error", "Debe ingresar un valor para buscar")
            return

        if self.ui.cbx_filtro.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Debe seleccionar un filtro para buscar")
            return

        cadena = self.ui.le_buscador.text()
        if self.ui.cbx_filtro.currentIndex() == 1:
            listaUser = self.dUser.buscarPorUsuario(cadena)
        else:
            listaUser = self.dUser.buscarPorNombre(cadena)

        self.ui.tw_registroUsuarios.setRowCount(len(listaUser))
        self.ui.tw_registroUsuarios.setColumnCount(6)
        row = 0
        for u in listaUser:
            self.ui.tw_registroUsuarios.setItem(row, 0, QtWidgets.QTableWidgetItem(str(u._id_user)))
            self.ui.tw_registroUsuarios.setItem(row, 1, QtWidgets.QTableWidgetItem(str(u._user)))
            self.ui.tw_registroUsuarios.setItem(row, 2, QtWidgets.QTableWidgetItem(str(u._pwd)))
            self.ui.tw_registroUsuarios.setItem(row, 3, QtWidgets.QTableWidgetItem(str(u._nombres)))
            self.ui.tw_registroUsuarios.setItem(row, 4, QtWidgets.QTableWidgetItem(str(u._apellidos)))
            self.ui.tw_registroUsuarios.setItem(row, 5, QtWidgets.QTableWidgetItem(str(u._email)))
            row += 1
