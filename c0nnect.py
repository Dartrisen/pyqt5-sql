import sys
import sqlite3
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QTableView, QAbstractItemView

class C0nnect0r(object):
    """
        sql database class connector
    """
    def __init__(self, name = None):
        if (name == None):
            self.name = ":memory:"
        else:
            self.name = name
        self.makeC0nnect()

    def makeC0nnect(self):
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()

    def clean(self):
        self.conn.close()

    def execute(self, statement):
        try:
            self.cursor.execute(statement)
            result = self.cursor.fetchall()
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        else:
            self.conn.commit()

class App(QWidget):
    """
        creates a qt window
    """
    def __init__(self):
        super().__init__()
        self.title = 'DB Connector'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 400
        self.table = QTableView()
        self.table.setGeometry(0, 0, 400, 200)
        self.model = QStandardItemModel(self)
        self.table.setModel(self.model)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.connection = QLineEdit(self)
        self.connection.move(20, 20)
        self.connection.resize(280, 25)

        self.statement = QLineEdit(self)
        self.statement.move(20, 50)
        self.statement.resize(280, 25)

        self.button = QPushButton('execute', self)
        self.button.move(20, 80)
 
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        name = self.connection.text()
        c0nn = C0nnect0r(name)
        statement = self.statement.text()
        c0nn.execute(statement)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())