# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Weather_Statistic.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Statistic(object):
    def setupUi(self, Statistic):
        Statistic.setObjectName("Statistic")
        Statistic.resize(625, 568)
        Statistic.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Statistic.setWindowIcon(icon)
        Statistic.setStyleSheet("background-color: #31CCFE    ;\n"
                                "QScrollArea{\n"
                                "background-color :rgb(255, 69, 0);\n"
                                "border: 2px solid #FEFEFE;\n"
                                "}")
        self.centralwidget = QtWidgets.QWidget(Statistic)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(440, 550))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 550))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -277, 585, 825))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.SensorData = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.SensorData.setStyleSheet("color: rgb(255, 255, 255);")
        self.SensorData.setObjectName("SensorData")
        self.verticalLayout_4.addWidget(self.SensorData)
        self.frame_SensorData = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_SensorData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_SensorData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_SensorData.setObjectName("frame_SensorData")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_SensorData)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_SensorData = QtWidgets.QScrollArea(self.frame_SensorData)
        self.scrollArea_SensorData.setMinimumSize(QtCore.QSize(0, 130))
        self.scrollArea_SensorData.setMaximumSize(QtCore.QSize(16777215, 130))
        self.scrollArea_SensorData.setAccessibleDescription("")
        self.scrollArea_SensorData.setStyleSheet("background-color: #00BFFF;\n"
                                                 "")
        self.scrollArea_SensorData.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_SensorData.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_SensorData.setWidgetResizable(True)
        self.scrollArea_SensorData.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_SensorData.setObjectName("scrollArea_SensorData")
        self.scrollAreaWidgetContents_SensorData = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_SensorData.setGeometry(QtCore.QRect(0, 0, 545, 128))
        self.scrollAreaWidgetContents_SensorData.setObjectName("scrollAreaWidgetContents_SensorData")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_SensorData)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        ################################################################################################################

        ################################################################################################################
        self.scrollArea_SensorData.setWidget(self.scrollAreaWidgetContents_SensorData)
        self.verticalLayout.addWidget(self.scrollArea_SensorData)
        self.verticalLayout_4.addWidget(self.frame_SensorData)
        self.CurrentDataStatistic = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.CurrentDataStatistic.setStyleSheet("color: rgb(255, 255, 255);")
        self.CurrentDataStatistic.setObjectName("CurrentDataStatistic")
        self.verticalLayout_4.addWidget(self.CurrentDataStatistic)
        self.frame_CurrentDataStatistic = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_CurrentDataStatistic.setMinimumSize(QtCore.QSize(350, 285))
        self.frame_CurrentDataStatistic.setMaximumSize(QtCore.QSize(16777215, 240))
        self.frame_CurrentDataStatistic.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                      "color:white;\n"
                                                      "border: none;")
        self.frame_CurrentDataStatistic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CurrentDataStatistic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CurrentDataStatistic.setObjectName("frame_CurrentDataStatistic")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_CurrentDataStatistic)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OpenWeatherMap_cds = QtWidgets.QLabel(self.frame_CurrentDataStatistic)
        self.OpenWeatherMap_cds.setObjectName("OpenWeatherMap_cds")
        self.verticalLayout_2.addWidget(self.OpenWeatherMap_cds)
        self.scrollArea_WeatherBit_cds = QtWidgets.QScrollArea(self.frame_CurrentDataStatistic)
        self.scrollArea_WeatherBit_cds.setAccessibleDescription("")
        self.scrollArea_WeatherBit_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                     "")
        self.scrollArea_WeatherBit_cds.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_WeatherBit_cds.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_WeatherBit_cds.setWidgetResizable(True)
        self.scrollArea_WeatherBit_cds.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_WeatherBit_cds.setObjectName("scrollArea_WeatherBit_cds")
        self.scrollAreaWidgetContents_WeatherBit_cds = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_WeatherBit_cds.setGeometry(QtCore.QRect(0, 0, 549, 106))
        self.scrollAreaWidgetContents_WeatherBit_cds.setObjectName("scrollAreaWidgetContents_WeatherBit_cds")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_WeatherBit_cds)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        ###############################################################################################################

        ###############################################################################################################
        self.scrollArea_WeatherBit_cds.setWidget(self.scrollAreaWidgetContents_WeatherBit_cds)
        self.verticalLayout_2.addWidget(self.scrollArea_WeatherBit_cds)
        self.WeatherBit_cds = QtWidgets.QLabel(self.frame_CurrentDataStatistic)
        self.WeatherBit_cds.setObjectName("WeatherBit_cds")
        self.verticalLayout_2.addWidget(self.WeatherBit_cds)
        self.scrollArea_OWM_cds = QtWidgets.QScrollArea(self.frame_CurrentDataStatistic)
        self.scrollArea_OWM_cds.setAccessibleDescription("")
        self.scrollArea_OWM_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                              "")
        self.scrollArea_OWM_cds.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_OWM_cds.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_OWM_cds.setWidgetResizable(True)
        self.scrollArea_OWM_cds.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_OWM_cds.setObjectName("scrollArea_OWM_cds")
        self.scrollAreaWidgetContents_OWM_cds = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_OWM_cds.setGeometry(QtCore.QRect(0, 0, 549, 105))
        self.scrollAreaWidgetContents_OWM_cds.setObjectName("scrollAreaWidgetContents_OWM_cds")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_OWM_cds)
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        ###############################################################################################################

        ##############################################################################################################
        self.scrollArea_OWM_cds.setWidget(self.scrollAreaWidgetContents_OWM_cds)
        self.verticalLayout_2.addWidget(self.scrollArea_OWM_cds)
        self.verticalLayout_4.addWidget(self.frame_CurrentDataStatistic)
        self.StartDayDataStatistic = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.StartDayDataStatistic.setStyleSheet("color: rgb(255, 255, 255);")
        self.StartDayDataStatistic.setObjectName("StartDayDataStatistic")
        self.verticalLayout_4.addWidget(self.StartDayDataStatistic)
        self.frame_StartDayDataStatistic = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_StartDayDataStatistic.setMinimumSize(QtCore.QSize(350, 285))
        self.frame_StartDayDataStatistic.setMaximumSize(QtCore.QSize(16777215, 274))
        self.frame_StartDayDataStatistic.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                       "color:white;\n"
                                                       "border: none;")
        self.frame_StartDayDataStatistic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_StartDayDataStatistic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_StartDayDataStatistic.setObjectName("frame_StartDayDataStatistic")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_StartDayDataStatistic)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.OpenWeatherMap_sdds = QtWidgets.QLabel(self.frame_StartDayDataStatistic)
        self.OpenWeatherMap_sdds.setObjectName("OpenWeatherMap_sdds")
        self.verticalLayout_3.addWidget(self.OpenWeatherMap_sdds)
        self.scrollArea_OWM_sdds = QtWidgets.QScrollArea(self.frame_StartDayDataStatistic)
        self.scrollArea_OWM_sdds.setAccessibleDescription("")
        self.scrollArea_OWM_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                               "")
        self.scrollArea_OWM_sdds.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_OWM_sdds.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_OWM_sdds.setWidgetResizable(True)
        self.scrollArea_OWM_sdds.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_OWM_sdds.setObjectName("scrollArea_OWM_sdds")
        self.scrollAreaWidgetContents_OWM_sdds = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_OWM_sdds.setGeometry(QtCore.QRect(0, 0, 549, 106))
        self.scrollAreaWidgetContents_OWM_sdds.setObjectName("scrollAreaWidgetContents_OWM_sdds")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_OWM_sdds)
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        ################################################################################################################

        ################################################################################################################
        self.scrollArea_OWM_sdds.setWidget(self.scrollAreaWidgetContents_OWM_sdds)
        self.verticalLayout_3.addWidget(self.scrollArea_OWM_sdds)
        self.WeatherBit_sdds = QtWidgets.QLabel(self.frame_StartDayDataStatistic)
        self.WeatherBit_sdds.setObjectName("WeatherBit_sdds")
        self.verticalLayout_3.addWidget(self.WeatherBit_sdds)
        self.scrollArea_WeatherBit = QtWidgets.QScrollArea(self.frame_StartDayDataStatistic)
        self.scrollArea_WeatherBit.setAccessibleDescription("")
        self.scrollArea_WeatherBit.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                 "")
        self.scrollArea_WeatherBit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_WeatherBit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_WeatherBit.setWidgetResizable(True)
        self.scrollArea_WeatherBit.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_WeatherBit.setObjectName("scrollArea_WeatherBit")
        self.scrollAreaWidgetContents_WeatherBit_sdds = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_WeatherBit_sdds.setGeometry(QtCore.QRect(0, 0, 549, 105))
        self.scrollAreaWidgetContents_WeatherBit_sdds.setObjectName("scrollAreaWidgetContents_WeatherBit_sdds")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_WeatherBit_sdds)
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 9)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        ################################################################################################################

        ################################################################################################################
        self.scrollArea_WeatherBit.setWidget(self.scrollAreaWidgetContents_WeatherBit_sdds)
        self.verticalLayout_3.addWidget(self.scrollArea_WeatherBit)
        self.verticalLayout_4.addWidget(self.frame_StartDayDataStatistic)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        Statistic.setCentralWidget(self.centralwidget)

        self.retranslateUi(Statistic)
        QtCore.QMetaObject.connectSlotsByName(Statistic)

    def retranslateUi(self, Statistic):
        _translate = QtCore.QCoreApplication.translate
        Statistic.setWindowTitle(_translate("Statistic", "Statistic"))

        self.CurrentDataStatistic.setText(_translate("Statistic", "Current  data statistic"))
        self.OpenWeatherMap_cds.setText(_translate("Statistic", "OpenWeatherMap"))

        self.StartDayDataStatistic.setText(_translate("Statistic", "Start day data statistic"))
        self.OpenWeatherMap_sdds.setText(_translate("Statistic", "OpenWeatherMap"))

        self.WeatherBit_cds.setText(_translate("Statistic", "WeatherBit"))
        self.WeatherBit_sdds.setText(_translate("Statistic", "WeatherBit"))

    # #####################################################################################################################

    def SensorData_base(self, temp, humidity, date):
        self.frame_SensorData_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_SensorData)
        self.frame_SensorData_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_SensorData_2.sizePolicy().hasHeightForWidth())
        self.frame_SensorData_2.setSizePolicy(sizePolicy)
        self.frame_SensorData_2.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_SensorData_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_SensorData_2.setStyleSheet("background-color :#31CCFE;\n"
                                              "color: white;\n"
                                              "border-radius: 15px;\n"
                                              "border: 6px solid #FEFEFE;\n"
                                              "")
        self.frame_SensorData_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_SensorData_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_SensorData_2.setObjectName("frame_SensorData_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_SensorData_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_SensorData = QtWidgets.QHBoxLayout()
        self.horizontalLayout_SensorData.setObjectName("horizontalLayout_SensorData")
        self.SensorData_data_temp = QtWidgets.QLabel(self.frame_SensorData_2)
        self.SensorData_data_temp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.SensorData_data_temp.setFont(font)
        self.SensorData_data_temp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SensorData_data_temp.setStyleSheet("background-color :#31CCFE    ;\n"
                                                "color: white;\n"
                                                "border: none;")
        #self.SensorData_data_temp.setTextFormat(QtCore.Qt.MarkdownText)
        self.SensorData_data_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.SensorData_data_temp.setWordWrap(False)
        self.SensorData_data_temp.setObjectName("SensorData_data_temp")
        self.horizontalLayout_SensorData.addWidget(self.SensorData_data_temp)
        self.SensorData_data_humidity = QtWidgets.QLabel(self.frame_SensorData_2)
        self.SensorData_data_humidity.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.SensorData_data_humidity.setFont(font)
        self.SensorData_data_humidity.setStyleSheet("background-color :#31CCFE    ;\n"
                                                    "color:white;\n"
                                                    "border: none;")
        self.SensorData_data_humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.SensorData_data_humidity.setObjectName("SensorData_data_humidity")
        self.horizontalLayout_SensorData.addWidget(self.SensorData_data_humidity)
        self.verticalLayout_6.addLayout(self.horizontalLayout_SensorData)
        self.SensorData_data_date = QtWidgets.QLabel(self.frame_SensorData_2)
        self.SensorData_data_date.setMinimumSize(QtCore.QSize(110, 20))
        self.SensorData_data_date.setStyleSheet("background-color :#31CCFE    ;\n"
                                                "color:white;\n"
                                                "border: none;")
        self.SensorData_data_date.setAlignment(QtCore.Qt.AlignCenter)
        self.SensorData_data_date.setObjectName("SensorData_data_date")
        self.verticalLayout_6.addWidget(self.SensorData_data_date)
        self.horizontalLayout_3.addWidget(self.frame_SensorData_2)
        # set text
        self.SensorData_data_temp.setText(str(temp))
        self.SensorData_data_humidity.setText(str(humidity))
        self.SensorData_data_date.setText(str(date))

    def cds_owm_frame_base(self, temp, humidity, date):
        self.frame_WeatherBit_cds = QtWidgets.QFrame(self.scrollAreaWidgetContents_WeatherBit_cds)
        self.frame_WeatherBit_cds.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_WeatherBit_cds.sizePolicy().hasHeightForWidth())
        self.frame_WeatherBit_cds.setSizePolicy(sizePolicy)
        self.frame_WeatherBit_cds.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_WeatherBit_cds.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_WeatherBit_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                "color: white;\n"
                                                "border-radius: 15px;\n"
                                                "border: 6px solid #FEFEFE;\n"
                                                "background-color :rgb(255, 69, 0);\n"
                                                "")
        self.frame_WeatherBit_cds.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_WeatherBit_cds.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_WeatherBit_cds.setObjectName("frame_WeatherBit_cds")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_WeatherBit_cds)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_WeatherBit_cds = QtWidgets.QHBoxLayout()
        self.horizontalLayout_WeatherBit_cds.setObjectName("horizontalLayout_WeatherBit_cds")
        self.WeatherBit_data_temp_cds = QtWidgets.QLabel(self.frame_WeatherBit_cds)
        self.WeatherBit_data_temp_cds.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.WeatherBit_data_temp_cds.setFont(font)
        self.WeatherBit_data_temp_cds.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WeatherBit_data_temp_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                    "color: white;\n"
                                                    "border: none;")
        #self.WeatherBit_data_temp_cds.setTextFormat(QtCore.Qt.MarkdownText)
        self.WeatherBit_data_temp_cds.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherBit_data_temp_cds.setWordWrap(False)
        self.WeatherBit_data_temp_cds.setObjectName("WeatherBit_data_temp_cds")
        self.horizontalLayout_WeatherBit_cds.addWidget(self.WeatherBit_data_temp_cds)
        self.WeatherBit_data_humidity_cds = QtWidgets.QLabel(self.frame_WeatherBit_cds)
        self.WeatherBit_data_humidity_cds.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.WeatherBit_data_humidity_cds.setFont(font)
        self.WeatherBit_data_humidity_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                        "color:white;\n"
                                                        "border: none;")
        self.WeatherBit_data_humidity_cds.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherBit_data_humidity_cds.setObjectName("WeatherBit_data_humidity_cds")
        self.horizontalLayout_WeatherBit_cds.addWidget(self.WeatherBit_data_humidity_cds)
        self.verticalLayout_12.addLayout(self.horizontalLayout_WeatherBit_cds)
        self.WeatherBit_data_date_cds = QtWidgets.QLabel(self.frame_WeatherBit_cds)
        self.WeatherBit_data_date_cds.setMinimumSize(QtCore.QSize(110, 20))
        self.WeatherBit_data_date_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                    "color:white;\n"
                                                    "border: none;")
        self.WeatherBit_data_date_cds.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherBit_data_date_cds.setObjectName("WeatherBit_data_date_cds")
        self.verticalLayout_12.addWidget(self.WeatherBit_data_date_cds)
        self.horizontalLayout_5.addWidget(self.frame_WeatherBit_cds)
        # set text
        self.WeatherBit_data_temp_cds.setText(str(temp))
        self.WeatherBit_data_humidity_cds.setText(str(humidity))
        self.WeatherBit_data_date_cds.setText(str(date))

    def cds_wbit_frame_base(self, temp, humidity, date):
        self.frame_OWM_cds = QtWidgets.QFrame(self.scrollAreaWidgetContents_OWM_cds)
        self.frame_OWM_cds.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_OWM_cds.sizePolicy().hasHeightForWidth())
        self.frame_OWM_cds.setSizePolicy(sizePolicy)
        self.frame_OWM_cds.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_OWM_cds.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_OWM_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                         "color: white;\n"
                                         "border-radius: 15px;\n"
                                         "border: 6px solid #FEFEFE;\n"
                                         "background-color :rgb(255, 69, 0);\n"
                                         "")
        self.frame_OWM_cds.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_OWM_cds.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_OWM_cds.setObjectName("frame_OWM_cds")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_OWM_cds)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_OWM_cds = QtWidgets.QHBoxLayout()
        self.horizontalLayout_OWM_cds.setObjectName("horizontalLayout_OWM_cds")
        self.OWM_data_temp_cds = QtWidgets.QLabel(self.frame_OWM_cds)
        self.OWM_data_temp_cds.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.OWM_data_temp_cds.setFont(font)
        self.OWM_data_temp_cds.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OWM_data_temp_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                             "color: white;\n"
                                             "border: none;")
        #self.OWM_data_temp_cds.setTextFormat(QtCore.Qt.MarkdownText)
        self.OWM_data_temp_cds.setAlignment(QtCore.Qt.AlignCenter)
        self.OWM_data_temp_cds.setWordWrap(False)
        self.OWM_data_temp_cds.setObjectName("OWM_data_temp_cds")
        self.horizontalLayout_OWM_cds.addWidget(self.OWM_data_temp_cds)
        self.OWM_data_humidity_cds = QtWidgets.QLabel(self.frame_OWM_cds)
        self.OWM_data_humidity_cds.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OWM_data_humidity_cds.setFont(font)
        self.OWM_data_humidity_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                 "color:white;\n"
                                                 "border: none;")
        self.OWM_data_humidity_cds.setAlignment(QtCore.Qt.AlignCenter)
        self.OWM_data_humidity_cds.setObjectName("OWM_data_humidity_cds")
        self.horizontalLayout_OWM_cds.addWidget(self.OWM_data_humidity_cds)
        self.verticalLayout_14.addLayout(self.horizontalLayout_OWM_cds)
        self.OWM_data_date_cds = QtWidgets.QLabel(self.frame_OWM_cds)
        self.OWM_data_date_cds.setMinimumSize(QtCore.QSize(110, 20))
        self.OWM_data_date_cds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                             "color:white;\n"
                                             "border: none;")
        self.OWM_data_date_cds.setAlignment(QtCore.Qt.AlignCenter)
        self.OWM_data_date_cds.setObjectName("OWM_data_date_cds")
        self.verticalLayout_14.addWidget(self.OWM_data_date_cds)
        self.horizontalLayout_9.addWidget(self.frame_OWM_cds)
        # set text
        self.OWM_data_temp_cds.setText(str(temp))
        self.OWM_data_humidity_cds.setText(str(humidity))
        self.OWM_data_date_cds.setText(str(date))

    def frame_OWM_sdds_base(self, temp, humidity, date):
        self.frame_OWM_sdds = QtWidgets.QFrame(self.scrollAreaWidgetContents_OWM_sdds)
        self.frame_OWM_sdds.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_OWM_sdds.sizePolicy().hasHeightForWidth())
        self.frame_OWM_sdds.setSizePolicy(sizePolicy)
        self.frame_OWM_sdds.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_OWM_sdds.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_OWM_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                          "color: white;\n"
                                          "border-radius: 15px;\n"
                                          "border: 6px solid #FEFEFE;\n"
                                          "background-color :rgb(255, 69, 0);\n"
                                          "")
        self.frame_OWM_sdds.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_OWM_sdds.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_OWM_sdds.setObjectName("frame_OWM_sdds")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_OWM_sdds)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_OWM_sdds = QtWidgets.QHBoxLayout()
        self.horizontalLayout_OWM_sdds.setObjectName("horizontalLayout_OWM_sdds")
        self.OWM_data_temp_sdds = QtWidgets.QLabel(self.frame_OWM_sdds)
        self.OWM_data_temp_sdds.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.OWM_data_temp_sdds.setFont(font)
        self.OWM_data_temp_sdds.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.OWM_data_temp_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                              "color: white;\n"
                                              "border: none;")
        #self.OWM_data_temp_sdds.setTextFormat(QtCore.Qt.MarkdownText)
        self.OWM_data_temp_sdds.setAlignment(QtCore.Qt.AlignCenter)
        self.OWM_data_temp_sdds.setWordWrap(False)
        self.OWM_data_temp_sdds.setObjectName("OWM_data_temp_sdds")
        self.horizontalLayout_OWM_sdds.addWidget(self.OWM_data_temp_sdds)
        self.OWM_data_humidity_sdds = QtWidgets.QLabel(self.frame_OWM_sdds)
        self.OWM_data_humidity_sdds.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.OWM_data_humidity_sdds.setFont(font)
        self.OWM_data_humidity_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                  "color:white;\n"
                                                  "border: none;")
        self.OWM_data_humidity_sdds.setAlignment(QtCore.Qt.AlignCenter)
        self.OWM_data_humidity_sdds.setObjectName("OWM_data_humidity_sdds")
        self.horizontalLayout_OWM_sdds.addWidget(self.OWM_data_humidity_sdds)
        self.verticalLayout_24.addLayout(self.horizontalLayout_OWM_sdds)
        self.OWM_data_date_sdds = QtWidgets.QLabel(self.frame_OWM_sdds)
        self.OWM_data_date_sdds.setMinimumSize(QtCore.QSize(110, 20))
        self.OWM_data_date_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                              "color:white;\n"
                                              "border: none;")
        self.OWM_data_date_sdds.setAlignment(QtCore.Qt.AlignCenter)
        self.OWM_data_date_sdds.setObjectName("OWM_data_date_sdds")
        self.verticalLayout_24.addWidget(self.OWM_data_date_sdds)
        self.horizontalLayout_14.addWidget(self.frame_OWM_sdds)
        # set text
        self.OWM_data_temp_sdds.setText(str(temp))
        self.OWM_data_humidity_sdds.setText(str(humidity))
        self.OWM_data_date_sdds.setText(str(date))

    def frame_WeatherBit_sdds_base(self, temp, humidity, date):
        self.frame_WeatherBit_sdds = QtWidgets.QFrame(self.scrollAreaWidgetContents_WeatherBit_sdds)
        self.frame_WeatherBit_sdds.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_WeatherBit_sdds.sizePolicy().hasHeightForWidth())
        self.frame_WeatherBit_sdds.setSizePolicy(sizePolicy)
        self.frame_WeatherBit_sdds.setMinimumSize(QtCore.QSize(150, 60))
        self.frame_WeatherBit_sdds.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_WeatherBit_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                 "color: white;\n"
                                                 "border-radius: 15px;\n"
                                                 "border: 6px solid #FEFEFE;\n"
                                                 "background-color :rgb(255, 69, 0);\n"
                                                 "")
        self.frame_WeatherBit_sdds.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_WeatherBit_sdds.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_WeatherBit_sdds.setObjectName("frame_WeatherBit_sdds")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_WeatherBit_sdds)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.horizontalLayout_WeatherBit_sdds = QtWidgets.QHBoxLayout()
        self.horizontalLayout_WeatherBit_sdds.setObjectName("horizontalLayout_WeatherBit_sdds")
        self.WeatherBit_data_temp_sdds = QtWidgets.QLabel(self.frame_WeatherBit_sdds)
        self.WeatherBit_data_temp_sdds.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.WeatherBit_data_temp_sdds.setFont(font)
        self.WeatherBit_data_temp_sdds.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.WeatherBit_data_temp_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                     "color: white;\n"
                                                     "border: none;")
        #self.WeatherBit_data_temp_sdds.setTextFormat(QtCore.Qt.MarkdownText)
        self.WeatherBit_data_temp_sdds.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherBit_data_temp_sdds.setWordWrap(False)
        self.WeatherBit_data_temp_sdds.setObjectName("WeatherBit_data_temp_sdds")
        self.horizontalLayout_WeatherBit_sdds.addWidget(self.WeatherBit_data_temp_sdds)
        self.WeatherBit_data_humidity_sdds = QtWidgets.QLabel(self.frame_WeatherBit_sdds)
        self.WeatherBit_data_humidity_sdds.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.WeatherBit_data_humidity_sdds.setFont(font)
        self.WeatherBit_data_humidity_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                         "color:white;\n"
                                                         "border: none;")
        self.WeatherBit_data_humidity_sdds.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherBit_data_humidity_sdds.setObjectName("WeatherBit_data_humidity_sdds")
        self.horizontalLayout_WeatherBit_sdds.addWidget(self.WeatherBit_data_humidity_sdds)
        self.verticalLayout_26.addLayout(self.horizontalLayout_WeatherBit_sdds)
        self.WeatherBit_data_date_sdds = QtWidgets.QLabel(self.frame_WeatherBit_sdds)
        self.WeatherBit_data_date_sdds.setMinimumSize(QtCore.QSize(110, 20))
        self.WeatherBit_data_date_sdds.setStyleSheet("background-color :rgb(255, 69, 0);\n"
                                                     "color:white;\n"
                                                     "border: none;")
        self.WeatherBit_data_date_sdds.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherBit_data_date_sdds.setObjectName("WeatherBit_data_date_sdds")
        self.verticalLayout_26.addWidget(self.WeatherBit_data_date_sdds)
        self.horizontalLayout_15.addWidget(self.frame_WeatherBit_sdds)
        # set text
        self.WeatherBit_data_temp_sdds.setText(str(temp))
        self.WeatherBit_data_humidity_sdds.setText(str(humidity))
        self.WeatherBit_data_date_sdds.setText(str(date))
