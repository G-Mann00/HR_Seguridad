# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmDepartamentos.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmDepartamentos(object):
    def setupUi(self, FrmDepartamentos):
        FrmDepartamentos.setObjectName("FrmDepartamentos")
        FrmDepartamentos.resize(677, 614)
        FrmDepartamentos.setMinimumSize(QtCore.QSize(677, 614))
        self.gb_datosDepartamento = QtWidgets.QGroupBox(FrmDepartamentos)
        self.gb_datosDepartamento.setGeometry(QtCore.QRect(20, 20, 631, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gb_datosDepartamento.setFont(font)
        self.gb_datosDepartamento.setObjectName("gb_datosDepartamento")
        self.lbl_identificador = QtWidgets.QLabel(self.gb_datosDepartamento)
        self.lbl_identificador.setGeometry(QtCore.QRect(30, 50, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_identificador.setFont(font)
        self.lbl_identificador.setObjectName("lbl_identificador")
        self.lbl_nombre = QtWidgets.QLabel(self.gb_datosDepartamento)
        self.lbl_nombre.setGeometry(QtCore.QRect(30, 130, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_localizacion = QtWidgets.QLabel(self.gb_datosDepartamento)
        self.lbl_localizacion.setGeometry(QtCore.QRect(30, 210, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_localizacion.setFont(font)
        self.lbl_localizacion.setObjectName("lbl_localizacion")
        self.le_identificador = QtWidgets.QLineEdit(self.gb_datosDepartamento)
        self.le_identificador.setGeometry(QtCore.QRect(30, 80, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_identificador.setFont(font)
        self.le_identificador.setObjectName("le_identificador")
        self.le_nombre = QtWidgets.QLineEdit(self.gb_datosDepartamento)
        self.le_nombre.setGeometry(QtCore.QRect(30, 160, 361, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_nombre.setFont(font)
        self.le_nombre.setObjectName("le_nombre")
        self.cbx_localizacion = QtWidgets.QComboBox(self.gb_datosDepartamento)
        self.cbx_localizacion.setGeometry(QtCore.QRect(30, 250, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cbx_localizacion.setFont(font)
        self.cbx_localizacion.setObjectName("cbx_localizacion")
        self.cbx_localizacion.addItem("")
        self.btn_eliminar = QtWidgets.QPushButton(self.gb_datosDepartamento)
        self.btn_eliminar.setGeometry(QtCore.QRect(480, 230, 111, 31))
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
        self.btn_agregar = QtWidgets.QPushButton(self.gb_datosDepartamento)
        self.btn_agregar.setGeometry(QtCore.QRect(480, 110, 111, 31))
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
        self.btn_editar = QtWidgets.QPushButton(self.gb_datosDepartamento)
        self.btn_editar.setGeometry(QtCore.QRect(480, 170, 111, 31))
        self.btn_editar.setMinimumSize(QtCore.QSize(111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_editar.setFont(font)
        self.btn_editar.setStyleSheet("color: White;\n"
"background-color: rgb(12,91,166)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconosCrud/edit40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_editar.setIcon(icon2)
        self.btn_editar.setIconSize(QtCore.QSize(20, 20))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_limpiar = QtWidgets.QPushButton(self.gb_datosDepartamento)
        self.btn_limpiar.setGeometry(QtCore.QRect(480, 50, 111, 31))
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
        self.le_buscador = QtWidgets.QLineEdit(FrmDepartamentos)
        self.le_buscador.setGeometry(QtCore.QRect(20, 350, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_buscador.setFont(font)
        self.le_buscador.setObjectName("le_buscador")
        self.tv_departamento = QtWidgets.QTableView(FrmDepartamentos)
        self.tv_departamento.setGeometry(QtCore.QRect(20, 400, 631, 171))
        self.tv_departamento.setObjectName("tv_departamento")
        self.btn_buscar = QtWidgets.QPushButton(FrmDepartamentos)
        self.btn_buscar.setGeometry(QtCore.QRect(510, 350, 111, 31))
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

        self.retranslateUi(FrmDepartamentos)
        QtCore.QMetaObject.connectSlotsByName(FrmDepartamentos)
        FrmDepartamentos.setTabOrder(self.le_identificador, self.le_nombre)
        FrmDepartamentos.setTabOrder(self.le_nombre, self.cbx_localizacion)
        FrmDepartamentos.setTabOrder(self.cbx_localizacion, self.le_buscador)
        FrmDepartamentos.setTabOrder(self.le_buscador, self.tv_departamento)

    def retranslateUi(self, FrmDepartamentos):
        _translate = QtCore.QCoreApplication.translate
        FrmDepartamentos.setWindowTitle(_translate("FrmDepartamentos", "Gestión de departamentos"))
        self.gb_datosDepartamento.setTitle(_translate("FrmDepartamentos", "Datos del Departamento  "))
        self.lbl_identificador.setText(_translate("FrmDepartamentos", "Identificador:"))
        self.lbl_nombre.setText(_translate("FrmDepartamentos", "Nombre:"))
        self.lbl_localizacion.setText(_translate("FrmDepartamentos", "Localización:"))
        self.cbx_localizacion.setToolTip(_translate("FrmDepartamentos", "<html><head/><body><p>Select</p><p><br/></p></body></html>"))
        self.cbx_localizacion.setItemText(0, _translate("FrmDepartamentos", "-- Select --"))
        self.btn_eliminar.setToolTip(_translate("FrmDepartamentos", "<html><head/><body><p><a name=\"docs-internal-guid-bab997e6-7fff-9ebb-1345-25d89d2521de\"/><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">E</span><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">limina un registro</span></p></body></html>"))
        self.btn_eliminar.setText(_translate("FrmDepartamentos", "Eliminar"))
        self.btn_agregar.setToolTip(_translate("FrmDepartamentos", "<html><head/><body><p><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">Crea un registro</span></p></body></html>"))
        self.btn_agregar.setText(_translate("FrmDepartamentos", "Agregar"))
        self.btn_editar.setToolTip(_translate("FrmDepartamentos", "<html><head/><body><p><a name=\"docs-internal-guid-9f32f1a0-7fff-3aa2-c71f-d8139ac015ba\"/><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">E</span><span style=\" font-family:\'Arial\'; font-weight:400; color:#000000; background-color:transparent;\">dita un registro ya existente</span></p></body></html>"))
        self.btn_editar.setText(_translate("FrmDepartamentos", "Editar"))
        self.btn_limpiar.setToolTip(_translate("FrmDepartamentos", "<html><head/><body><p><span style=\" font-weight:400;\">Limpia los campos del formulario</span></p></body></html>"))
        self.btn_limpiar.setText(_translate("FrmDepartamentos", "Nuevo"))
        self.btn_buscar.setText(_translate("FrmDepartamentos", "Buscar"))
import iconosBotones_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDepartamentos = QtWidgets.QWidget()
    ui = Ui_FrmDepartamentos()
    ui.setupUi(FrmDepartamentos)
    FrmDepartamentos.show()
    sys.exit(app.exec_())