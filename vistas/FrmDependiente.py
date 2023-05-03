# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmDependiente.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmDependiente(object):
    def setupUi(self, FrmDependiente):
        FrmDependiente.setObjectName("FrmDependiente")
        FrmDependiente.resize(800, 729)
        FrmDependiente.setMinimumSize(QtCore.QSize(800, 729))
        self.gbox_datosDependiente = QtWidgets.QGroupBox(FrmDependiente)
        self.gbox_datosDependiente.setGeometry(QtCore.QRect(30, 30, 741, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gbox_datosDependiente.setFont(font)
        self.gbox_datosDependiente.setObjectName("gbox_datosDependiente")
        self.lbl_identificador = QtWidgets.QLabel(self.gbox_datosDependiente)
        self.lbl_identificador.setGeometry(QtCore.QRect(30, 50, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_identificador.setFont(font)
        self.lbl_identificador.setObjectName("lbl_identificador")
        self.le_id = QtWidgets.QLineEdit(self.gbox_datosDependiente)
        self.le_id.setGeometry(QtCore.QRect(30, 80, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_id.setFont(font)
        self.le_id.setReadOnly(True)
        self.le_id.setObjectName("le_id")
        self.lbl_nombre = QtWidgets.QLabel(self.gbox_datosDependiente)
        self.lbl_nombre.setGeometry(QtCore.QRect(30, 130, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.le_primerNombre = QtWidgets.QLineEdit(self.gbox_datosDependiente)
        self.le_primerNombre.setGeometry(QtCore.QRect(30, 160, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_primerNombre.setFont(font)
        self.le_primerNombre.setText("")
        self.le_primerNombre.setObjectName("le_primerNombre")
        self.le_ultimoNombre = QtWidgets.QLineEdit(self.gbox_datosDependiente)
        self.le_ultimoNombre.setGeometry(QtCore.QRect(220, 160, 251, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_ultimoNombre.setFont(font)
        self.le_ultimoNombre.setText("")
        self.le_ultimoNombre.setObjectName("le_ultimoNombre")
        self.lbl_relacion = QtWidgets.QLabel(self.gbox_datosDependiente)
        self.lbl_relacion.setGeometry(QtCore.QRect(30, 210, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_relacion.setFont(font)
        self.lbl_relacion.setObjectName("lbl_relacion")
        self.le_relacion = QtWidgets.QLineEdit(self.gbox_datosDependiente)
        self.le_relacion.setGeometry(QtCore.QRect(30, 240, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_relacion.setFont(font)
        self.le_relacion.setText("")
        self.le_relacion.setObjectName("le_relacion")
        self.cmb_empleado = QtWidgets.QComboBox(self.gbox_datosDependiente)
        self.cmb_empleado.setGeometry(QtCore.QRect(30, 320, 201, 25))
        self.cmb_empleado.setObjectName("cmb_empleado")
        self.lbl_empleado = QtWidgets.QLabel(self.gbox_datosDependiente)
        self.lbl_empleado.setGeometry(QtCore.QRect(30, 290, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_empleado.setFont(font)
        self.lbl_empleado.setObjectName("lbl_empleado")
        self.btn_limpiar = QtWidgets.QPushButton(self.gbox_datosDependiente)
        self.btn_limpiar.setGeometry(QtCore.QRect(600, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setStyleSheet("border-style:outset;\n"
"background-color:white")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.btn_agregar = QtWidgets.QPushButton(self.gbox_datosDependiente)
        self.btn_agregar.setGeometry(QtCore.QRect(600, 110, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("color:white;\n"
"background-color:rgb(76, 154, 42);\n"
"border-style: outset")
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_editar = QtWidgets.QPushButton(self.gbox_datosDependiente)
        self.btn_editar.setGeometry(QtCore.QRect(600, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("color:white;\n"
"background-color:rgb(53, 132, 228);\n"
"border-style: outset")
        self.btn_editar.setObjectName("btn_editar")
        self.btn_eliminar = QtWidgets.QPushButton(self.gbox_datosDependiente)
        self.btn_eliminar.setGeometry(QtCore.QRect(600, 230, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("color:white;\n"
"background-color:rgb(237, 51, 59);\n"
"border-style: outset")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.le_buscador = QtWidgets.QLineEdit(FrmDependiente)
        self.le_buscador.setGeometry(QtCore.QRect(50, 430, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.le_buscador.setFont(font)
        self.le_buscador.setText("")
        self.le_buscador.setObjectName("le_buscador")
        self.tbw_registrosDependientes = QtWidgets.QTableView(FrmDependiente)
        self.tbw_registrosDependientes.setGeometry(QtCore.QRect(50, 480, 681, 221))
        self.tbw_registrosDependientes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tbw_registrosDependientes.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tbw_registrosDependientes.setObjectName("tbw_registrosDependientes")
        self.btn_buscar = QtWidgets.QPushButton(FrmDependiente)
        self.btn_buscar.setGeometry(QtCore.QRect(620, 430, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_buscar.setFont(font)
        self.btn_buscar.setStyleSheet("")
        self.btn_buscar.setObjectName("btn_buscar")

        self.retranslateUi(FrmDependiente)
        QtCore.QMetaObject.connectSlotsByName(FrmDependiente)

    def retranslateUi(self, FrmDependiente):
        _translate = QtCore.QCoreApplication.translate
        FrmDependiente.setWindowTitle(_translate("FrmDependiente", "Gestion de Dependientes"))
        self.gbox_datosDependiente.setTitle(_translate("FrmDependiente", "Datos del Dependiente  "))
        self.lbl_identificador.setText(_translate("FrmDependiente", "Identificador"))
        self.lbl_nombre.setText(_translate("FrmDependiente", "Nombre"))
        self.lbl_relacion.setText(_translate("FrmDependiente", "Relacion"))
        self.lbl_empleado.setText(_translate("FrmDependiente", "Empleado"))
        self.btn_limpiar.setText(_translate("FrmDependiente", "Limpiar"))
        self.btn_agregar.setText(_translate("FrmDependiente", "Agregar"))
        self.btn_editar.setText(_translate("FrmDependiente", "Editar"))
        self.btn_eliminar.setText(_translate("FrmDependiente", "Eliminar"))
        self.btn_buscar.setText(_translate("FrmDependiente", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDependiente = QtWidgets.QWidget()
    ui = Ui_FrmDependiente()
    ui.setupUi(FrmDependiente)
    FrmDependiente.show()
    sys.exit(app.exec_())