# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frmlocalizacion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from recursos import iconosApp_rc


class Ui_FrmLocalizacion(object):
    def setupUi(self, FrmLocalizacion):
        FrmLocalizacion.setObjectName("FrmLocalizacion")
        FrmLocalizacion.resize(740, 776)
        FrmLocalizacion.setMinimumSize(QtCore.QSize(740, 776))
        self.gb_datosLocalizacion = QtWidgets.QGroupBox(FrmLocalizacion)
        self.gb_datosLocalizacion.setGeometry(QtCore.QRect(20, 20, 691, 481))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gb_datosLocalizacion.setFont(font)
        self.gb_datosLocalizacion.setObjectName("gb_datosLocalizacion")
        self.lb_identificador = QtWidgets.QLabel(self.gb_datosLocalizacion)
        self.lb_identificador.setGeometry(QtCore.QRect(30, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lb_identificador.setFont(font)
        self.lb_identificador.setObjectName("lb_identificador")
        self.lbl_pais = QtWidgets.QLabel(self.gb_datosLocalizacion)
        self.lbl_pais.setGeometry(QtCore.QRect(30, 120, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_pais.setFont(font)
        self.lbl_pais.setObjectName("lbl_pais")
        self.le_identificador = QtWidgets.QLineEdit(self.gb_datosLocalizacion)
        self.le_identificador.setGeometry(QtCore.QRect(30, 80, 161, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_identificador.setFont(font)
        self.le_identificador.setReadOnly(True)
        self.le_identificador.setObjectName("le_identificador")
        self.cmb_pais = QtWidgets.QComboBox(self.gb_datosLocalizacion)
        self.cmb_pais.setGeometry(QtCore.QRect(30, 140, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cmb_pais.setFont(font)
        self.cmb_pais.setObjectName("cmb_pais")
        self.cmb_pais.addItem("")
        self.le_estado = QtWidgets.QLineEdit(self.gb_datosLocalizacion)
        self.le_estado.setGeometry(QtCore.QRect(30, 200, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_estado.setFont(font)
        self.le_estado.setObjectName("le_estado")
        self.lbl_ciudad = QtWidgets.QLabel(self.gb_datosLocalizacion)
        self.lbl_ciudad.setGeometry(QtCore.QRect(30, 240, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_ciudad.setFont(font)
        self.lbl_ciudad.setObjectName("lbl_ciudad")
        self.le_ciudad = QtWidgets.QLineEdit(self.gb_datosLocalizacion)
        self.le_ciudad.setGeometry(QtCore.QRect(30, 260, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_ciudad.setFont(font)
        self.le_ciudad.setObjectName("le_ciudad")
        self.lbl_codigoPostal = QtWidgets.QLabel(self.gb_datosLocalizacion)
        self.lbl_codigoPostal.setGeometry(QtCore.QRect(30, 300, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_codigoPostal.setFont(font)
        self.lbl_codigoPostal.setObjectName("lbl_codigoPostal")
        self.le_codigoPostal = QtWidgets.QLineEdit(self.gb_datosLocalizacion)
        self.le_codigoPostal.setGeometry(QtCore.QRect(30, 320, 301, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.le_codigoPostal.setFont(font)
        self.le_codigoPostal.setObjectName("le_codigoPostal")
        self.lbl_direccion_2 = QtWidgets.QLabel(self.gb_datosLocalizacion)
        self.lbl_direccion_2.setGeometry(QtCore.QRect(30, 360, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_direccion_2.setFont(font)
        self.lbl_direccion_2.setObjectName("lbl_direccion_2")
        self.lbl_estado_2 = QtWidgets.QLabel(self.gb_datosLocalizacion)
        self.lbl_estado_2.setGeometry(QtCore.QRect(30, 180, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_estado_2.setFont(font)
        self.lbl_estado_2.setObjectName("lbl_estado_2")
        self.btn_agregar = QtWidgets.QPushButton(self.gb_datosLocalizacion)
        self.btn_agregar.setGeometry(QtCore.QRect(550, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setStyleSheet("color: White;\n"
"background-color:rgb(7,125,8)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconosCrud/add40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_agregar.setIcon(icon)
        self.btn_agregar.setIconSize(QtCore.QSize(20, 20))
        self.btn_agregar.setObjectName("btn_agregar")
        self.btn_eliminar = QtWidgets.QPushButton(self.gb_datosLocalizacion)
        self.btn_eliminar.setGeometry(QtCore.QRect(550, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_eliminar.setFont(font)
        self.btn_eliminar.setStyleSheet("color: White;\n"
"background-color: rgb(201,0,0)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconosCrud/delete40.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eliminar.setIcon(icon1)
        self.btn_eliminar.setIconSize(QtCore.QSize(20, 20))
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.btn_editar = QtWidgets.QPushButton(self.gb_datosLocalizacion)
        self.btn_editar.setGeometry(QtCore.QRect(550, 160, 111, 31))
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
        self.btn_limpiar = QtWidgets.QPushButton(self.gb_datosLocalizacion)
        self.btn_limpiar.setGeometry(QtCore.QRect(550, 40, 111, 31))
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
        self.textEdit = QtWidgets.QTextEdit(self.gb_datosLocalizacion)
        self.textEdit.setGeometry(QtCore.QRect(30, 380, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.lbl_filtro = QtWidgets.QLabel(FrmLocalizacion)
        self.lbl_filtro.setGeometry(QtCore.QRect(20, 535, 40, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_filtro.setFont(font)
        self.lbl_filtro.setObjectName("lbl_filtro")
        self.cbx_filtro = QtWidgets.QComboBox(FrmLocalizacion)
        self.cbx_filtro.setGeometry(QtCore.QRect(70, 530, 111, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbx_filtro.setFont(font)
        self.cbx_filtro.setObjectName("cbx_filtro")
        self.cbx_filtro.addItem("")
        self.le_buscar = QtWidgets.QLineEdit(FrmLocalizacion)
        self.le_buscar.setGeometry(QtCore.QRect(190, 530, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_buscar.setFont(font)
        self.le_buscar.setObjectName("le_buscar")
        self.btn_buscar = QtWidgets.QPushButton(FrmLocalizacion)
        self.btn_buscar.setGeometry(QtCore.QRect(570, 530, 111, 31))
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
        self.tw_registroLocalizacion = QtWidgets.QTableWidget(FrmLocalizacion)
        self.tw_registroLocalizacion.setGeometry(QtCore.QRect(20, 570, 691, 181))
        self.tw_registroLocalizacion.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tw_registroLocalizacion.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tw_registroLocalizacion.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_registroLocalizacion.setObjectName("tw_registroLocalizacion")
        self.tw_registroLocalizacion.setColumnCount(6)
        self.tw_registroLocalizacion.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroLocalizacion.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroLocalizacion.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroLocalizacion.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroLocalizacion.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroLocalizacion.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_registroLocalizacion.setHorizontalHeaderItem(5, item)
        self.tw_registroLocalizacion.horizontalHeader().setCascadingSectionResizes(False)
        self.tw_registroLocalizacion.horizontalHeader().setSortIndicatorShown(False)
        self.tw_registroLocalizacion.horizontalHeader().setStretchLastSection(True)
        self.tw_registroLocalizacion.verticalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(FrmLocalizacion)
        QtCore.QMetaObject.connectSlotsByName(FrmLocalizacion)
        FrmLocalizacion.setTabOrder(self.btn_limpiar, self.btn_agregar)
        FrmLocalizacion.setTabOrder(self.btn_agregar, self.btn_editar)
        FrmLocalizacion.setTabOrder(self.btn_editar, self.btn_eliminar)
        FrmLocalizacion.setTabOrder(self.btn_eliminar, self.le_identificador)
        FrmLocalizacion.setTabOrder(self.le_identificador, self.cmb_pais)
        FrmLocalizacion.setTabOrder(self.cmb_pais, self.le_estado)
        FrmLocalizacion.setTabOrder(self.le_estado, self.le_ciudad)
        FrmLocalizacion.setTabOrder(self.le_ciudad, self.le_codigoPostal)
        FrmLocalizacion.setTabOrder(self.le_codigoPostal, self.textEdit)
        FrmLocalizacion.setTabOrder(self.textEdit, self.cbx_filtro)
        FrmLocalizacion.setTabOrder(self.cbx_filtro, self.le_buscar)
        FrmLocalizacion.setTabOrder(self.le_buscar, self.btn_buscar)

    def retranslateUi(self, FrmLocalizacion):
        _translate = QtCore.QCoreApplication.translate
        FrmLocalizacion.setWindowTitle(_translate("FrmLocalizacion", "Gestión de localización"))
        self.gb_datosLocalizacion.setTitle(_translate("FrmLocalizacion", "Datos de Localización    "))
        self.lb_identificador.setText(_translate("FrmLocalizacion", "Identificador:"))
        self.lbl_pais.setText(_translate("FrmLocalizacion", "País:"))
        self.cmb_pais.setToolTip(_translate("FrmLocalizacion", "<html><head/><body><p>Select</p><p><br/></p></body></html>"))
        self.cmb_pais.setItemText(0, _translate("FrmLocalizacion", "-- Select --"))
        self.lbl_ciudad.setText(_translate("FrmLocalizacion", "Ciudad:"))
        self.lbl_codigoPostal.setText(_translate("FrmLocalizacion", "Codigo Postal:"))
        self.lbl_direccion_2.setText(_translate("FrmLocalizacion", "Dirección:"))
        self.lbl_estado_2.setText(_translate("FrmLocalizacion", "Estado:"))
        self.btn_agregar.setToolTip(_translate("FrmLocalizacion", "<html><head/><body><p><span style=\" font-weight:400;\">Crea un nuevo registro</span></p></body></html>"))
        self.btn_agregar.setText(_translate("FrmLocalizacion", "Agregar"))
        self.btn_eliminar.setToolTip(_translate("FrmLocalizacion", "<html><head/><body><p><span style=\" font-weight:400;\">Elimina un registro</span></p></body></html>"))
        self.btn_eliminar.setText(_translate("FrmLocalizacion", "Eliminar"))
        self.btn_editar.setToolTip(_translate("FrmLocalizacion", "<html><head/><body><p><span style=\" font-weight:400;\">Edita un registro ya existente</span></p></body></html>"))
        self.btn_editar.setText(_translate("FrmLocalizacion", "Editar"))
        self.btn_limpiar.setToolTip(_translate("FrmLocalizacion", "<html><head/><body><p><span style=\" font-weight:400;\">Limpia los campos del formulario</span></p></body></html>"))
        self.btn_limpiar.setText(_translate("FrmLocalizacion", "Nuevo"))
        self.lbl_filtro.setText(_translate("FrmLocalizacion", "Filtro"))
        self.cbx_filtro.setToolTip(_translate("FrmLocalizacion", "<html><head/><body><p>Select</p><p><br/></p></body></html>"))
        self.cbx_filtro.setItemText(0, _translate("FrmLocalizacion", "-- Select --"))
        self.btn_buscar.setText(_translate("FrmLocalizacion", "Buscar"))
        item = self.tw_registroLocalizacion.horizontalHeaderItem(0)
        item.setText(_translate("FrmLocalizacion", "ID"))
        item = self.tw_registroLocalizacion.horizontalHeaderItem(1)
        item.setText(_translate("FrmLocalizacion", "País"))
        item = self.tw_registroLocalizacion.horizontalHeaderItem(2)
        item.setText(_translate("FrmLocalizacion", "Estado"))
        item = self.tw_registroLocalizacion.horizontalHeaderItem(3)
        item.setText(_translate("FrmLocalizacion", "Ciudad"))
        item = self.tw_registroLocalizacion.horizontalHeaderItem(4)
        item.setText(_translate("FrmLocalizacion", "Codigo Postal"))
        item = self.tw_registroLocalizacion.horizontalHeaderItem(5)
        item.setText(_translate("FrmLocalizacion", "Dirección"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLocalizacion = QtWidgets.QWidget()
    ui = Ui_FrmLocalizacion()
    ui.setupUi(FrmLocalizacion)
    FrmLocalizacion.show()
    sys.exit(app.exec_())