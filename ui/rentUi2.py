# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rentUi2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.historyFilePath = QtWidgets.QLineEdit(self.centralwidget)
        self.historyFilePath.setObjectName("historyFilePath")
        self.horizontalLayout.addWidget(self.historyFilePath)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.fileinputstate = QtWidgets.QLabel(self.centralwidget)
        self.fileinputstate.setText("")
        self.fileinputstate.setObjectName("fileinputstate")
        self.verticalLayout.addWidget(self.fileinputstate)
        self.getDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.getDataButton.setObjectName("getDataButton")
        self.verticalLayout.addWidget(self.getDataButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_water = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_water.setObjectName("checkBox_water")
        self.horizontalLayout_2.addWidget(self.checkBox_water)
        self.waterFee = QtWidgets.QLineEdit(self.centralwidget)
        self.waterFee.setObjectName("waterFee")
        self.horizontalLayout_2.addWidget(self.waterFee)
        self.waterCostUnit = QtWidgets.QLabel(self.centralwidget)
        self.waterCostUnit.setObjectName("waterCostUnit")
        self.horizontalLayout_2.addWidget(self.waterCostUnit)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.RentCost = QtWidgets.QLineEdit(self.centralwidget)
        self.RentCost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RentCost.setObjectName("RentCost")
        self.horizontalLayout_8.addWidget(self.RentCost)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.result_Power = QtWidgets.QVBoxLayout()
        self.result_Power.setObjectName("result_Power")
        self.verticalLayout_2.addLayout(self.result_Power)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelTotalRent = QtWidgets.QLabel(self.centralwidget)
        self.labelTotalRent.setObjectName("labelTotalRent")
        self.horizontalLayout_4.addWidget(self.labelTotalRent)
        self.labelState = QtWidgets.QLabel(self.centralwidget)
        self.labelState.setObjectName("labelState")
        self.horizontalLayout_4.addWidget(self.labelState)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.pushButtonCaculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCaculate.setObjectName("pushButtonCaculate")
        self.verticalLayout_2.addWidget(self.pushButtonCaculate)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButtonExport = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.verticalLayout_2.addWidget(self.pushButtonExport)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 25))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menu.addAction(self.actionClose)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "是否有歷史紀錄"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.getDataButton.setText(_translate("MainWindow", "撈資料並計算"))
        self.checkBox_water.setText(_translate("MainWindow", "是否含水費"))
        self.waterCostUnit.setText(_translate("MainWindow", "元"))
        self.label_8.setText(_translate("MainWindow", "房租"))
        self.RentCost.setText(_translate("MainWindow", "2500"))
        self.label_9.setText(_translate("MainWindow", "元"))
        self.labelTotalRent.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">總金額</span></p></body></html>"))
        self.labelState.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">State</span></p></body></html>"))
        self.pushButtonCaculate.setText(_translate("MainWindow", "計算"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">功能列表</span></p></body></html>"))
        self.pushButtonExport.setText(_translate("MainWindow", "輸出文件"))
        self.menu.setTitle(_translate("MainWindow", "功能"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
