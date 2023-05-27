from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QApplication
from vistas.FrmPais import Ui_FrmPais
from datos.Dt_Country import Dt_Country
from datos.Dt_Region import Dt_Region
from entidades.Country import Country
from negocios.Ng_Country import Ng_Country


class CtrlFrmPais(QtWidgets.QMainWindow):
    dCountry = Dt_Country()
    country = Country()
    ngCountry = Ng_Country()
    dRegion = Dt_Region()
    modoEdicion = False #si es true, se está editando un registro o se va a borrar un registro

    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmPais()
        self.ui.setupUi(self)
        self.initControlGui()


    def initControlGui(self):
        self.ui.btn_agregar.clicked.connect(self.btnAgregar)
        self.ui.tw_registroPais.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btn_limpiar.clicked.connect(self.limpiarDatos)
        self.ui.tw_registroPais.clicked.connect(self.filaSeleccionada)
        QApplication.instance().focusChanged.connect(self.validarIdentificador)
        self.ui.btn_editar.clicked.connect(self.btnEditar)
        self.ui.btn_eliminar.clicked.connect(self.btnEliminar)
        self.ui.btn_buscar.clicked.connect(self.btnBuscar)
        self.ui.le_buscar.textChanged.connect(self.refresh)

        self.cargarDatosTabla()
        self.cargarDatosCombobox()



    def refresh(self):
        if self.ui.le_buscar.text() == "":
            self.cargarDatosTabla()

    def validarIdentificador(self, old_widget, now_widget):

        if self.ui.le_identificador is old_widget:

            if len(self.ui.le_identificador.text()) > 2:
                QMessageBox.warning(self, "Alerta", "El identificador no puede tener más de 2 caracteres")
                #self.ui.le_identificador.setFocus()
                return


    def filaSeleccionada(self):
        if len(self.ui.tw_registroPais.selectedItems()) > 0:
            row = self.ui.tw_registroPais.selectedItems()[0].row()
            self.ui.le_identificador.setText(self.ui.tw_registroPais.item(row, 0).text())
            self.ui.le_nombre.setText(self.ui.tw_registroPais.item(row, 1).text())
            self.ui.cmb_region.setCurrentText(self.ui.tw_registroPais.item(row, 2).text())

        self.ui.le_identificador.setEnabled(False)
        self.country.country_name = self.ui.le_nombre.text() # Nos va permitir verificar si cambio el nombre del pais
        self.country.region_id = self.ui.cmb_region.currentData() # Nos va permitir verificar si cambio la region del pais
        self.modoEdicion = True




    def cargarDatosCombobox(self):
        self.listaRegion = self.dRegion.listarRegion()
        self.ui.cmb_region.clear()
        self.ui.cmb_region.addItem("---Seleccione---")
        for r in self.listaRegion:
            self.ui.cmb_region.addItem(r.region_name, r.region_id)

    def cargarDatosTabla(self):
        listaPaises = self.dCountry.listarPaises()

        self.ui.tw_registroPais.setRowCount(len(listaPaises))
        self.ui.tw_registroPais.setColumnCount(3)
        self.ui.tw_registroPais.verticalHeader().setVisible(False)
        row = 0
        for r in listaPaises:
            self.ui.tw_registroPais.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.country_id)))
            self.ui.tw_registroPais.setItem(row, 1, QtWidgets.QTableWidgetItem(r.country_name))
            self.ui.tw_registroPais.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r.region_name)))
            row += 1

    def limpiarDatos(self):
        self.ui.le_identificador.setText("")
        self.ui.le_nombre.setText("")
        self.ui.cmb_region.setCurrentIndex(0)
        self.ui.le_identificador.setEnabled(True)
        self.modoEdicion = False



    def btnAgregar(self):

        if self.modoEdicion:
            QMessageBox.warning(self, "Error", "Te encuentras en modo edición")
            return


        if self.ui.le_nombre.text() == "" or self.ui.cmb_region.currentIndex() == 0 or self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        if len(self.ui.le_identificador.text()) > 2:
            QMessageBox.warning(self, "Error", "El identificador no puede tener más de 2 caracteres")
            return

        self.country.country_id = self.ui.le_identificador.text().strip().upper()
        self.country.country_name = self.ui.le_nombre.text().strip()
        self.country.region_id = self.ui.cmb_region.currentData()

        resultado =self.ngCountry.insertarPais(self.country)
        match resultado:
            case -1:
                QMessageBox.warning(self, "Error", "No se ha podido agregar el país", QMessageBox.Ok)
            case 1:
                QMessageBox.information(self, "Éxito", "Se ha agregado el país correctamente", QMessageBox.Ok)
                self.limpiarDatos()
                self.cargarDatosTabla()
            case 2:
                QMessageBox.warning(self, "Error", "El identificador ya existe", QMessageBox.Ok)
            case 3:
                QMessageBox.warning(self, "Error", "El pais ya existe", QMessageBox.Ok)


    def btnEditar(self):

        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "No se ha seleccionado un registro")
            return


        if self.ui.le_nombre.text() == "" or self.ui.cmb_region.currentIndex() == 0 or self.ui.le_identificador.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese todos los datos")
            return

        if self.country.country_name == self.ui.le_nombre.text() and self.country.region_id == self.ui.cmb_region.currentData():
            QMessageBox.warning(self, "Alerta", "No se han realizado modificaciones en los datos del registro.")
            return

        self.country.country_id = self.ui.le_identificador.text()
        self.country.country_name = self.ui.le_nombre.text()
        self.country.region_id = self.ui.cmb_region.currentData()

        if not self.ngCountry.actualizarPais(self.country):
            QMessageBox.warning(self, "Error", "No se pudo editar el registro")
            return

        QMessageBox.information(self, "Éxito", "Se editó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()

    def btnEliminar(self):
        if not self.modoEdicion:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún registro")
            return

        self.country.country_id = self.ui.le_identificador.text()
        self.country.country_name = self.ui.le_nombre.text()

        alert = QMessageBox.warning(self, 'Alerta', f"¿Está seguro de eliminar el pais {self.country.country_name}?", QMessageBox.Yes | QMessageBox.No)
        if alert == QMessageBox.No:
            return

        if not self.ngCountry.eliminarPais(self.country):
            QMessageBox.warning(self, "Error", "No se pudo eliminar el registro")
            return
        QMessageBox.information(self, "Éxito", "Se eliminó el registro")
        self.cargarDatosTabla()
        self.limpiarDatos()

    def btnBuscar(self):
        if self.ui.le_buscar.text() == "":
            QMessageBox.warning(self, "Error", "Ingrese el nombre del país")
            return

        self.country.country_name = self.ui.le_buscar.text()
        listaPaises = self.dCountry.buscarPais(self.country)

        self.ui.tw_registroPais.setRowCount(len(listaPaises))
        self.ui.tw_registroPais.setColumnCount(3)
        self.ui.tw_registroPais.verticalHeader().setVisible(False)
        row = 0
        for r in listaPaises:
            self.ui.tw_registroPais.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r.country_id)))
            self.ui.tw_registroPais.setItem(row, 1, QtWidgets.QTableWidgetItem(r.country_name))
            self.ui.tw_registroPais.setItem(row, 2, QtWidgets.QTableWidgetItem(str(r.region_name)))
            row += 1