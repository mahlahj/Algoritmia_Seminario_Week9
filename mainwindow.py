from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from ui_MainWindow import Ui_MainWindow
from particula import Particula
from organizador import Organizador
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.particula = Particula()
        self.organizador = Organizador()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.abInicio.clicked.connect(self.click_agregar_inicio)
        self.ui.abFinal.clicked.connect(self.click_agregar_final)
        self.ui.abMostrar.clicked.connect(self.click_mostrar)
        self.ui.actionGuardar_.triggered.connect(self.guardar)
        self.ui.actionAbrir_.triggered.connect(self.abrir)
        self.ui.abMostrarParticulas.clicked.connect(self.mostrarParticulasTodas)
        self.ui.abBuscar.clicked.connect(self.buscarParticulaId)
        self.ui.abLimpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)


    @Slot()
    def click_mostrar(self):
        if (not self.ui.rBId.isChecked() and not self.ui.rBDistancia.isChecked() and not self.ui.rBVelocidad.isChecked()):
            QMessageBox.about(self, "Advertencia",  "Seleccione alguna de las siguientes opciones.")
        self.click_mostrar_grafico()
        lista = []
        if (self.ui.rBId.isChecked()):
            lista = sorted(self.organizador.organizador, key=lambda particula: particula.Id, reverse=False)
        elif (self.ui.rBDistancia.isChecked()):
            lista = sorted(self.organizador.organizador, key=lambda particula: particula.distancia, reverse=True)
        elif (self.ui.rBVelocidad.isChecked()):
            lista = sorted(self.organizador.organizador, key=lambda particula: particula.velocidad, reverse=False)
        self.click_mostrar_ordenacion(lista)

    @Slot()
    def click_mostrar_grafico(self):
        pen = QPen()
        pen.setWidth(2)

        for item in self.organizador.organizador:
            pen.setColor(item.color())

            origen_x = item.Xi()
            origen_y = item.Yi()
            destino_x = item.Xf()
            destino_y = item.Yf()

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)
            self.scene.addLine(origen_x+3, origen_y+3, destino_x, destino_y, pen)

    @Slot()
    def click_mostrar_ordenacion(self, lista):
        cadenas = ""
        self.ui.plainTextEdit.clear()
        for particula in lista:
            cadenas += str(particula) + "\n"
        self.ui.plainTextEdit.insertPlainText(cadenas)
    
    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id.value()
        origen_x = self.ui.origenX.value()
        origen_y = self.ui.origenY.value()
        destino_x = self.ui.destinoX.value()
        destino_y = self.ui.destinoY.value()
        velocidad = self.ui.velocidad.value()
        rojo = self.ui.rojo.value()
        verde = self.ui.verde.value()
        azul = self.ui.azul.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.organizador.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        id = self.ui.id.value()
        origen_x = self.ui.origenX.value()
        origen_y = self.ui.origenY.value()
        destino_x = self.ui.destinoX.value()
        destino_y = self.ui.destinoY.value()
        velocidad = self.ui.velocidad.value()
        rojo = self.ui.rojo.value()
        verde = self.ui.verde.value()
        azul = self.ui.azul.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, rojo, verde, azul)
        self.organizador.agregar_final(particula)

    @Slot()
    def guardar(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar', '.', 'JSON (*.json)')
        with open(ubicacion[0], 'w') as archivo:
            json.dump(self.organizador.guardar(), archivo, indent=4)

    @Slot()
    def abrir(self):
        ubicacion = QFileDialog.getOpenFileName(self, 'Abrir', '.', 'JSON (*.json)')
        with open(ubicacion[0], 'r') as archivo:
            self.organizador.get(json.load(archivo))

    @Slot()
    def buscarParticulaId(self):
        id = self.ui.lineaBuscar.text()
        encontrado = False
        for item in self.organizador.organizador:
            if id == item.getId():
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(1)
                headers = ["Id", "Origen", "Destino", "Velocidad", "Color", "Distancia"]
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)

                id = QTableWidgetItem(item.getId())
                origen = QTableWidgetItem(item.getOrigen())
                destino = QTableWidgetItem(item.getDestino())
                velocidad = QTableWidgetItem(item.getVelocidad())
                color = QTableWidgetItem(item.getColor())
                distancia = QTableWidgetItem(item.getDistancia())

                self.ui.tableWidget.setItem(0, 0, id)
                self.ui.tableWidget.setItem(0, 1, origen)
                self.ui.tableWidget.setItem(0, 2, destino)
                self.ui.tableWidget.setItem(0, 3, velocidad)
                self.ui.tableWidget.setItem(0, 4, color)
                self.ui.tableWidget.setItem(0, 5, distancia)

                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La partícula con identificador "{id}" no fue encontrada'
            )

    @Slot()
    def mostrarParticulasTodas(self):
        row = 0
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(len(self.organizador.organizador))
        headers = ["Id", "Origen", "Destino", "Velocidad", "Color", "Distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        for item in self.organizador.organizador:
            id = QTableWidgetItem(item.getId())
            origen = QTableWidgetItem(item.getOrigen())
            destino = QTableWidgetItem(item.getDestino())
            velocidad = QTableWidgetItem(item.getVelocidad())
            color = QTableWidgetItem(item.getColor())
            distancia = QTableWidgetItem(item.getDistancia())

            self.ui.tableWidget.setItem(row, 0, id)
            self.ui.tableWidget.setItem(row, 1, origen)
            self.ui.tableWidget.setItem(row, 2, destino)
            self.ui.tableWidget.setItem(row, 3, velocidad)
            self.ui.tableWidget.setItem(row, 4, color)
            self.ui.tableWidget.setItem(row, 5, distancia)

            row += 1

    @Slot()
    def limpiar(self):
        self.scene.clear()
        self.ui.plainTextEdit.clear()