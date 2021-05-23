import time
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QTableWidget, QTableView, QHeaderView, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QBrush, QColor, QFont
from  ui.rentUi3 import Ui_MainWindow
import sys
import pandas as pd
import math
from  datetime import datetime

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.checkHistoryFile.setChecked(True)
        self.ui.filepath.setText(r"C:\Users\syaun\Desktop\Rent\file\202103.xlsx")
        self.ui.getFilePathButton.clicked.connect(self.getFileData)
        self.ui.getDataButton.clicked.connect(self.getDataOut)
        self.ui.goCalculate.clicked.connect(self.calculate)

        self.state_get_data = False
        self.state_calculate=False
        self.state_nofile_calculate = False
        self.ui.exportButton.clicked.connect(self.expotToexcelButton)


    def expotToexcelButton(self):
        #有上次歷史檔案
        if(self.state_get_data==True and self.state_calculate==True):
            self.df_export = pd.DataFrame(index = range(self.table.rowCount()+1),columns=self.horizontalHeader)
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    if(type(self.table.item(i,j))!=type(None) and (self.table.item(i,j).text()!="")):
                        self.df_export.iloc[i,j] = self.table.item(i,j).text()
                    else:
                        pass
            self.can_export = True
            self.haveHistory = True
            print(self.df_export)
            self.export()
            # savefilename = "初始電表"+datetime.today().strftime("%Y%m")+".xlsx"
            # df_export.to_excel("./save/"+savefilename,index=None)
        #初始檔建立
        elif(self.state_nofile_calculate==True):
            self.df_export = pd.DataFrame(index=range(self.table.rowCount()), columns=self.horizontalHeader)
            self.can_export = False
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    if (type(self.table.item(i, j)) != type(None) and (self.table.item(i, j).text() != "")):
                        self.df_export.iloc[i, j] = self.table.item(i, j).text()
                        conttinue=True
                    else:
                        self.ui.statusbar.showMessage("表格尚未產生或尚未細算成功過")
                        conttinue = False
                        break
            #完整填好了初始檔
            if(conttinue):
                self.ui.statusbar.showMessage("")
                self.can_export = True
                self.haveHistory = False
                print(self.df_export)
                self.export()
            else:
                self.ui.statusbar.showMessage("尚未填妥表格")
        else:
            self.ui.statusbar.showMessage("表格尚未產生或尚未細算成功過")

        # else:
    def export(self):
            print(datetime.today().strftime("%Y%m"))
            if(self.haveHistory):
                self.df_export.iloc[5][6] = str(self.ui.finalRent.text())
                savefilename = datetime.today().strftime("%Y%m") + "房租.xlsx"
            else:
                savefilename = datetime.today().strftime("%Y%m") + "初始檔.xlsx"

            self.df_export.to_excel('./save/' + savefilename, index=None)

    def calculate(self):
        for i in range(self.table.rowCount()):
            if(self.table.item(i,1).text()!=""):
                self.table.item(i,1).setBackground(QColor("#FFFFFF"))
                pre = self.table.item(i,1).text()
                pre_pre = self.table.item(i,2).text()
                diff = int(pre)-int(pre_pre)

                self.table.setItem(i,3,QTableWidgetItem(str(diff)))
                if(i!=4):
                    diff_4 = diff * 4
                    self.table.setItem(i,4,QTableWidgetItem(str(diff_4)))
                if(i==4):
                    rentFee = self.ui.RentFee.text()

                    for j in range(self.table.rowCount()):
                        if(j!=4):
                            pre_4 = self.table.item(j,4).text()
                            pre_4_add = diff+int(pre_4)
                            self.table.setItem(j,5,QTableWidgetItem(str(pre_4_add))) #個人電費加公費
                            if (rentFee == ""):
                                self.ui.statusbar.showMessage("房租尚未填入")
                                self.ui.RentFee.setStyleSheet("QLineEdit"
                                                                "{"
                                                                "background : lightblue;"
                                                                "}")
                            else:
                                pre_total = pre_4_add+int(rentFee)
                                self.table.setItem(j,6,QTableWidgetItem(str(pre_total)))
                                self.state_calculate = True
                                self.ui.RentFee.setStyleSheet("QLineEdit"
                                                              "{"
                                                              "background : white;"
                                                              "}")
                                self.ui.statusbar.showMessage("")
                                total_rent = 0

                                for i in range(self.table.rowCount() - 1):
                                    if (type(self.table.item(i, 6)) != type(None)):
                                        per_rent = int(self.table.item(i, 6).text())
                                        total_rent += (per_rent)
                                    print("total_rent:", total_rent)
                                    text = "房租為:" + str(total_rent) + "\n"
                                    self.ui.finalRent.setText(text)
            else:
                self.ui.statusbar.showMessage("還有欄位是空的")



    def getDataOut(self):
        #如果有上筆歷史檔案要匯入的話
        self.state_get_data=True
        if(self.ui.checkHistoryFile.isChecked()):
            #檔案路徑不能為空
            if(self.ui.filepath.text()==""):
                self.ui.statusbar.showMessage("檔案路徑不能為空")
            else:#如果有檔案路徑則執行資料讀取
                self.filename = self.ui.filepath.text()
                if(self.filename!=""):
                    self.haveFile(self.filename)
                    self.ui.goCalculate.show()
                else:
                    self.ui.statusbar.showMessage("檔案路徑不能為空")
        else: #沒有上筆歷史檔案要匯入的話
            self.ui.filepath.setText("")
            self.ui.goCalculate.hide()
            self.state_calculate=False
            self.noHaveFile()

    def updateTable(self,row,column,header):
        self.table = QTableWidget(row,column)
        self.table.setHorizontalHeaderLabels(header)
        if (self.ui.tableView.count() >= 1):
            self.table.clear()
            self.table = QTableWidget(row, column)
            self.table.setHorizontalHeaderLabels(header)
            print("大於1個")
            self.ui.tableView.itemAt(0).widget().deleteLater()
            self.ui.tableView.addWidget(self.table)
        else:
            self.ui.tableView.addWidget(self.table)

        self.roomName = ['A', 'B', 'C', 'D', '公']
        for i in range(len(self.roomName)):
            self.table.setItem(i, 0, QTableWidgetItem(self.roomName[i]))
            self.table.item(i, 0).setTextAlignment(Qt.AlignCenter)

    def noHaveFile(self):
        # self.ui.filepath.setText("")
        self.horizontalHeader = ["編號","上個月的度數"]
        self.updateTable(5,2,self.horizontalHeader)

        self.state_nofile_calculate=True
        print("tableView的元素個數:",self.ui.tableView.count())
        # for i in range(self.table.rowCount()):
        #     self.table.setItem(i,1,QTableWidgetItem(""))
        #     self.table.item(i,1).setBackground(QColor("#ff6347"))
        # self.ui.statusbar.showMessage("請在顏色區填入這個月的度數")


    def haveFile(self,filename):
        self.horizontalHeader = ["編號", "上個月", "前個月", "度差", "4元/度", '含公費', '總共']

        self.updateTable(5,7,self.horizontalHeader)
        print("tableView的元素個數:",self.ui.tableView.count())

        df = pd.read_excel(filename,header=0)
        df = df.fillna("") #空值處理
        df_array=df.values
        for i in range(len(df_array)):
            if(df_array[i][1]!=""):
                per = int(df_array[i][1])  #浮點數轉整數
                self.table.setItem(i,2,QTableWidgetItem(str(per)))
                self.table.setItem(i,1,QTableWidgetItem(""))
                self.table.item(i,1).setBackground(QColor("#ff6347"))
        self.ui.statusbar.showMessage("請在顏色區填入這個月的度數")

    def getFileData(self):
        options = QFileDialog.Options()
        # 不使用本機文件對話框
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.ui.filepath.setText(fileName)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())