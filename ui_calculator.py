# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatorvfKKNI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(336, 534)
        MainWindow.setMinimumSize(QSize(336, 534))
        MainWindow.setStyleSheet(u"QPushButton{	\n"
"	color:rgb(225,84,171);\n"
"	background-color:rgb(92,35,225);\n"
"	border-radius:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color:rgb(62,176,240);\n"
"	background-color:rgb(167,33,204);\n"
"}\n"
"\n"
"QMainWindow{\n"
"	background-color:rgb(16, 24, 32);\n"
"}\n"
"\n"
"QPushButton#sum,#sub,#equal,#division,#multiple{	\n"
"	color:rgb(255,255,255);\n"
"	background-color:rgb(169,250,47);\n"
"	border-radius:30px;\n"
"}\n"
"\n"
"QPushButton#sum:hover,#sub:hover,#equal:hover,#division:hover,#multiple:hover{\n"
"	color:rgb(255,255,255);\n"
"	background-color:rgb(204,198,37);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_6 = QPushButton(self.centralwidget)
        self.button_6.setObjectName(u"button_6")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.button_6.setFont(font)

        self.gridLayout.addWidget(self.button_6, 3, 2, 1, 1)

        self.button_4 = QPushButton(self.centralwidget)
        self.button_4.setObjectName(u"button_4")
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setFont(font)

        self.gridLayout.addWidget(self.button_4, 3, 0, 1, 1)

        self.button_3 = QPushButton(self.centralwidget)
        self.button_3.setObjectName(u"button_3")
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setFont(font)

        self.gridLayout.addWidget(self.button_3, 4, 2, 1, 1)

        self.point = QPushButton(self.centralwidget)
        self.point.setObjectName(u"point")
        sizePolicy.setHeightForWidth(self.point.sizePolicy().hasHeightForWidth())
        self.point.setSizePolicy(sizePolicy)
        self.point.setFont(font)

        self.gridLayout.addWidget(self.point, 5, 2, 1, 1)

        self.sum = QPushButton(self.centralwidget)
        self.sum.setObjectName(u"sum")
        sizePolicy.setHeightForWidth(self.sum.sizePolicy().hasHeightForWidth())
        self.sum.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setItalic(False)
        self.sum.setFont(font1)
        self.sum.setStyleSheet(u"")

        self.gridLayout.addWidget(self.sum, 1, 3, 1, 1)

        self.multiple = QPushButton(self.centralwidget)
        self.multiple.setObjectName(u"multiple")
        sizePolicy.setHeightForWidth(self.multiple.sizePolicy().hasHeightForWidth())
        self.multiple.setSizePolicy(sizePolicy)
        self.multiple.setFont(font1)

        self.gridLayout.addWidget(self.multiple, 3, 3, 1, 1)

        self.equal = QPushButton(self.centralwidget)
        self.equal.setObjectName(u"equal")
        sizePolicy.setHeightForWidth(self.equal.sizePolicy().hasHeightForWidth())
        self.equal.setSizePolicy(sizePolicy)
        self.equal.setFont(font1)

        self.gridLayout.addWidget(self.equal, 5, 3, 1, 1)

        self.sub = QPushButton(self.centralwidget)
        self.sub.setObjectName(u"sub")
        sizePolicy.setHeightForWidth(self.sub.sizePolicy().hasHeightForWidth())
        self.sub.setSizePolicy(sizePolicy)
        self.sub.setFont(font1)

        self.gridLayout.addWidget(self.sub, 2, 3, 1, 1)

        self.delete_2 = QPushButton(self.centralwidget)
        self.delete_2.setObjectName(u"delete_2")
        sizePolicy.setHeightForWidth(self.delete_2.sizePolicy().hasHeightForWidth())
        self.delete_2.setSizePolicy(sizePolicy)
        self.delete_2.setFont(font)

        self.gridLayout.addWidget(self.delete_2, 1, 2, 1, 1)

        self.button_8 = QPushButton(self.centralwidget)
        self.button_8.setObjectName(u"button_8")
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setFont(font)

        self.gridLayout.addWidget(self.button_8, 2, 1, 1, 1)

        self.division = QPushButton(self.centralwidget)
        self.division.setObjectName(u"division")
        sizePolicy.setHeightForWidth(self.division.sizePolicy().hasHeightForWidth())
        self.division.setSizePolicy(sizePolicy)
        self.division.setFont(font1)

        self.gridLayout.addWidget(self.division, 4, 3, 1, 1)

        self.button_9 = QPushButton(self.centralwidget)
        self.button_9.setObjectName(u"button_9")
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setFont(font)

        self.gridLayout.addWidget(self.button_9, 2, 2, 1, 1)

        self.button_2 = QPushButton(self.centralwidget)
        self.button_2.setObjectName(u"button_2")
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setFont(font)

        self.gridLayout.addWidget(self.button_2, 4, 1, 1, 1)

        self.button_1 = QPushButton(self.centralwidget)
        self.button_1.setObjectName(u"button_1")
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setFont(font)

        self.gridLayout.addWidget(self.button_1, 4, 0, 1, 1)

        self.button_5 = QPushButton(self.centralwidget)
        self.button_5.setObjectName(u"button_5")
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setFont(font)

        self.gridLayout.addWidget(self.button_5, 3, 1, 1, 1)

        self.button_7 = QPushButton(self.centralwidget)
        self.button_7.setObjectName(u"button_7")
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setFont(font)

        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(14)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 700 28pt \"Segoe UI\";\n"
"color:rgb(255,255,255);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.clear = QPushButton(self.centralwidget)
        self.clear.setObjectName(u"clear")
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)
        self.clear.setFont(font)
        self.clear.setStyleSheet(u"")

        self.gridLayout.addWidget(self.clear, 1, 0, 1, 2)

        self.button_0 = QPushButton(self.centralwidget)
        self.button_0.setObjectName(u"button_0")
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setFont(font)

        self.gridLayout.addWidget(self.button_0, 5, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.sum.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.multiple.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"Del", None))
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.division.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label.setText("")
        self.clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

