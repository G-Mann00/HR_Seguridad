# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmAsignarPermisos.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from recursos import iconosApp_rc


class Ui_FrmAsignarPermisos(object):
    def setupUi(self, FrmAsignarPermisos):
        FrmAsignarPermisos.setObjectName("FrmAsignarPermisos")
        FrmAsignarPermisos.resize(800, 405)
        FrmAsignarPermisos.setMinimumSize(QtCore.QSize(0, 0))
        self.gb_datosAsignarPermisos = QtWidgets.QGroupBox(FrmAsignarPermisos)
        self.gb_datosAsignarPermisos.setGeometry(QtCore.QRect(30, 30, 731, 351))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gb_datosAsignarPermisos.setFont(font)
        self.gb_datosAsignarPermisos.setObjectName("gb_datosAsignarPermisos")
        self.cbx_rol = QtWidgets.QComboBox(self.gb_datosAsignarPermisos)
        self.cbx_rol.setGeometry(QtCore.QRect(40, 80, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbx_rol.setFont(font)
        self.cbx_rol.setObjectName("cbx_rol")
        self.lbl_rol = QtWidgets.QLabel(self.gb_datosAsignarPermisos)
        self.lbl_rol.setGeometry(QtCore.QRect(40, 50, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_rol.setFont(font)
        self.lbl_rol.setObjectName("lbl_rol")
        self.gb_permisos = QtWidgets.QGroupBox(self.gb_datosAsignarPermisos)
        self.gb_permisos.setGeometry(QtCore.QRect(40, 220, 631, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gb_permisos.setFont(font)
        self.gb_permisos.setObjectName("gb_permisos")
        self.cb_guardar = QtWidgets.QCheckBox(self.gb_permisos)
        self.cb_guardar.setGeometry(QtCore.QRect(20, 50, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_guardar.setFont(font)
        self.cb_guardar.setObjectName("cb_guardar")
        self.cb_editar = QtWidgets.QCheckBox(self.gb_permisos)
        self.cb_editar.setGeometry(QtCore.QRect(130, 50, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_editar.setFont(font)
        self.cb_editar.setObjectName("cb_editar")
        self.cb_eliminar = QtWidgets.QCheckBox(self.gb_permisos)
        self.cb_eliminar.setGeometry(QtCore.QRect(230, 50, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cb_eliminar.setFont(font)
        self.cb_eliminar.setObjectName("cb_eliminar")
        self.btn_guardar = QtWidgets.QPushButton(self.gb_datosAsignarPermisos)
        self.btn_guardar.setGeometry(QtCore.QRect(520, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_guardar.setFont(font)
        self.btn_guardar.setStyleSheet("color:white;\n"
"background-color:rgb(7, 125, 8)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconosCrud/add40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_guardar.setIcon(icon)
        self.btn_guardar.setIconSize(QtCore.QSize(20, 20))
        self.btn_guardar.setObjectName("btn_guardar")
        self.lbl_opcion = QtWidgets.QLabel(self.gb_datosAsignarPermisos)
        self.lbl_opcion.setGeometry(QtCore.QRect(40, 130, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_opcion.setFont(font)
        self.lbl_opcion.setObjectName("lbl_opcion")
        self.cbx_opcion = QtWidgets.QComboBox(self.gb_datosAsignarPermisos)
        self.cbx_opcion.setGeometry(QtCore.QRect(40, 160, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbx_opcion.setFont(font)
        self.cbx_opcion.setObjectName("cbx_opcion")

        self.retranslateUi(FrmAsignarPermisos)
        QtCore.QMetaObject.connectSlotsByName(FrmAsignarPermisos)
        FrmAsignarPermisos.setTabOrder(self.btn_guardar, self.cbx_rol)
        FrmAsignarPermisos.setTabOrder(self.cbx_rol, self.cbx_opcion)
        FrmAsignarPermisos.setTabOrder(self.cbx_opcion, self.cb_guardar)
        FrmAsignarPermisos.setTabOrder(self.cb_guardar, self.cb_editar)
        FrmAsignarPermisos.setTabOrder(self.cb_editar, self.cb_eliminar)

    def retranslateUi(self, FrmAsignarPermisos):
        _translate = QtCore.QCoreApplication.translate
        FrmAsignarPermisos.setWindowTitle(_translate("FrmAsignarPermisos", "Asignar Permisos"))
        self.gb_datosAsignarPermisos.setTitle(_translate("FrmAsignarPermisos", "Asignación de Permisos"))
        self.lbl_rol.setText(_translate("FrmAsignarPermisos", "Rol"))
        self.gb_permisos.setTitle(_translate("FrmAsignarPermisos", "Permisos:"))
        self.cb_guardar.setText(_translate("FrmAsignarPermisos", "Guardar"))
        self.cb_editar.setText(_translate("FrmAsignarPermisos", "Editar"))
        self.cb_eliminar.setText(_translate("FrmAsignarPermisos", "Eliminar"))
        self.btn_guardar.setToolTip(_translate("FrmAsignarPermisos", "<html><head/><body><p><span style=\" font-weight:400;\">Asignar las funciones que tiene permitido un rol</span></p></body></html>"))
        self.btn_guardar.setText(_translate("FrmAsignarPermisos", "Guardar Permisos"))
        self.lbl_opcion.setText(_translate("FrmAsignarPermisos", "Opción"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmAsignarPermisos = QtWidgets.QWidget()
    ui = Ui_FrmAsignarPermisos()
    ui.setupUi(FrmAsignarPermisos)
    FrmAsignarPermisos.show()
    sys.exit(app.exec_())