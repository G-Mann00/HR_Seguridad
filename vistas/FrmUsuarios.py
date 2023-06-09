# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmUsuarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from recursos import iconosApp_rc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(874, 719)
        Form.setMinimumSize(QtCore.QSize(814, 719))
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.gb_datosUsuario = QtWidgets.QGroupBox(Form)
        self.gb_datosUsuario.setGeometry(QtCore.QRect(10, 30, 851, 361))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gb_datosUsuario.setFont(font)
        self.gb_datosUsuario.setObjectName("gb_datosUsuario")
        self.lbl_identificador = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_identificador.setGeometry(QtCore.QRect(10, 40, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_identificador.setFont(font)
        self.lbl_identificador.setObjectName("lbl_identificador")
        self.lbl_nombre = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_nombre.setGeometry(QtCore.QRect(10, 160, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_email = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_email.setGeometry(QtCore.QRect(10, 220, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_email.setFont(font)
        self.lbl_email.setObjectName("lbl_email")
        self.lbl_estado = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_estado.setGeometry(QtCore.QRect(10, 280, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_estado.setFont(font)
        self.lbl_estado.setObjectName("lbl_estado")
        self.lbl_pwd = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_pwd.setGeometry(QtCore.QRect(360, 100, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_pwd.setFont(font)
        self.lbl_pwd.setObjectName("lbl_pwd")
        self.lbl_apellido = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_apellido.setGeometry(QtCore.QRect(360, 160, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_apellido.setFont(font)
        self.lbl_apellido.setObjectName("lbl_apellido")
        self.le_identificador = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_identificador.setGeometry(QtCore.QRect(10, 60, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_identificador.setFont(font)
        self.le_identificador.setReadOnly(True)
        self.le_identificador.setObjectName("le_identificador")
        self.le_nombre = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_nombre.setGeometry(QtCore.QRect(10, 180, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_nombre.setFont(font)
        self.le_nombre.setObjectName("le_nombre")
        self.le_email = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_email.setGeometry(QtCore.QRect(10, 240, 331, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_email.setFont(font)
        self.le_email.setObjectName("le_email")
        self.le_confirmarPwd = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_confirmarPwd.setGeometry(QtCore.QRect(360, 120, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_confirmarPwd.setFont(font)
        self.le_confirmarPwd.setObjectName("le_confirmarPwd")
        self.le_apellido = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_apellido.setGeometry(QtCore.QRect(360, 180, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_apellido.setFont(font)
        self.le_apellido.setObjectName("le_apellido")
        self.cb_estado = QtWidgets.QCheckBox(self.gb_datosUsuario)
        self.cb_estado.setGeometry(QtCore.QRect(11, 310, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_estado.setFont(font)
        self.cb_estado.setObjectName("cb_estado")
        self.lbl_usuario_3 = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_usuario_3.setGeometry(QtCore.QRect(360, 40, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_usuario_3.setFont(font)
        self.lbl_usuario_3.setObjectName("lbl_usuario_3")
        self.le_usuario = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_usuario.setGeometry(QtCore.QRect(360, 60, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_usuario.setFont(font)
        self.le_usuario.setObjectName("le_usuario")
        self.lbl_pwd_4 = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_pwd_4.setGeometry(QtCore.QRect(10, 100, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_pwd_4.setFont(font)
        self.lbl_pwd_4.setObjectName("lbl_pwd_4")
        self.le_pwd = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_pwd.setGeometry(QtCore.QRect(10, 120, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_pwd.setFont(font)
        self.le_pwd.setObjectName("le_pwd")
        self.le_comfirmarEmail = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_comfirmarEmail.setGeometry(QtCore.QRect(360, 240, 331, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_comfirmarEmail.setFont(font)
        self.le_comfirmarEmail.setObjectName("le_comfirmarEmail")
        self.lbl_email_5 = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_email_5.setGeometry(QtCore.QRect(360, 220, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_email_5.setFont(font)
        self.lbl_email_5.setObjectName("lbl_email_5")
        self.btn_editar = QtWidgets.QPushButton(self.gb_datosUsuario)
        self.btn_editar.setGeometry(QtCore.QRect(720, 180, 111, 31))
        self.btn_editar.setMinimumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("color: White;\n"
"background-color: rgb(12,91,166)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconosCrud/edit40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editar.setIcon(icon)
        self.btn_editar.setIconSize(QtCore.QSize(20, 20))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_agregar = QtWidgets.QPushButton(self.gb_datosUsuario)
        self.btn_agregar.setGeometry(QtCore.QRect(720, 120, 111, 31))
        self.btn_agregar.setMinimumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("color: White;\n"
"background-color:rgb(7,125,8)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconosCrud/add40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon1)
        self.btn_agregar.setIconSize(QtCore.QSize(20, 20))
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_limpiar = QtWidgets.QPushButton(self.gb_datosUsuario)
        self.btn_limpiar.setGeometry(QtCore.QRect(720, 60, 111, 31))
        self.btn_limpiar.setMinimumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setStyleSheet("color: Black;\n"
"background-color:white\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconosCrud/clean40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_limpiar.setIcon(icon2)
        self.btn_limpiar.setIconSize(QtCore.QSize(20, 20))
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.btn_eliminar = QtWidgets.QPushButton(self.gb_datosUsuario)
        self.btn_eliminar.setGeometry(QtCore.QRect(720, 240, 111, 31))
        self.btn_eliminar.setMinimumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("color: White;\n"
"background-color: rgb(201,0,0)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconosCrud/delete40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eliminar.setIcon(icon3)
        self.btn_eliminar.setIconSize(QtCore.QSize(20, 20))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.lbl_filtro = QtWidgets.QLabel(Form)
        self.lbl_filtro.setGeometry(QtCore.QRect(10, 426, 67, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_filtro.setFont(font)
        self.lbl_filtro.setObjectName("lbl_filtro")
        self.cbx_filtro = QtWidgets.QComboBox(Form)
        self.cbx_filtro.setGeometry(QtCore.QRect(70, 420, 141, 25))
        self.cbx_filtro.setObjectName("cbx_filtro")
        self.cbx_filtro.addItem("")
        self.cbx_filtro.addItem("")
        self.cbx_filtro.addItem("")
        self.le_buscador = QtWidgets.QLineEdit(Form)
        self.le_buscador.setGeometry(QtCore.QRect(250, 420, 461, 25))
        self.le_buscador.setObjectName("le_buscador")
        self.btn_buscar = QtWidgets.QPushButton(Form)
        self.btn_buscar.setGeometry(QtCore.QRect(740, 420, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_buscar.setFont(font)
        self.btn_buscar.setStyleSheet("color: Black;\n"
"background-color: rgb(255, 255, 255)")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconosCrud/search40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar.setIcon(icon4)
        self.btn_buscar.setIconSize(QtCore.QSize(20, 20))
        self.btn_buscar.setObjectName("btn_buscar")
        self.tw_registroUsuarios = QtWidgets.QTableWidget(Form)
        self.tw_registroUsuarios.setGeometry(QtCore.QRect(10, 480, 851, 201))
        self.tw_registroUsuarios.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tw_registroUsuarios.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_registroUsuarios.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tw_registroUsuarios.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_registroUsuarios.setObjectName("tw_registroUsuarios")
        self.tw_registroUsuarios.setColumnCount(7)
        self.tw_registroUsuarios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroUsuarios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroUsuarios.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroUsuarios.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroUsuarios.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroUsuarios.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroUsuarios.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroUsuarios.setHorizontalHeaderItem(6, item)
        self.tw_registroUsuarios.horizontalHeader().setDefaultSectionSize(284)
        self.tw_registroUsuarios.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.btn_limpiar, self.btn_agregar)
        Form.setTabOrder(self.btn_agregar, self.btn_editar)
        Form.setTabOrder(self.btn_editar, self.btn_eliminar)
        Form.setTabOrder(self.btn_eliminar, self.le_identificador)
        Form.setTabOrder(self.le_identificador, self.le_usuario)
        Form.setTabOrder(self.le_usuario, self.le_pwd)
        Form.setTabOrder(self.le_pwd, self.le_confirmarPwd)
        Form.setTabOrder(self.le_confirmarPwd, self.le_nombre)
        Form.setTabOrder(self.le_nombre, self.le_apellido)
        Form.setTabOrder(self.le_apellido, self.le_email)
        Form.setTabOrder(self.le_email, self.le_comfirmarEmail)
        Form.setTabOrder(self.le_comfirmarEmail, self.cb_estado)
        Form.setTabOrder(self.cb_estado, self.cbx_filtro)
        Form.setTabOrder(self.cbx_filtro, self.le_buscador)
        Form.setTabOrder(self.le_buscador, self.btn_buscar)
        Form.setTabOrder(self.btn_buscar, self.tw_registroUsuarios)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestión de Usuarios"))
        self.gb_datosUsuario.setTitle(_translate("Form", "Datos del Usuario       "))
        self.lbl_identificador.setText(_translate("Form", "<html><head/><body><p>Identificador:      </p></body></html>"))
        self.lbl_nombre.setText(_translate("Form", "Nombres:"))
        self.lbl_email.setText(_translate("Form", "Correo Electrónico: "))
        self.lbl_estado.setText(_translate("Form", "Estado:"))
        self.lbl_pwd.setText(_translate("Form", "Confirmar Contraseña:"))
        self.lbl_apellido.setText(_translate("Form", "Apellidos:"))
        self.cb_estado.setText(_translate("Form", "Activo"))
        self.lbl_usuario_3.setText(_translate("Form", "Usuario:"))
        self.lbl_pwd_4.setText(_translate("Form", "Contraseña:"))
        self.lbl_email_5.setText(_translate("Form", "Confirmar Correo Electrónico: "))
        self.btn_editar.setToolTip(_translate("Form", "<html><head/><body><p><a name=\"docs-internal-guid-9f32f1a0-7fff-3aa2-c71f-d8139ac015ba\"/><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">E</span><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">dita un registro ya existente</span></p></body></html>"))
        self.btn_editar.setText(_translate("Form", "Editar"))
        self.btn_agregar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">Crea un registro</span></p></body></html>"))
        self.btn_agregar.setText(_translate("Form", "Agregar"))
        self.btn_limpiar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Limpia los campos del formulario</span></p></body></html>"))
        self.btn_limpiar.setText(_translate("Form", "Nuevo"))
        self.btn_eliminar.setText(_translate("Form", "Eliminar"))
        self.lbl_filtro.setText(_translate("Form", "Filtro:"))
        self.cbx_filtro.setItemText(0, _translate("Form", "-- Seleccionar --"))
        self.cbx_filtro.setItemText(1, _translate("Form", "Usuario"))
        self.cbx_filtro.setItemText(2, _translate("Form", "Nombre"))
        self.btn_buscar.setText(_translate("Form", "Buscar"))
        item = self.tw_registroUsuarios.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tw_registroUsuarios.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Usuario"))
        item = self.tw_registroUsuarios.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Contraseña"))
        item = self.tw_registroUsuarios.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Nombres"))
        item = self.tw_registroUsuarios.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Apellidos"))
        item = self.tw_registroUsuarios.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Correo electrónico"))
        item = self.tw_registroUsuarios.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Estado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
