import sys
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QDialog, QVBoxLayout
import get_routes


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.standard_vrp_button = QPushButton(self)
        self.standard_label = QLabel(self)
        self.standard_label.setText("Touching every node, with shortest distance and back to depot.")

        self.setup()

    def setup(self):
        self.setWindowTitle("Vehicle Routing Problem Solutions")
        self.setGeometry(50, 50, 960, 960)

        self.standard_vrp_button.resize(200, 40)
        self.standard_vrp_button.move(50, 100)
        self.standard_vrp_button.setText("Standard Solution")
        self.standard_vrp_button.clicked.connect(self.to_standard)

        self.standard_label.resize(600, 40)
        self.standard_label.move(50, 150)

        self.show()

    @pyqtSlot()
    def to_standard(self):
        self.statusBar().showMessage("Switched to window 1")
        self.cams = StandardWindow()
        self.cams.show()
        self.close()


class StandardWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.width = 960
        self.height = 960
        self.title = "Standard VRP"
        self.next_button = QPushButton(self)
        self.back_button = QPushButton(self)
        self.start_button = QPushButton(self)
        self.pressed = False
        self.route_display = QLabel()
        self.route_display.setFont(QFont('Arial', 18))
        self.totals_display = QLabel()
        self.totals_display.setFont(QFont('Arial', 16))
        self.display = QLabel()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.route_display, stretch=True)
        self.vbox.addWidget(self.display, stretch=True)
        self.vbox.addWidget(self.totals_display, stretch=True)
        self.vbox.addWidget(self.next_button, stretch=True)
        self.vbox.addWidget(self.start_button, stretch=True)
        self.vbox.addWidget(self.back_button, stretch=True)
        self.setLayout(self.vbox)
        self.print_text = f""

        self.setup()

    def setup(self):
        self.setWindowTitle(self.title)
        self.setGeometry(50, 50, self.width, self.height)

        self.back_button.resize(150, 40)
        self.back_button.move(50, 860)
        self.back_button.setText("Back to Main")
        self.back_button.clicked.connect(self.back_to_main)

        self.start_button.resize(150, 40)
        self.start_button.move(50, 760)
        self.start_button.setText("Start")
        self.start_button.clicked.connect(self.start_vrp)

        self.next_button.resize(150, 40)
        self.next_button.move(250, 760)
        self.next_button.setText("Next Step")
        self.next_button.clicked.connect(self.handleStop)
        self.show()

    def start_vrp(self):
        get_routes.run_vehicle(self)

    def handleStart(self):
        try:
            self.start_button.setDisabled(True)
            self._running = True
            while self._running:
                QtGui.QGuiApplication.processEvents()
                time.sleep(0.05)
            self.start_button.setDisabled(False)
        except Exception as e:
            print(Exception, e)

    def handleStop(self):
        self._running = False

    def back_to_main(self):
        try:
            self.cams = MainWindow()
            self.cams.show()
            self.close()
        except Exception as e:
            print(Exception, e)


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
