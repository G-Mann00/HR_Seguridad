from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.Frmlocalizacion import Ui_FrmLocalizacion
from datos.Dt_Location import Dt_Location
from entidades.Location import Location
from datos.Dt_Country import Dt_Country
from negocios.Ng_Location import Ng_Location
from entidades.VwLocations import VwLocations



class CtrlFrmLocation(QtWidgets.QMainWindow):
    dCountry = Dt_Country()
    dLocation = Dt_Location()
    modoEdicion = False
    loc = Location()
    ngLocation = Ng_Location()
    vista = VwLocations() #buscar una manera mas elegenta de hacer esto



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
        self.ui.tw_registroLocalizacion.clicked.connect(self.filaSeleccionada)
        self.ui.btn_editar.clicked.connect(self.btnEditar)
        self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        self.ui.le_buscar.textChanged.connect(self.le_buscarChanged)


    def btnLimpiarCampos(self):
        self.ui.le_identificador.setText("")
        self.ui.le_estado.setText("")
        self.ui.le_ciudad.setText("")
        self.ui.le_codigoPostal.setText("")
        self.ui.te_Direccion.setText("")
        self.ui.cmb_pais.setCurrentIndex(0)
        self.modoEdicion = False


    def cargarComboPais(self):
        listaPais = self.dCountry.listarPaises()
        self.ui.cmb_pais.clear()
        self.ui.cmb_pais.addItem("---Seleccione---")
        for p in listaPais:
            self.ui.cmb_pais.addItem(p.country_name, p.country_id)

    def cargarTabla(self):

        listaLocation = self.dLocation.listarLocations()

        self.ui.tw_registroLocalizacion.setRowCount(len(listaLocation))
        self.ui.tw_registroLocalizacion.setColumnCount(6)
        self.ui.tw_registroLocalizacion.verticalHeader().setVisible(False)
        row = 0
        for l in listaLocation:
            self.ui.tw_registroLocalizacion.setItem(row, 0, QtWidgets.QTableWidgetItem(str(l.location_id)))
            self.ui.tw_registroLocalizacion.setItem(row, 1, QtWidgets.QTableWidgetItem(l.country_name))
            self.ui.tw_registroLocalizacion.setItem(row, 2, QtWidgets.QTableWidgetItem(l.state_province))
            self.ui.tw_registroLocalizacion.setItem(row, 3, QtWidgets.QTableWidgetItem(l.city))
            self.ui.tw_registroLocalizacion.setItem(row, 4, QtWidgets.QTableWidgetItem(l.postal_code))
            self.ui.tw_registroLocalizacion.setItem(row, 5, QtWidgets.QTableWidgetItem(l.street_address))
            row += 1

    def filaSeleccionada(self):
        try:
            if len(self.ui.tw_registroLocalizacion.selectedItems()) >0:
                row = self.ui.tw_registroLocalizacion.currentRow()
                #Obtenemos los datos de la fila seleccionada
                self.loc.location_id = self.ui.tw_registroLocalizacion.item(row, 0).text()
                self.vista.country_name = self.ui.tw_registroLocalizacion.item(row, 1).text()
                self.loc.state_province = self.ui.tw_registroLocalizacion.item(row, 2).text()
                self.loc.city = self.ui.tw_registroLocalizacion.item(row, 3).text()
                self.loc.postal_code = self.ui.tw_registroLocalizacion.item(row, 4).text()
                self.loc.street_address = self.ui.tw_registroLocalizacion.item(row, 5).text()

                #Ponemos los textos en los Line Edit
                self.ui.le_identificador.setText(self.loc.location_id)
                self.ui.le_estado.setText(self.loc.state_province)
                self.ui.le_ciudad.setText(self.loc.city)
                self.ui.le_codigoPostal.setText(self.loc.postal_code)
                self.ui.te_Direccion.setText(self.loc.street_address)

                self.ui.cmb_pais.setCurrentText(self.vista.country_name)
                self.modoEdicion = True


        except Exception as e:
            print("Error en filaSeleccionada()", e)
            return False

    def btnAgregar(self):

        if self.modoEdicion:
            QMessageBox.warning(self, "Error", "No se puede agregar una localización en modo edición")
            return

        if self.ui.cmb_pais.currentIndex() == 0 or self.ui.le_ciudad.text() =="":
            QMessageBox.warning(self, "Error", "No se puede agregar una localización sin país o ciudad")
            return

        self.loc.street_address = self.ui.te_Direccion.toPlainText()
        self.loc.postal_code = self.ui.le_codigoPostal.text()
        self.loc.city = self.ui.le_ciudad.text()
        self.loc.state_province = self.ui.le_estado.text()
        self.loc.country_id = self.ui.cmb_pais.currentData()
        self.loc.location_id = self.ui.le_identificador.text()

        if not self.ngLocation.agregarLocation(self.loc):
            QMessageBox.warning(self, "Error", "No se pudo agregar la localización")
            return

        QMessageBox.information(self, "Éxito", "Se agregó la localización")
        self.btnLimpiarCampos()
        self.cargarTabla()

    def btnEditar(self):
        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "Debe seleccionar una localización para editar")
            return

        if self.vista.country_name == self.ui.cmb_pais.currentText() and self.loc.city == self.ui.le_ciudad.text() and self.loc.state_province == self.ui.le_estado.text() and self.loc.street_address == self.ui.te_Direccion.toPlainText() and self.loc.postal_code == self.ui.le_codigoPostal.text():
            QMessageBox.warning(self, "Error", "No se realizaron cambios en la localización")
            return

        if self.ui.cmb_pais.currentIndex() == 0 or self.ui.le_ciudad.text() =="":
            QMessageBox.warning(self, "Error", "No se puede agregar una localización sin país o ciudad")
            return

        self.loc.street_address = self.ui.te_Direccion.toPlainText()
        self.loc.postal_code = self.ui.le_codigoPostal.text()
        self.loc.city = self.ui.le_ciudad.text()
        self.loc.state_province = self.ui.le_estado.text()
        self.loc.country_id = self.ui.cmb_pais.currentData()
        self.loc.location_id = self.ui.le_identificador.text()

        if not self.ngLocation.actualizarLocalizacion(self.loc):
            QMessageBox.warning(self, "Error", "No se pudo editar la localización")
            return

        QMessageBox.information(self, "Éxito", "Se editó la localización")
        self.btnLimpiarCampos()
        self.cargarTabla()

    def btnEliminar(self):
        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "Debe seleccionar una localización para eliminar")
            return

        Alert = QMessageBox.warning(self, "Confirmar", f"¿Desea eliminar la localización?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if Alert == QMessageBox.No:
            return

        self.loc.location_id = self.ui.le_identificador.text()

        if not self.ngLocation.eliminarLocalizacion(self.loc):
            QMessageBox.warning(self, "Error", "No se pudo eliminar la localización")
            return

        QMessageBox.information(self, "Éxito", "Se eliminó la localización")
        self.btnLimpiarCampos()
        self.cargarTabla()

    def btnBuscar(self):

        if self.ui.le_buscar.text() == "":
            QMessageBox.warning(self, "Error", "Debe ingresar un valor para buscar")
            return

        if self.ui.cbx_filtro.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Debe seleccionar un filtro para buscar")
            return

        cadena = self.ui.le_buscar.text()
        if self.ui.cbx_filtro.currentIndex() == 1:
            listaLocation = self.dLocation.buscarPorPais(cadena)
        else:
            listaLocation = self.dLocation.buscarPorCiudad(cadena)

        self.ui.tw_registroLocalizacion.setRowCount(len(listaLocation))
        self.ui.tw_registroLocalizacion.setColumnCount(6)
        row = 0
        for l in listaLocation:
            self.ui.tw_registroLocalizacion.setItem(row, 0, QtWidgets.QTableWidgetItem(str(l.location_id)))
            self.ui.tw_registroLocalizacion.setItem(row, 1, QtWidgets.QTableWidgetItem(l.country_name))
            self.ui.tw_registroLocalizacion.setItem(row, 2, QtWidgets.QTableWidgetItem(l.state_province))
            self.ui.tw_registroLocalizacion.setItem(row, 3, QtWidgets.QTableWidgetItem(l.city))
            self.ui.tw_registroLocalizacion.setItem(row, 4, QtWidgets.QTableWidgetItem(l.postal_code))
            self.ui.tw_registroLocalizacion.setItem(row, 5, QtWidgets.QTableWidgetItem(l.street_address))
            row += 1

    def le_buscarChanged(self):
        if self.ui.le_buscar.text() == "":
            self.cargarTabla()





