import time
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QFileDialog, QTableWidget, QTableView, QHeaderView, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QBrush, QColor, QFont
from  ui.rentUi2 import Ui_MainWindow
import sys
import pandas as pd
from  datetime import datetime

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.waterFee.hide()
        self.ui.waterCostUnit.hide()
        self.last_month = list()
        self.ui.checkBox.setChecked(True)
        self.ui.checkBox_water.setChecked(False)
        self.ui.labelState.setText("")
        # self.ui.historyFilePath.setText("C:/Users/kuen/Desktop/Rent/file/202104房租.xlsx")
        self.ui.historyFilePath.setText(r"C:\Users\syaun\Desktop\Rent/file/202104房租.xlsx")
        self.ui.checkBox.stateChanged.connect(self.showFilePath)
        self.ui.checkBox_water.stateChanged.connect(self.showWaterCost)
        self.ui.getDataButton.clicked.connect(self.getData)
        self.ui.toolButton.clicked.connect(self.getPath)


        self.horizontalHeader = ["編號", "上個月", "前個月", "度差", "4元/度",'含公費','總共']
        self.table = QTableWidget(5,7)
        self.table.setHorizontalHeaderLabels(self.horizontalHeader)
        self.ui.result_Power.addWidget(self.table)
        # layout = QVBoxLayout();
        # layout.addWidget(self.table);
        self.ui.pushButtonCaculate.clicked.connect(self.Caculate)
        self.ui.pushButtonExport.clicked.connect(self.expotToexcel)



    def showWaterCost(self):
        if self.ui.checkBox_water.isChecked():
            self.ui.waterFee.show()
            self.ui.waterCostUnit.show()
        else:
            self.ui.waterFee.hide()
            self.ui.waterCostUnit.hide()
    def showFilePath(self):
        if self.ui.checkBox.isChecked():
            self.ui.historyFilePath.show()
            self.ui.toolButton.show()
            self.ui.getDataButton.show()
            self.ui.pushButtonCaculate.show()
            for i in range(len(self.name_header)):
                self.table.setItem(i,0,QTableWidgetItem(""))
            self.ui.statusbar.showMessage("請先選擇上次的統計檔案>接著按計算>計算結果無誤>輸出文件")
            print("show file path checkbox is clicked")
        else:
            # 如果沒有歷史紀錄文檔可以自動生成初始紀錄文檔
            self.ui.historyFilePath.hide()
            self.ui.toolButton.hide()
            self.ui.getDataButton.hide()
            self.ui.pushButtonCaculate.hide()
            self.ui.statusbar.showMessage("直接於表格中「上個月」欄位寫入當前電表度數，方便後續抓文件資料讀取")
            self.name_header=['A','B','C','D','公']
            for i in range(len(self.name_header)):
                self.table.setItem(i,0,QTableWidgetItem(self.name_header[i]))


    def getPath(self):
        options = QFileDialog.Options()
        #不使用本機文件對話框
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.ui.historyFilePath.setText(fileName)


    def getData(self):
        #取得選取好檔案路徑之路徑進行讀檔
        filepath = self.ui.historyFilePath.text()

        if filepath == '':
            self.ui.fileinputstate.setText("↑請選擇檔案")
        else:
            print("else")
            self.ui.fileinputstate.setText("")
            print(filepath)
            df = pd.read_excel(filepath)
            print(df)
            print(df.values)

            dataArray = df.values  # 2維陣列

            self.last_month = list()
            for i in range(len(dataArray)):
                self.last_month.append(dataArray[i][1])
                self.table.setItem(i, 2, QTableWidgetItem(str(dataArray[i][1])))
                self.table.setItem(i, 0, QTableWidgetItem(dataArray[i][0]))

                if '公' in dataArray[i]:
                    break

    def Caculate(self):
        print(len(self.last_month))

        self.less_diff_multply_4=list()
        if(len(self.last_month)!=0):
            print("have data")
            self.ui.labelState.setText("")
            for i in range(len(self.last_month)):

                if(type(self.table.item(i,1))==type(None) or (self.table.item(i,1).text()=="")):
                    self.ui.labelState.setText("↑請完整填入值")
                    # self.table.item(i,2).setBackground(QtGui.QColor("#ff4500"))
                    self.table.setItem(i,1,QTableWidgetItem("")) #因為是Nonetype，所以要重新賦予一個空值
                    #setBackground必須是有對象的，若對象為null or none，則會出錯
                    self.table.item(i, 1).setBackground(QColor("#ff4500"))
                    print(self.table.item(i,2).text())
                else:
                    text_value = self.table.item(i, 1).text()
                    less_diff = int(int(text_value)-self.last_month[i])
                    self.less_diff_multply_4.append(less_diff*4)
                    self.table.setItem(i,3,QTableWidgetItem(str(less_diff)))
                    if i!=4:
                        self.table.setItem(i,4,QTableWidgetItem(str(less_diff*4)))

                    if i==4:
                        power_diff = less_diff
                        #讀取房租租金
                        rent_fee = int(self.ui.RentCost.text())
                        total_Rent =0
                        if(self.ui.checkBox_water.isChecked()):
                            water_fee = int(self.ui.waterFee.text())
                        print(rent_fee)
                        for j in range(len(self.last_month)-1):
                            individual_power = self.table.item(j, 4).text()
                            individual_add_power = int(individual_power)+power_diff
                            total = individual_add_power+rent_fee
                            print(individual_add_power)
                            print(type(individual_add_power))

                            total_Rent+=total #總共要會的房租為個別的總和

                            self.table.setItem(j,5,QTableWidgetItem(str(individual_add_power)))
                            self.table.setItem(j,6,QTableWidgetItem(str(total)))
                        self.ui.labelTotalRent.setFont(QFont('Arial', 12))
                        self.ui.labelTotalRent.setText("本月房租應繳交"+str(total_Rent))
                    self.ui.labelState.setText("")
                    self.table.item(i, 1).setBackground(QColor("#ffffff"))
        else:
            self.ui.labelState.setText("請進行資料讀取")

    def expotToexcel(self):
        if(self.ui.checkBox.isChecked()==False):
            df_export = pd.DataFrame(index = range(self.table.rowCount()+1),columns=self.horizontalHeader)
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    if(type(self.table.item(i,j))!=type(None) and (self.table.item(i,j).text()!="")):
                        df_export.iloc[i,j] = self.table.item(i,j).text()
                    else:
                        pass
            print(df_export)
            savefilename = "初始電表"+datetime.today().strftime("%Y%m")+".xlsx"
            df_export.to_excel("./save/"+savefilename,index=None)
        else:
            if(self.table.rowCount()!=0 and self.table.colorCount()!=0):
                df_export = pd.DataFrame(index = range(self.table.rowCount()+1),columns=self.horizontalHeader)
                for i in range(self.table.rowCount()):
                    for j in range(self.table.columnCount()):
                        if(type(self.table.item(i,j))!=type(None) and (self.table.item(i,j).text()!="")):
                            df_export.iloc[i,j] = self.table.item(i,j).text()
                        else:
                            pass
                df_export.iloc[5][6] = str(self.ui.labelTotalRent.text())
                print(df_export)
                print(datetime.today().strftime("%Y%m"))
                savefilename = datetime.today().strftime("%Y%m")+"房租.xlsx"

                df_export.to_excel('./save/'+savefilename,index=None)






if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())