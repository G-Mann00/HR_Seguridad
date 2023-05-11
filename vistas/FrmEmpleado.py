# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmEmpleado.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from recursos import iconosApp_rc


class Ui_FrmEmpleado(object):
    def setupUi(self, FrmEmpleado):
        FrmEmpleado.setObjectName("FrmEmpleado")
        FrmEmpleado.resize(800, 969)
        FrmEmpleado.setMinimumSize(QtCore.QSize(800, 969))
        self.gbox_datosEmpleado = QtWidgets.QGroupBox(FrmEmpleado)
        self.gbox_datosEmpleado.setGeometry(QtCore.QRect(20, 20, 751, 621))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gbox_datosEmpleado.setFont(font)
        self.gbox_datosEmpleado.setObjectName("gbox_datosEmpleado")
        self.lbl_identificador = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_identificador.setGeometry(QtCore.QRect(30, 50, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_identificador.setFont(font)
        self.lbl_identificador.setObjectName("lbl_identificador")
        self.le_id = QtWidgets.QLineEdit(self.gbox_datosEmpleado)
        self.le_id.setGeometry(QtCore.QRect(30, 80, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_id.setFont(font)
        self.le_id.setReadOnly(True)
        self.le_id.setObjectName("le_id")
        self.lbl_nombre = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_nombre.setGeometry(QtCore.QRect(30, 130, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.le_primerNombre = QtWidgets.QLineEdit(self.gbox_datosEmpleado)
        self.le_primerNombre.setGeometry(QtCore.QRect(30, 160, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_primerNombre.setFont(font)
        self.le_primerNombre.setText("")
        self.le_primerNombre.setObjectName("le_primerNombre")
        self.le_ultimoNombre = QtWidgets.QLineEdit(self.gbox_datosEmpleado)
        self.le_ultimoNombre.setGeometry(QtCore.QRect(220, 160, 251, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_ultimoNombre.setFont(font)
        self.le_ultimoNombre.setText("")
        self.le_ultimoNombre.setObjectName("le_ultimoNombre")
        self.lbl_correoElectronico = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_correoElectronico.setGeometry(QtCore.QRect(30, 210, 151, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_correoElectronico.setFont(font)
        self.lbl_correoElectronico.setObjectName("lbl_correoElectronico")
        self.le_correo = QtWidgets.QLineEdit(self.gbox_datosEmpleado)
        self.le_correo.setGeometry(QtCore.QRect(30, 240, 371, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_correo.setFont(font)
        self.le_correo.setText("")
        self.le_correo.setObjectName("le_correo")
        self.le_telefono = QtWidgets.QLineEdit(self.gbox_datosEmpleado)
        self.le_telefono.setGeometry(QtCore.QRect(30, 400, 171, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_telefono.setFont(font)
        self.le_telefono.setText("")
        self.le_telefono.setObjectName("le_telefono")
        self.lbl_numeroTelefono = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_numeroTelefono.setGeometry(QtCore.QRect(30, 370, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_numeroTelefono.setFont(font)
        self.lbl_numeroTelefono.setObjectName("lbl_numeroTelefono")
        self.lbl_fechaContratacion = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_fechaContratacion.setGeometry(QtCore.QRect(240, 370, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_fechaContratacion.setFont(font)
        self.lbl_fechaContratacion.setObjectName("lbl_fechaContratacion")
        self.de_fechaContratacion = QtWidgets.QDateEdit(self.gbox_datosEmpleado)
        self.de_fechaContratacion.setGeometry(QtCore.QRect(240, 400, 161, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.de_fechaContratacion.setFont(font)
        self.de_fechaContratacion.setObjectName("de_fechaContratacion")
        self.lbl_trabajo = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_trabajo.setGeometry(QtCore.QRect(30, 450, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_trabajo.setFont(font)
        self.lbl_trabajo.setObjectName("lbl_trabajo")
        self.cbx_trabajo = QtWidgets.QComboBox(self.gbox_datosEmpleado)
        self.cbx_trabajo.setGeometry(QtCore.QRect(30, 480, 371, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbx_trabajo.setFont(font)
        self.cbx_trabajo.setEditable(False)
        self.cbx_trabajo.setObjectName("cbx_trabajo")
        self.lbl_salario = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_salario.setGeometry(QtCore.QRect(430, 450, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_salario.setFont(font)
        self.lbl_salario.setObjectName("lbl_salario")
        self.le_salario = QtWidgets.QLineEdit(self.gbox_datosEmpleado)
        self.le_salario.setGeometry(QtCore.QRect(430, 480, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_salario.setFont(font)
        self.le_salario.setText("")
        self.le_salario.setObjectName("le_salario")
        self.lbl_manager = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_manager.setGeometry(QtCore.QRect(30, 530, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_manager.setFont(font)
        self.lbl_manager.setObjectName("lbl_manager")
        self.cbx_manager = QtWidgets.QComboBox(self.gbox_datosEmpleado)
        self.cbx_manager.setGeometry(QtCore.QRect(30, 560, 321, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbx_manager.setFont(font)
        self.cbx_manager.setObjectName("cbx_manager")
        self.lbl_departamento = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_departamento.setGeometry(QtCore.QRect(380, 530, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_departamento.setFont(font)
        self.lbl_departamento.setObjectName("lbl_departamento")
        self.cbx_departamento = QtWidgets.QComboBox(self.gbox_datosEmpleado)
        self.cbx_departamento.setGeometry(QtCore.QRect(380, 560, 321, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbx_departamento.setFont(font)
        self.cbx_departamento.setObjectName("cbx_departamento")
        self.btn_nuevo = QtWidgets.QPushButton(self.gbox_datosEmpleado)
        self.btn_nuevo.setGeometry(QtCore.QRect(610, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_nuevo.setFont(font)
        self.btn_nuevo.setStyleSheet("background-color:white")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconosCrud/clean40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_nuevo.setIcon(icon)
        self.btn_nuevo.setIconSize(QtCore.QSize(20, 20))
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.btn_eliminar = QtWidgets.QPushButton(self.gbox_datosEmpleado)
        self.btn_eliminar.setGeometry(QtCore.QRect(610, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("color:white;\n"
"background-color:rgb(201, 0, 0)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconosCrud/delete40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eliminar.setIcon(icon1)
        self.btn_eliminar.setIconSize(QtCore.QSize(20, 20))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_editar = QtWidgets.QPushButton(self.gbox_datosEmpleado)
        self.btn_editar.setGeometry(QtCore.QRect(610, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("color:white;\n"
"background-color:rgb(12, 91, 166)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconosCrud/edit40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editar.setIcon(icon2)
        self.btn_editar.setIconSize(QtCore.QSize(20, 20))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_agregar = QtWidgets.QPushButton(self.gbox_datosEmpleado)
        self.btn_agregar.setGeometry(QtCore.QRect(610, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("color:white;\n"
"background-color:rgb(7, 125, 8)")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconosCrud/add40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon3)
        self.btn_agregar.setIconSize(QtCore.QSize(20, 20))
        self.btn_agregar.setObjectName("btn_agregar")
        self.lbl_apellido = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_apellido.setGeometry(QtCore.QRect(220, 130, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_apellido.setFont(font)
        self.lbl_apellido.setObjectName("lbl_apellido")
        self.le_confirmarCorreo = QtWidgets.QLineEdit(self.gbox_datosEmpleado)
        self.le_confirmarCorreo.setGeometry(QtCore.QRect(30, 320, 371, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_confirmarCorreo.setFont(font)
        self.le_confirmarCorreo.setText("")
        self.le_confirmarCorreo.setObjectName("le_confirmarCorreo")
        self.lbl_confirmarCorreo = QtWidgets.QLabel(self.gbox_datosEmpleado)
        self.lbl_confirmarCorreo.setGeometry(QtCore.QRect(30, 290, 231, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_confirmarCorreo.setFont(font)
        self.lbl_confirmarCorreo.setObjectName("lbl_confirmarCorreo")
        self.le_buscador = QtWidgets.QLineEdit(FrmEmpleado)
        self.le_buscador.setGeometry(QtCore.QRect(60, 670, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.le_buscador.setFont(font)
        self.le_buscador.setText("")
        self.le_buscador.setObjectName("le_buscador")
        self.btn_buscar = QtWidgets.QPushButton(FrmEmpleado)
        self.btn_buscar.setGeometry(QtCore.QRect(630, 670, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_buscar.setFont(font)
        self.btn_buscar.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconosCrud/search40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar.setIcon(icon4)
        self.btn_buscar.setObjectName("btn_buscar")
        self.tw_registrosEmpleado = QtWidgets.QTableWidget(FrmEmpleado)
        self.tw_registrosEmpleado.setGeometry(QtCore.QRect(20, 720, 751, 231))
        self.tw_registrosEmpleado.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tw_registrosEmpleado.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_registrosEmpleado.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tw_registrosEmpleado.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_registrosEmpleado.setObjectName("tw_registrosEmpleado")
        self.tw_registrosEmpleado.setColumnCount(10)
        self.tw_registrosEmpleado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registrosEmpleado.setHorizontalHeaderItem(9, item)
        self.tw_registrosEmpleado.horizontalHeader().setDefaultSectionSize(150)
        self.tw_registrosEmpleado.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(FrmEmpleado)
        QtCore.QMetaObject.connectSlotsByName(FrmEmpleado)
        FrmEmpleado.setTabOrder(self.btn_nuevo, self.btn_agregar)
        FrmEmpleado.setTabOrder(self.btn_agregar, self.btn_editar)
        FrmEmpleado.setTabOrder(self.btn_editar, self.btn_eliminar)
        FrmEmpleado.setTabOrder(self.btn_eliminar, self.le_id)
        FrmEmpleado.setTabOrder(self.le_id, self.le_primerNombre)
        FrmEmpleado.setTabOrder(self.le_primerNombre, self.le_ultimoNombre)
        FrmEmpleado.setTabOrder(self.le_ultimoNombre, self.le_correo)
        FrmEmpleado.setTabOrder(self.le_correo, self.le_confirmarCorreo)
        FrmEmpleado.setTabOrder(self.le_confirmarCorreo, self.le_telefono)
        FrmEmpleado.setTabOrder(self.le_telefono, self.de_fechaContratacion)
        FrmEmpleado.setTabOrder(self.de_fechaContratacion, self.cbx_trabajo)
        FrmEmpleado.setTabOrder(self.cbx_trabajo, self.le_salario)
        FrmEmpleado.setTabOrder(self.le_salario, self.cbx_manager)
        FrmEmpleado.setTabOrder(self.cbx_manager, self.cbx_departamento)
        FrmEmpleado.setTabOrder(self.cbx_departamento, self.le_buscador)
        FrmEmpleado.setTabOrder(self.le_buscador, self.btn_buscar)

    def retranslateUi(self, FrmEmpleado):
        _translate = QtCore.QCoreApplication.translate
        FrmEmpleado.setWindowTitle(_translate("FrmEmpleado", "Gestion de Empleados"))
        self.gbox_datosEmpleado.setTitle(_translate("FrmEmpleado", "Datos del Empleado "))
        self.lbl_identificador.setText(_translate("FrmEmpleado", "Identificador"))
        self.lbl_nombre.setText(_translate("FrmEmpleado", "Primer Nombre"))
        self.lbl_correoElectronico.setText(_translate("FrmEmpleado", "Correo Electrónico"))
        self.lbl_numeroTelefono.setText(_translate("FrmEmpleado", "Número de Teléfono"))
        self.lbl_fechaContratacion.setText(_translate("FrmEmpleado", "Fecha de Contratación"))
        self.lbl_trabajo.setText(_translate("FrmEmpleado", "Trabajo"))
        self.lbl_salario.setText(_translate("FrmEmpleado", "Salario"))
        self.lbl_manager.setText(_translate("FrmEmpleado", "Manager"))
        self.lbl_departamento.setText(_translate("FrmEmpleado", "Departamento"))
        self.btn_nuevo.setToolTip(_translate("FrmEmpleado", "<html><head/><body><p><span style=\" font-weight:400;\">Limpia los campos del formulario</span></p></body></html>"))
        self.btn_nuevo.setText(_translate("FrmEmpleado", "Nuevo"))
        self.btn_eliminar.setToolTip(_translate("FrmEmpleado", "<html><head/><body><p><span style=\" font-weight:400;\">Elimina un registro</span></p></body></html>"))
        self.btn_eliminar.setText(_translate("FrmEmpleado", "Eliminar"))
        self.btn_editar.setToolTip(_translate("FrmEmpleado", "<html><head/><body><p><span style=\" font-weight:400;\">Edita un registro ya existente</span></p></body></html>"))
        self.btn_editar.setText(_translate("FrmEmpleado", "Editar"))
        self.btn_agregar.setToolTip(_translate("FrmEmpleado", "<html><head/><body><p><span style=\" font-weight:400;\">Crea un nuevo registro</span></p></body></html>"))
        self.btn_agregar.setText(_translate("FrmEmpleado", "Agregar"))
        self.lbl_apellido.setText(_translate("FrmEmpleado", "Primer Apellido"))
        self.lbl_confirmarCorreo.setText(_translate("FrmEmpleado", "Confirmar Correo Electrónico"))
        self.btn_buscar.setText(_translate("FrmEmpleado", "Buscar"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(0)
        item.setText(_translate("FrmEmpleado", "ID"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(1)
        item.setText(_translate("FrmEmpleado", "Primer Nombre"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(2)
        item.setText(_translate("FrmEmpleado", "Último Nombre"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(3)
        item.setText(_translate("FrmEmpleado", "Correo"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(4)
        item.setText(_translate("FrmEmpleado", "Teléfono"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(5)
        item.setText(_translate("FrmEmpleado", "Contratación"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(6)
        item.setText(_translate("FrmEmpleado", "Trabajo"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(7)
        item.setText(_translate("FrmEmpleado", "Salario"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(8)
        item.setText(_translate("FrmEmpleado", "Manager"))
        item = self.tw_registrosEmpleado.horizontalHeaderItem(9)
        item.setText(_translate("FrmEmpleado", "Departamento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmEmpleado = QtWidgets.QWidget()
    ui = Ui_FrmEmpleado()
    ui.setupUi(FrmEmpleado)
    FrmEmpleado.show()
    sys.exit(app.exec_())
