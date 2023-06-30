import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit

# Create a class for the main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Set the window title and size
        self.setWindowTitle("Simple PyQt Function")
        self.resize(300, 200)
        # Create some labels and inputs
        self.label1 = QLabel("Name:", self)
        self.label1.move(50, 50)
        self.input1 = QLineEdit(self)
        self.input1.move(100, 50)
        self.label2 = QLabel("Age:", self)
        self.label2.move(50, 100)
        self.input2 = QLineEdit(self)
        self.input2.move(100, 100)


if __name__=='__main__':
    # Create an application object
    app = QApplication(sys.argv)
    # Create a main window object
    window = MainWindow()
    # Show the window
    window.show()
    print('hah')
    # time.sleep(2)
    # window.hide()
    # Run the application loop
    sys.exit(app.exec_())