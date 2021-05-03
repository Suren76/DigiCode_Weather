# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Weather_SensorLiveMode.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SensorLiveMode(object):
    def setupUi(self, SensorLiveMode):
        SensorLiveMode.setObjectName("SensorLiveMode")
        SensorLiveMode.resize(320, 320)
        SensorLiveMode.setMinimumSize(QtCore.QSize(320, 320))
        SensorLiveMode.setMaximumSize(QtCore.QSize(320, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SensorLiveMode.setWindowIcon(icon)
        SensorLiveMode.setStyleSheet("background-color: #31CCFE    ;\n"
"")
        self.centralwidget = QtWidgets.QWidget(SensorLiveMode)
        self.centralwidget.setObjectName("centralwidget")
        self.Sensor_data_temp = QtWidgets.QLabel(self.centralwidget)
        self.Sensor_data_temp.setGeometry(QtCore.QRect(40, 50, 170, 170))
        font = QtGui.QFont()
        font.setPointSize(90)
        font.setBold(True)
        font.setWeight(75)
        self.Sensor_data_temp.setFont(font)
        self.Sensor_data_temp.setStyleSheet("background-color: #00BFFF;\n"
"color: white;\n"
"")
        #self.Sensor_data_temp.setTextFormat(QtCore.Qt.MarkdownText)
        self.Sensor_data_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.Sensor_data_temp.setObjectName("Sensor_data_temp")
        self.Sensor_data = QtWidgets.QLabel(self.centralwidget)
        self.Sensor_data.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.Sensor_data.setStyleSheet("background-color: #00BFFF;\n"
"border: 6px solid #FEFEFE;\n"
"border-top-left-radius: 70px;\n"
"border-bottom-right-radius: 70px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-left-radius: 20px;")
        self.Sensor_data.setText("")
        self.Sensor_data.setObjectName("Sensor_data")
        self.about_localdata = QtWidgets.QLabel(self.centralwidget)
        self.about_localdata.setGeometry(QtCore.QRect(40, 260, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.about_localdata.setFont(font)
        self.about_localdata.setStyleSheet("background-color: #00BFFF;\n"
"color: white;\n"
"\n"
"")
        self.about_localdata.setAlignment(QtCore.Qt.AlignCenter)
        self.about_localdata.setObjectName("about_localdata")
        self.Sensor_data_humidity = QtWidgets.QLabel(self.centralwidget)
        self.Sensor_data_humidity.setGeometry(QtCore.QRect(190, 210, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Sensor_data_humidity.setFont(font)
        self.Sensor_data_humidity.setStyleSheet("background-color: #00BFFF;\n"
"color:white;")
        self.Sensor_data_humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.Sensor_data_humidity.setObjectName("Sensor_data_humidity")
        self.Sensor_data.raise_()
        self.about_localdata.raise_()
        self.Sensor_data_humidity.raise_()
        self.Sensor_data_temp.raise_()
        SensorLiveMode.setCentralWidget(self.centralwidget)

        self.retranslateUi(SensorLiveMode)
        QtCore.QMetaObject.connectSlotsByName(SensorLiveMode)

    def retranslateUi(self, SensorLiveMode):
        _translate = QtCore.QCoreApplication.translate
        SensorLiveMode.setWindowTitle(_translate("SensorLiveMode", "Sensor Live Mode"))
        self.Sensor_data_temp.setText(_translate("SensorLiveMode", "t"))
        self.about_localdata.setText(_translate("SensorLiveMode", "Weather get from  \n"
"     local sensor"))
        self.Sensor_data_humidity.setText(_translate("SensorLiveMode", "h"))
# import 1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SensorLiveMode = QtWidgets.QMainWindow()
    ui = Ui_SensorLiveMode()
    ui.setupUi(SensorLiveMode)
    SensorLiveMode.show()
    sys.exit(app.exec_())
