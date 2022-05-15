# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3dprinterprice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.total_cost = QtWidgets.QLCDNumber(self.centralwidget)
        self.total_cost.setGeometry(QtCore.QRect(830, 720, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.total_cost.setFont(font)
        self.total_cost.setObjectName("total_cost")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 750, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 340, 401, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 500, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 360, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 430, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 200, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.machine_type = QtWidgets.QComboBox(self.centralwidget)
        self.machine_type.setGeometry(QtCore.QRect(640, 360, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.machine_type.setFont(font)
        self.machine_type.setObjectName("machine_type")
        self.machine_type.addItem("")
        self.machine_type.addItem("")
        self.machine_type.addItem("")
        self.machine_type.addItem("")
        self.print_time = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.print_time.setGeometry(QtCore.QRect(640, 440, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.print_time.setFont(font)
        self.print_time.setObjectName("print_time")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(190, 380, 401, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(220, 450, 371, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(300, 520, 291, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(250, 80, 341, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(340, 150, 251, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(220, 220, 371, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.filament_cost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.filament_cost.setGeometry(QtCore.QRect(640, 510, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.filament_cost.setFont(font)
        self.filament_cost.setObjectName("filament_cost")
        self.labour_cost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.labour_cost.setGeometry(QtCore.QRect(640, 70, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.labour_cost.setFont(font)
        self.labour_cost.setObjectName("labour_cost")
        self.maint_cost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.maint_cost.setGeometry(QtCore.QRect(640, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.maint_cost.setFont(font)
        self.maint_cost.setObjectName("maint_cost")
        self.electric_cost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.electric_cost.setGeometry(QtCore.QRect(640, 210, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.electric_cost.setFont(font)
        self.electric_cost.setObjectName("electric_cost")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 740, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Final Total Cost"))
        self.label_3.setText(_translate("MainWindow", "Fixed Cost"))
        self.label_4.setText(_translate("MainWindow", "Labour Cost"))
        self.label_5.setText(_translate("MainWindow", "Maintenance Cost"))
        self.label_6.setText(_translate("MainWindow", "Machine Cost"))
        self.label_7.setText(_translate("MainWindow", "Filament Spend"))
        self.label_8.setText(_translate("MainWindow", "Machine"))
        self.label_9.setText(_translate("MainWindow", "Print Time"))
        self.label_10.setText(_translate("MainWindow", "Electricity"))
        self.machine_type.setItemText(0, _translate("MainWindow", "Ender 3"))
        self.machine_type.setItemText(1, _translate("MainWindow", "Ender 3 Pro"))
        self.machine_type.setItemText(2, _translate("MainWindow", "Ender CR 10"))
        self.machine_type.setItemText(3, _translate("MainWindow", "Qidi Max"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))

    def click(self):
        if self.machine_type.currentText() == "Ender 3":
            ma_pr = 1
        elif self.machine_type.currentText() == "Ender 3 Pro":
            ma_pr = 2
        elif self.machine_type.currentText() == "Ender CR 10":
            ma_pr = 2
        elif self.machine_type.currentText() == "Qidi Max":
            ma_pr = 2
        number = self.labour_cost.value() + self.maint_cost.value() + self.electric_cost.value() + self.print_time.value() + self.filament_cost.value() + ma_pr
        self.total_cost.display(number)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())