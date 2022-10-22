# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacev2ZYbEnp.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(720, 480))
        MainWindow.setMaximumSize(QSize(2560, 2160))
        MainWindow.setBaseSize(QSize(720, 480))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMaximumSize(QSize(400, 16777215))
        self.tab_query = QWidget()
        self.tab_query.setObjectName(u"tab_query")
        self.gridLayout_2 = QGridLayout(self.tab_query)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.query1 = QRadioButton(self.tab_query)
        self.query1.setObjectName(u"query1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.query1.sizePolicy().hasHeightForWidth())
        self.query1.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query1, 0, 0, 1, 1)

        self.label_3 = QLabel(self.tab_query)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.query2 = QRadioButton(self.tab_query)
        self.query2.setObjectName(u"query2")
        sizePolicy2.setHeightForWidth(self.query2.sizePolicy().hasHeightForWidth())
        self.query2.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query2, 1, 0, 1, 1)

        self.label_6 = QLabel(self.tab_query)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)

        self.query3 = QRadioButton(self.tab_query)
        self.query3.setObjectName(u"query3")
        sizePolicy2.setHeightForWidth(self.query3.sizePolicy().hasHeightForWidth())
        self.query3.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query3, 2, 0, 1, 1)

        self.label_8 = QLabel(self.tab_query)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_8, 2, 1, 1, 1)

        self.query4 = QRadioButton(self.tab_query)
        self.query4.setObjectName(u"query4")
        sizePolicy2.setHeightForWidth(self.query4.sizePolicy().hasHeightForWidth())
        self.query4.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query4, 3, 0, 1, 1)

        self.label_4 = QLabel(self.tab_query)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.query5 = QRadioButton(self.tab_query)
        self.query5.setObjectName(u"query5")
        sizePolicy2.setHeightForWidth(self.query5.sizePolicy().hasHeightForWidth())
        self.query5.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query5, 4, 0, 1, 1)

        self.label_9 = QLabel(self.tab_query)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_9, 4, 1, 1, 1)

        self.query6 = QRadioButton(self.tab_query)
        self.query6.setObjectName(u"query6")
        sizePolicy2.setHeightForWidth(self.query6.sizePolicy().hasHeightForWidth())
        self.query6.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query6, 5, 0, 1, 1)

        self.label_5 = QLabel(self.tab_query)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_5, 5, 1, 1, 1)

        self.query7 = QRadioButton(self.tab_query)
        self.query7.setObjectName(u"query7")
        sizePolicy2.setHeightForWidth(self.query7.sizePolicy().hasHeightForWidth())
        self.query7.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query7, 6, 0, 1, 1)

        self.label_10 = QLabel(self.tab_query)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_10, 6, 1, 1, 1)

        self.query8 = QRadioButton(self.tab_query)
        self.query8.setObjectName(u"query8")
        sizePolicy2.setHeightForWidth(self.query8.sizePolicy().hasHeightForWidth())
        self.query8.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query8, 7, 0, 1, 1)

        self.label_11 = QLabel(self.tab_query)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_11, 7, 1, 1, 1)

        self.query9 = QRadioButton(self.tab_query)
        self.query9.setObjectName(u"query9")
        sizePolicy2.setHeightForWidth(self.query9.sizePolicy().hasHeightForWidth())
        self.query9.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query9, 8, 0, 1, 1)

        self.label_12 = QLabel(self.tab_query)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_12, 8, 1, 1, 1)

        self.query12 = QRadioButton(self.tab_query)
        self.query12.setObjectName(u"query12")
        sizePolicy2.setHeightForWidth(self.query12.sizePolicy().hasHeightForWidth())
        self.query12.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query12, 9, 0, 1, 1)

        self.label_13 = QLabel(self.tab_query)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_13, 9, 1, 1, 1)

        self.query13 = QRadioButton(self.tab_query)
        self.query13.setObjectName(u"query13")
        sizePolicy2.setHeightForWidth(self.query13.sizePolicy().hasHeightForWidth())
        self.query13.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query13, 10, 0, 1, 1)

        self.label_14 = QLabel(self.tab_query)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_14, 10, 1, 1, 1)

        self.query14 = QRadioButton(self.tab_query)
        self.query14.setObjectName(u"query14")
        sizePolicy2.setHeightForWidth(self.query14.sizePolicy().hasHeightForWidth())
        self.query14.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query14, 11, 0, 1, 1)

        self.label_15 = QLabel(self.tab_query)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_15, 11, 1, 1, 1)

        self.query15 = QRadioButton(self.tab_query)
        self.query15.setObjectName(u"query15")
        sizePolicy2.setHeightForWidth(self.query15.sizePolicy().hasHeightForWidth())
        self.query15.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query15, 12, 0, 1, 1)

        self.label_16 = QLabel(self.tab_query)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_16, 12, 1, 1, 1)

        self.query16 = QRadioButton(self.tab_query)
        self.query16.setObjectName(u"query16")
        sizePolicy2.setHeightForWidth(self.query16.sizePolicy().hasHeightForWidth())
        self.query16.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.query16, 13, 0, 1, 1)

        self.label_17 = QLabel(self.tab_query)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_17, 13, 1, 1, 1)

        self.queryButton = QPushButton(self.tab_query)
        self.queryButton.setObjectName(u"queryButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.queryButton.sizePolicy().hasHeightForWidth())
        self.queryButton.setSizePolicy(sizePolicy3)
        self.queryButton.setMinimumSize(QSize(200, 0))
        self.queryButton.setMaximumSize(QSize(400, 16777215))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.queryButton.setFont(font)

        self.gridLayout_2.addWidget(self.queryButton, 14, 1, 1, 1)

        self.tabWidget.addTab(self.tab_query, "")
        self.tab_full = QWidget()
        self.tab_full.setObjectName(u"tab_full")
        self.verticalLayout = QVBoxLayout(self.tab_full)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.tab_full)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(18)
        self.label_7.setFont(font1)

        self.verticalLayout.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.comboBox_tables = QComboBox(self.tab_full)
        self.comboBox_tables.setObjectName(u"comboBox_tables")
        self.comboBox_tables.setMinimumSize(QSize(0, 60))

        self.verticalLayout.addWidget(self.comboBox_tables)

        self.verticalSpacer_2 = QSpacerItem(0, 60, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.showTableButton = QPushButton(self.tab_full)
        self.showTableButton.setObjectName(u"showTableButton")
        font2 = QFont()
        font2.setPointSize(14)
        self.showTableButton.setFont(font2)

        self.verticalLayout.addWidget(self.showTableButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_full, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 2, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 61, 21))
        self.nextButton = QPushButton(self.groupBox_2)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(270, 20, 75, 24))
        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(60, 20, 61, 22))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(10)
        self.spinBox.setFont(font3)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(2000)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 20, 71, 20))
        self.label_totalRows = QLabel(self.groupBox_2)
        self.label_totalRows.setObjectName(u"label_totalRows")
        self.label_totalRows.setGeometry(QRect(208, 20, 51, 21))

        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setMinimumSize(QSize(0, 60))
        self.exportButton.setMaximumSize(QSize(600, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        self.exportButton.setFont(font4)

        self.gridLayout.addWidget(self.exportButton, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        if (self.tableWidget.rowCount() < 100):
            self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName(u"tableWidget")
        font5 = QFont()
        font5.setFamily(u"Source Sans Pro")
        font5.setPointSize(9)
        self.tableWidget.setFont(font5)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"alternate-background-color: rgb(238, 238, 238);\n"
"background-color: rgb(200, 200, 200);")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(5)

        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.tableWidget.raise_()
        self.groupBox_2.raise_()
        self.tabWidget.raise_()
        self.exportButton.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.query1.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"List all provincial districts in decreasing order based on median full time income of all genders", None))
        self.query2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"List all provincial districts in decreasing order based on crime incidents reported per capita", None))
        self.query3.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"List Winnipeg wards in descending order based on the number of trees per capita and show the median income", None))
        self.query4.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Top 5 popular crimes in the top 3 neighbourhoods in number of advanced degree holders", None))
        self.query5.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Rank the companies with tenders awarded by the U of M and show the number of fraud incidents in the neighbourhoods they belong in", None))
        self.query6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Rank School divisions by bus route count", None))
        self.query7.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Rank the wards by total park area and show average full time median income in the area", None))
        self.query8.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"How many trees in each ward are the only representative of their species in that ward", None))
        self.query9.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Top 5 popular crimes in the 5 shadiest (by tree count) neighbourhoods in Winnipeg", None))
        self.query12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"List MLAs that get extra compensation greater than the average median income in their district", None))
        self.query13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"How many high school aged people in each school division are not enrolled in school", None))
        self.query14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Neighbourhoods with a park but no high schools", None))
        self.query15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Bus routes that pass through the top 10 neighbourhoods for robbery", None))
        self.query16.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Rank electoral districts by median income and count all the play structures in the area", None))
        self.queryButton.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_query), QCoreApplication.translate("MainWindow", u"Queries", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Select a table", None))
        self.showTableButton.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_full), QCoreApplication.translate("MainWindow", u"Show Full Table", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Table controls", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Showing", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rows out of", None))
        self.label_totalRows.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export ALL rows to CSV", None))
    # retranslateUi

