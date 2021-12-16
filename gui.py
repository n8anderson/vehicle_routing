import sys
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QDialog, QVBoxLayout
import get_routes


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: gray;")

        self.standard_vrp_button = QPushButton(self)
        self.limited_vrp_button = QPushButton(self)
        self.shortest_vrp_button = QPushButton(self)
        self.standard_label = QLabel(self)
        self.standard_label.setText("Touching every node, with shortest distance and back to depot.")

        self.limited_label = QLabel(self)
        self.limited_label.setText("Highest Value for Max 3 Stops.")

        self.shortest_label = QLabel(self)
        self.shortest_label.setText("Shortest Distance with no defined route.")

        self.pixmap = QPixmap('start.png')

        self.pix_label = QLabel(self)
        self.pix_label.setPixmap(self.pixmap)

        self.pix_label.resize(self.pixmap.width(), self.pixmap.height())

        self.pix_label.move(650, 50)

        self.pixmap2 = QPixmap('start2.png')

        self.pix_label2 = QLabel(self)
        self.pix_label2.setPixmap(self.pixmap2)

        self.pix_label2.resize(self.pixmap2.width(), self.pixmap2.height())

        self.pix_label2.move(50, 450)

        self.setup()

    def setup(self):
        self.setWindowTitle("Vehicle Routing Problem Solutions")
        self.setGeometry(768, 462, 1200, 900)

        self.standard_vrp_button.resize(200, 40)
        self.standard_vrp_button.move(50, 100)
        self.standard_vrp_button.setText("Standard Solution")
        self.standard_vrp_button.clicked.connect(self.to_standard)

        self.standard_label.resize(600, 40)
        self.standard_label.move(50, 150)

        self.limited_vrp_button.resize(200, 40)
        self.limited_vrp_button.move(50, 200)
        self.limited_vrp_button.setText("Limited Solution")
        self.limited_vrp_button.clicked.connect(self.to_limited)

        self.limited_label.resize(600, 40)
        self.limited_label.move(50, 250)

        self.shortest_vrp_button.resize(200, 40)
        self.shortest_vrp_button.move(50, 300)
        self.shortest_vrp_button.setText("Shortest Solution")
        self.shortest_vrp_button.clicked.connect(self.to_shortest)

        self.shortest_label.resize(600, 40)
        self.shortest_label.move(50, 350)

        self.show()

    def to_shortest(self):
        self.cams = ShortestWindow()
        self.cams.show()
        self.close()

    def to_limited(self):
        self.cams = LimitedWindow()
        self.cams.show()
        self.close()

    def to_standard(self):
        self.cams = StandardWindow()
        self.cams.show()
        self.close()

class LimitedWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: gray;")
        self.title = "Limited Stop VRP"
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
        self.setGeometry(768, 462, 1200, 900)

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
        get_routes.limited_stops(self)

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

class ShortestWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: gray;")
        self.title = "Shortest VRP"
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
        self.setGeometry(768, 462, 1200, 900)

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
        get_routes.short_route(self)

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

class StandardWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: gray;")
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
        self.setGeometry(768, 462, 1200, 900)

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
