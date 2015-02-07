# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\devel\github\flightlinks\mainform.ui'
#
# Created: Sat Feb  7 19:08:25 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 538)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rb_momondocom = QtWidgets.QRadioButton(self.groupBox)
        self.rb_momondocom.setObjectName("rb_momondocom")
        self.gridLayout_3.addWidget(self.rb_momondocom, 3, 0, 1, 1)
        self.rb_pelikansk = QtWidgets.QRadioButton(self.groupBox)
        self.rb_pelikansk.setChecked(True)
        self.rb_pelikansk.setObjectName("rb_pelikansk")
        self.gridLayout_3.addWidget(self.rb_pelikansk, 0, 0, 1, 1)
        self.rb_kayakcom = QtWidgets.QRadioButton(self.groupBox)
        self.rb_kayakcom.setObjectName("rb_kayakcom")
        self.gridLayout_3.addWidget(self.rb_kayakcom, 1, 0, 1, 1)
        self.rb_tripadvisorcom = QtWidgets.QRadioButton(self.groupBox)
        self.rb_tripadvisorcom.setObjectName("rb_tripadvisorcom")
        self.gridLayout_3.addWidget(self.rb_tripadvisorcom, 2, 0, 1, 1)
        self.rb_skyscannercom = QtWidgets.QRadioButton(self.groupBox)
        self.rb_skyscannercom.setObjectName("rb_skyscannercom")
        self.gridLayout_3.addWidget(self.rb_skyscannercom, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.rb_roundtrip = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_roundtrip.setChecked(True)
        self.rb_roundtrip.setObjectName("rb_roundtrip")
        self.gridLayout.addWidget(self.rb_roundtrip, 0, 0, 1, 1)
        self.rb_multicity = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_multicity.setObjectName("rb_multicity")
        self.gridLayout.addWidget(self.rb_multicity, 1, 0, 1, 1)
        self.rb_oneway = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_oneway.setObjectName("rb_oneway")
        self.gridLayout.addWidget(self.rb_oneway, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.btn_combine = QtWidgets.QPushButton(self.centralWidget)
        self.btn_combine.setObjectName("btn_combine")
        self.verticalLayout.addWidget(self.btn_combine)
        self.btn_open = QtWidgets.QPushButton(self.centralWidget)
        self.btn_open.setObjectName("btn_open")
        self.verticalLayout.addWidget(self.btn_open)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Flight Links"))
        self.groupBox.setTitle(_translate("MainWindow", "Search Engines"))
        self.rb_momondocom.setText(_translate("MainWindow", "momondo.com"))
        self.rb_pelikansk.setText(_translate("MainWindow", "pelikan.sk"))
        self.rb_kayakcom.setText(_translate("MainWindow", "kayak.com"))
        self.rb_tripadvisorcom.setText(_translate("MainWindow", "tripadvisor.com"))
        self.rb_skyscannercom.setText(_translate("MainWindow", "skyscanner.com"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Direction"))
        self.rb_roundtrip.setText(_translate("MainWindow", "Round trip"))
        self.rb_multicity.setText(_translate("MainWindow", "Multi city"))
        self.rb_oneway.setText(_translate("MainWindow", "One way"))
        self.btn_combine.setText(_translate("MainWindow", "Combine"))
        self.btn_open.setText(_translate("MainWindow", "Open in browser"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

