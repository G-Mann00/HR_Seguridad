# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmUsuarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(814, 719)
        Form.setMinimumSize(QtCore.QSize(814, 719))
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.gb_datosUsuario = QtWidgets.QGroupBox(Form)
        self.gb_datosUsuario.setGeometry(QtCore.QRect(10, 20, 791, 361))
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
        self.lbl_usuario = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_usuario.setGeometry(QtCore.QRect(10, 100, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setObjectName("lbl_usuario")
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
        self.lbl_pwd.setGeometry(QtCore.QRect(370, 100, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_pwd.setFont(font)
        self.lbl_pwd.setObjectName("lbl_pwd")
        self.lbl_apellido = QtWidgets.QLabel(self.gb_datosUsuario)
        self.lbl_apellido.setGeometry(QtCore.QRect(370, 160, 81, 17))
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
        self.le_usuario = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_usuario.setGeometry(QtCore.QRect(10, 120, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_usuario.setFont(font)
        self.le_usuario.setObjectName("le_usuario")
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
        self.le_email.setGeometry(QtCore.QRect(10, 240, 341, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_email.setFont(font)
        self.le_email.setObjectName("le_email")
        self.cbx_estado = QtWidgets.QComboBox(self.gb_datosUsuario)
        self.cbx_estado.setGeometry(QtCore.QRect(10, 300, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbx_estado.setFont(font)
        self.cbx_estado.setObjectName("cbx_estado")
        self.cbx_estado.addItem("")
        self.le_pwd = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_pwd.setGeometry(QtCore.QRect(370, 120, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_pwd.setFont(font)
        self.le_pwd.setObjectName("le_pwd")
        self.le_apellido = QtWidgets.QLineEdit(self.gb_datosUsuario)
        self.le_apellido.setGeometry(QtCore.QRect(370, 180, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_apellido.setFont(font)
        self.le_apellido.setObjectName("le_apellido")
        self.btn_eliminar = QtWidgets.QPushButton(self.gb_datosUsuario)
        self.btn_eliminar.setGeometry(QtCore.QRect(650, 260, 111, 31))
        self.btn_eliminar.setMinimumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("color: White;\n"
"background-color: rgb(201,0,0)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconosCrud/delete40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eliminar.setIcon(icon)
        self.btn_eliminar.setIconSize(QtCore.QSize(20, 20))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_editar = QtWidgets.QPushButton(self.gb_datosUsuario)
        self.btn_editar.setGeometry(QtCore.QRect(650, 200, 111, 31))
        self.btn_editar.setMinimumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("color: White;\n"
"background-color: rgb(12,91,166)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconosCrud/edit40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editar.setIcon(icon1)
        self.btn_editar.setIconSize(QtCore.QSize(20, 20))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_agregar = QtWidgets.QPushButton(self.gb_datosUsuario)
        self.btn_agregar.setGeometry(QtCore.QRect(650, 140, 111, 31))
        self.btn_agregar.setMinimumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("color: White;\n"
"background-color:rgb(7,125,8)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconosCrud/add40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon2)
        self.btn_agregar.setIconSize(QtCore.QSize(20, 20))
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_limpiar = QtWidgets.QPushButton(self.gb_datosUsuario)
        self.btn_limpiar.setGeometry(QtCore.QRect(650, 80, 111, 31))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconosCrud/clean40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_limpiar.setIcon(icon3)
        self.btn_limpiar.setIconSize(QtCore.QSize(20, 20))
        self.btn_limpiar.setObjectName("btn_limpiar")
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
        self.le_filtro = QtWidgets.QLineEdit(Form)
        self.le_filtro.setGeometry(QtCore.QRect(250, 420, 381, 25))
        self.le_filtro.setObjectName("le_filtro")
        self.tv_usuario = QtWidgets.QTableView(Form)
        self.tv_usuario.setGeometry(QtCore.QRect(10, 490, 791, 192))
        self.tv_usuario.setObjectName("tv_usuario")
        self.btn_buscar = QtWidgets.QPushButton(Form)
        self.btn_buscar.setGeometry(QtCore.QRect(660, 420, 111, 31))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.le_identificador, self.le_usuario)
        Form.setTabOrder(self.le_usuario, self.le_pwd)
        Form.setTabOrder(self.le_pwd, self.le_nombre)
        Form.setTabOrder(self.le_nombre, self.le_apellido)
        Form.setTabOrder(self.le_apellido, self.le_email)
        Form.setTabOrder(self.le_email, self.cbx_estado)
        Form.setTabOrder(self.cbx_estado, self.cbx_filtro)
        Form.setTabOrder(self.cbx_filtro, self.le_filtro)
        Form.setTabOrder(self.le_filtro, self.tv_usuario)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestión de Usuarios"))
        self.gb_datosUsuario.setTitle(_translate("Form", "Datos del Usuario       "))
        self.lbl_identificador.setText(_translate("Form", "<html><head/><body><p>Identificador:      </p></body></html>"))
        self.lbl_usuario.setText(_translate("Form", "Usuario:"))
        self.lbl_nombre.setText(_translate("Form", "Nombres:"))
        self.lbl_email.setText(_translate("Form", "Correo Electrónico: "))
        self.lbl_estado.setText(_translate("Form", "Estado:"))
        self.lbl_pwd.setText(_translate("Form", "Contraseña:"))
        self.lbl_apellido.setText(_translate("Form", "Apellidos:"))
        self.cbx_estado.setItemText(0, _translate("Form", "-- Seleccionar --"))
        self.btn_eliminar.setText(_translate("Form", "Eliminar"))
        self.btn_editar.setToolTip(_translate("Form", "<html><head/><body><p><a name=\"docs-internal-guid-9f32f1a0-7fff-3aa2-c71f-d8139ac015ba\"/><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">E</span><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">dita un registro ya existente</span></p></body></html>"))
        self.btn_editar.setText(_translate("Form", "Editar"))
        self.btn_agregar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">Crea un registro</span></p></body></html>"))
        self.btn_agregar.setText(_translate("Form", "Agregar"))
        self.btn_limpiar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Limpia los campos del formulario</span></p></body></html>"))
        self.btn_limpiar.setText(_translate("Form", "Nuevo"))
        self.lbl_filtro.setText(_translate("Form", "Filtro:"))
        self.cbx_filtro.setItemText(0, _translate("Form", "-- Seleccionar --"))
        self.btn_buscar.setText(_translate("Form", "Buscar"))
import iconosBotones_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
