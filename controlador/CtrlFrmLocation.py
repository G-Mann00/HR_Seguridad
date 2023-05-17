from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.Frmlocalizacion import Ui_FrmLocalizacion
from datos.Dt_Location import Dt_Location
from entidades.Location import Location
from datos.Dt_Country import Dt_Country


class CtrlFrmLocation(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmLocalizacion()
        self.ui.setupUi(self)
        self.initControlGui()
        self.cargarComboPais()
        self.cargarTabla()

    def initControlGui(self):
        self.ui.btn_limpiar.clicked.connect(self.btnLimpiarCampos)
        self.ui.btn_agregar.clicked.connect(self.btnAgregar)
        pass

    def btnLimpiarCampos(self):
        self.ui.le_identificador.setText("")
        self.ui.le_estado.setText("")
        self.ui.le_ciudad.setText("")
        self.ui.le_codigoPostal.setText("")
        self.ui.te_Direccion.setText("")
        self.ui.cmb_pais.setCurrentIndex(0)


    def cargarComboPais(self):
        dCountry = Dt_Country()
        listaPais = dCountry.listarPaises()
        if listaPais == None:
            return

        for p in listaPais:
            self.ui.cmb_pais.addItem(p.country_name, p.country_id)

    def cargarTabla(self):
        dLocation = Dt_Location()
        listaLocation = dLocation.listarLocations()
        if listaLocation == None:
            return

        self.ui.tw_registroLocalizacion.setRowCount(len(listaLocation))
        self.ui.tw_registroLocalizacion.setColumnCount(6)
        self.ui.tw_registroLocalizacion.verticalHeader().setVisible(False)
        row = 0
        for l in listaLocation:
            self.ui.tw_registroLocalizacion.setItem(row, 0, QtWidgets.QTableWidgetItem(str(l.location_id)))
            self.ui.tw_registroLocalizacion.setItem(row, 1, QtWidgets.QTableWidgetItem(l.country_id))
            self.ui.tw_registroLocalizacion.setItem(row, 2, QtWidgets.QTableWidgetItem(l.state_province))
            self.ui.tw_registroLocalizacion.setItem(row, 3, QtWidgets.QTableWidgetItem(l.city))
            self.ui.tw_registroLocalizacion.setItem(row, 4, QtWidgets.QTableWidgetItem(l.postal_code))
            self.ui.tw_registroLocalizacion.setItem(row, 5, QtWidgets.QTableWidgetItem(l.street_address))
            row += 1

    def btnAgregar(self):
        if self.ui.le_estado.text() == "" or self.ui.le_ciudad.text() == "" or self.ui.le_estado.text() == "" or self.ui.cmb_pais.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        dLocation = Dt_Location()
        l = Location()
        l.street_address = self.ui.te_Direccion.toPlainText()
        l.postal_code = self.ui.le_codigoPostal.text()
        l.city = self.ui.le_ciudad.text()
        l.state_province = self.ui.le_estado.text()
        l.country_id = self.ui.cmb_pais.currentData()
        l.location_id = self.ui.le_identificador.text()

        if not dLocation.agregarLocation(l):
            QMessageBox.warning(self, "Error", "No se pudo agregar la localización")
            return

        QMessageBox.information(self, "Éxito", "Se agregó la localización")
        self.btnLimpiarCampos()
        self.cargarTabla()






