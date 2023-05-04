# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmPais.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from recursos import iconosBotones_rc


class Ui_FrmPais(object):
    def setupUi(self, FrmPais):
        FrmPais.setObjectName("FrmPais")
        FrmPais.resize(677, 613)
        FrmPais.setMinimumSize(QtCore.QSize(677, 613))
        self.gb_datosPais = QtWidgets.QGroupBox(FrmPais)
        self.gb_datosPais.setGeometry(QtCore.QRect(20, 20, 631, 311))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gb_datosPais.setFont(font)
        self.gb_datosPais.setObjectName("gb_datosPais")
        self.lbl_identificador = QtWidgets.QLabel(self.gb_datosPais)
        self.lbl_identificador.setGeometry(QtCore.QRect(30, 50, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_identificador.setFont(font)
        self.lbl_identificador.setObjectName("lbl_identificador")
        self.lbl_nombre = QtWidgets.QLabel(self.gb_datosPais)
        self.lbl_nombre.setGeometry(QtCore.QRect(30, 130, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_nombre.setFont(font)
        self.lbl_nombre.setObjectName("lbl_nombre")
        self.lbl_region = QtWidgets.QLabel(self.gb_datosPais)
        self.lbl_region.setGeometry(QtCore.QRect(30, 210, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_region.setFont(font)
        self.lbl_region.setObjectName("lbl_region")
        self.le_identificador = QtWidgets.QLineEdit(self.gb_datosPais)
        self.le_identificador.setGeometry(QtCore.QRect(30, 80, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.le_identificador.setFont(font)
        self.le_identificador.setReadOnly(True)
        self.le_identificador.setObjectName("le_identificador")
        self.le_nombre = QtWidgets.QLineEdit(self.gb_datosPais)
        self.le_nombre.setGeometry(QtCore.QRect(30, 160, 361, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.le_nombre.setFont(font)
        self.le_nombre.setObjectName("le_nombre")
        self.cmb_region = QtWidgets.QComboBox(self.gb_datosPais)
        self.cmb_region.setGeometry(QtCore.QRect(30, 250, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cmb_region.setFont(font)
        self.cmb_region.setObjectName("cmb_region")
        self.cmb_region.addItem("")
        self.btn_limpiar = QtWidgets.QPushButton(self.gb_datosPais)
        self.btn_limpiar.setGeometry(QtCore.QRect(490, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_limpiar.setFont(font)
        self.btn_limpiar.setStyleSheet("color: Black;\n"
"background-color:white\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconosCrud/clean40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_limpiar.setIcon(icon)
        self.btn_limpiar.setIconSize(QtCore.QSize(20, 20))
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.btn_agregar = QtWidgets.QPushButton(self.gb_datosPais)
        self.btn_agregar.setGeometry(QtCore.QRect(490, 110, 111, 31))
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
        self.btn_editar = QtWidgets.QPushButton(self.gb_datosPais)
        self.btn_editar.setGeometry(QtCore.QRect(490, 170, 111, 31))
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
        self.btn_eliminar = QtWidgets.QPushButton(self.gb_datosPais)
        self.btn_eliminar.setGeometry(QtCore.QRect(490, 230, 111, 31))
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
        self.le_buscar = QtWidgets.QLineEdit(FrmPais)
        self.le_buscar.setGeometry(QtCore.QRect(20, 360, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_buscar.setFont(font)
        self.le_buscar.setObjectName("le_buscar")
        self.btn_buscar = QtWidgets.QPushButton(FrmPais)
        self.btn_buscar.setGeometry(QtCore.QRect(510, 360, 111, 31))
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
        self.tbv_registroPais = QtWidgets.QTableView(FrmPais)
        self.tbv_registroPais.setGeometry(QtCore.QRect(20, 410, 631, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tbv_registroPais.setFont(font)
        self.tbv_registroPais.setObjectName("tbv_registroPais")

        self.retranslateUi(FrmPais)
        QtCore.QMetaObject.connectSlotsByName(FrmPais)
        FrmPais.setTabOrder(self.btn_limpiar, self.btn_agregar)
        FrmPais.setTabOrder(self.btn_agregar, self.btn_editar)
        FrmPais.setTabOrder(self.btn_editar, self.btn_eliminar)
        FrmPais.setTabOrder(self.btn_eliminar, self.le_identificador)
        FrmPais.setTabOrder(self.le_identificador, self.le_nombre)
        FrmPais.setTabOrder(self.le_nombre, self.cmb_region)
        FrmPais.setTabOrder(self.cmb_region, self.le_buscar)
        FrmPais.setTabOrder(self.le_buscar, self.btn_buscar)
        FrmPais.setTabOrder(self.btn_buscar, self.tbv_registroPais)

    def retranslateUi(self, FrmPais):
        _translate = QtCore.QCoreApplication.translate
        FrmPais.setWindowTitle(_translate("FrmPais", "Gestión de pais"))
        self.gb_datosPais.setTitle(_translate("FrmPais", "Datos del País  "))
        self.lbl_identificador.setText(_translate("FrmPais", "Identificador:"))
        self.lbl_nombre.setText(_translate("FrmPais", "Nombre:"))
        self.lbl_region.setText(_translate("FrmPais", "Región:"))
        self.cmb_region.setToolTip(_translate("FrmPais", "<html><head/><body><p>Select</p><p><br/></p></body></html>"))
        self.cmb_region.setItemText(0, _translate("FrmPais", "-- Select --"))
        self.btn_limpiar.setToolTip(_translate("FrmPais", "<html><head/><body><p><span style=\" font-weight:400;\">Limpia los campos del formulario</span></p></body></html>"))
        self.btn_limpiar.setText(_translate("FrmPais", "Nuevo"))
        self.btn_agregar.setToolTip(_translate("FrmPais", "<html><head/><body><p><span style=\" font-weight:400;\">Crea un nuevo registro</span></p></body></html>"))
        self.btn_agregar.setText(_translate("FrmPais", "Agregar"))
        self.btn_editar.setToolTip(_translate("FrmPais", "<html><head/><body><p><span style=\" font-weight:400;\">Edita un registro ya existente</span></p></body></html>"))
        self.btn_editar.setText(_translate("FrmPais", "Editar"))
        self.btn_eliminar.setToolTip(_translate("FrmPais", "<html><head/><body><p><span style=\" font-weight:400;\">Elimina un registro</span></p></body></html>"))
        self.btn_eliminar.setText(_translate("FrmPais", "Eliminar"))
        self.btn_buscar.setText(_translate("FrmPais", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPais = QtWidgets.QWidget()
    ui = Ui_FrmPais()
    ui.setupUi(FrmPais)
    FrmPais.show()
    sys.exit(app.exec_())
