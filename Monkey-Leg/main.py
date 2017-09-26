import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

from widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent, Qt.Window)
        self.setupUi(self)

app = QApplication(sys.argv)

widget = Widget()
widget.show()

sys.exit(app.exec_())