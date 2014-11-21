# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './rsrc/orQanon.ui'
#
# Created: Sat Nov 22 00:25:59 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(975, 637)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.verticalSlider_6 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_6.setStyleSheet("QSlider::groove:vertical {\n"
"background: white;\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: white;\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_6.setMaximum(8)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setInvertedAppearance(True)
        self.verticalSlider_6.setInvertedControls(False)
        self.verticalSlider_6.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_6.setTickInterval(1)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.gridLayout.addWidget(self.verticalSlider_6, 0, 5, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_4.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_4.setLineWidth(1)
        self.lcdNumber_4.setDigitCount(1)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 1, 3, 1, 1)
        self.verticalSlider_4 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_4.setStyleSheet("QSlider::groove:vertical {\n"
"background: white;\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: white;\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_4.setMaximum(8)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setInvertedAppearance(True)
        self.verticalSlider_4.setInvertedControls(False)
        self.verticalSlider_4.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_4.setTickInterval(1)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.gridLayout.addWidget(self.verticalSlider_4, 0, 3, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_3.setLineWidth(1)
        self.lcdNumber_3.setDigitCount(1)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 1, 2, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_2.setLineWidth(1)
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 6, 1, 1)
        self.verticalSlider_8 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_8.setStyleSheet("QSlider::groove:vertical {\n"
"background: rgb(51, 51, 51);\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: rgb(51, 51, 51);\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_8.setMaximum(8)
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setInvertedAppearance(True)
        self.verticalSlider_8.setInvertedControls(False)
        self.verticalSlider_8.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_8.setTickInterval(1)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.gridLayout.addWidget(self.verticalSlider_8, 0, 7, 1, 1)
        self.verticalSlider_3 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_3.setStyleSheet("QSlider::groove:vertical {\n"
"background: white;\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: white;\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_3.setMaximum(8)
        self.verticalSlider_3.setProperty("value", 8)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setInvertedAppearance(True)
        self.verticalSlider_3.setInvertedControls(False)
        self.verticalSlider_3.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_3.setTickInterval(1)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.gridLayout.addWidget(self.verticalSlider_3, 0, 2, 1, 1)
        self.verticalSlider_7 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_7.setStyleSheet("QSlider::groove:vertical {\n"
"background: rgb(51, 51, 51);\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: rgb(51, 51, 51);\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_7.setMaximum(8)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setInvertedAppearance(True)
        self.verticalSlider_7.setInvertedControls(False)
        self.verticalSlider_7.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_7.setTickInterval(1)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.gridLayout.addWidget(self.verticalSlider_7, 0, 6, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 7, 1, 1)
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_7.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_7.setLineWidth(1)
        self.lcdNumber_7.setDigitCount(1)
        self.lcdNumber_7.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.gridLayout.addWidget(self.lcdNumber_7, 1, 6, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 2, 0, 1, 1)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_5.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_5.setLineWidth(1)
        self.lcdNumber_5.setDigitCount(1)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout.addWidget(self.lcdNumber_5, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 4, 1, 1)
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_8.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_8.setLineWidth(1)
        self.lcdNumber_8.setDigitCount(1)
        self.lcdNumber_8.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.gridLayout.addWidget(self.lcdNumber_8, 1, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 5, 1, 1)
        self.verticalSlider_5 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_5.setStyleSheet("QSlider::groove:vertical {\n"
"background: rgb(51, 51, 51);\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: rgb(51, 51, 51);\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_5.setMaximum(8)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setInvertedAppearance(True)
        self.verticalSlider_5.setInvertedControls(False)
        self.verticalSlider_5.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_5.setTickInterval(1)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.gridLayout.addWidget(self.verticalSlider_5, 0, 4, 1, 1)
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_1.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_1.setLineWidth(1)
        self.lcdNumber_1.setDigitCount(1)
        self.lcdNumber_1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.gridLayout.addWidget(self.lcdNumber_1, 1, 0, 1, 1)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lcdNumber_6.setFont(font)
        self.lcdNumber_6.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_6.setLineWidth(1)
        self.lcdNumber_6.setDigitCount(1)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.gridLayout.addWidget(self.lcdNumber_6, 1, 5, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_2.setStyleSheet("QSlider::groove:vertical {\n"
"background: rgb(128, 0, 0);\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: rgb(128, 0, 0);\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_2.setMaximum(8)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setInvertedAppearance(True)
        self.verticalSlider_2.setInvertedControls(False)
        self.verticalSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_2.setTickInterval(1)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout.addWidget(self.verticalSlider_2, 0, 1, 1, 1)
        self.verticalSlider_1 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_1.setStyleSheet("QSlider::groove:vertical {\n"
"background: rgb(128, 0, 0);\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: rgb(128, 0, 0);\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_1.setMaximum(8)
        self.verticalSlider_1.setSingleStep(1)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setInvertedAppearance(True)
        self.verticalSlider_1.setInvertedControls(False)
        self.verticalSlider_1.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_1.setTickInterval(1)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.gridLayout.addWidget(self.verticalSlider_1, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 8, 1, 1)
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdNumber_9.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_9.setLineWidth(1)
        self.lcdNumber_9.setDigitCount(1)
        self.lcdNumber_9.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.gridLayout.addWidget(self.lcdNumber_9, 1, 8, 1, 1)
        self.verticalSlider_9 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_9.setStyleSheet("QSlider::groove:vertical {\n"
"background: white;\n"
"position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"left: 4px; right: 4px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"height: 10px;\n"
"background: white;\n"
"margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"QSlider::add-page:vertical {\n"
"background: rgb(230, 230, 230);\n"
"}\n"
"/*\n"
"QSlider::sub-page:vertical {\n"
"background: white;\n"
"}\n"
"*/")
        self.verticalSlider_9.setMaximum(8)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setInvertedAppearance(True)
        self.verticalSlider_9.setInvertedControls(False)
        self.verticalSlider_9.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.verticalSlider_9.setTickInterval(1)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.gridLayout.addWidget(self.verticalSlider_9, 0, 8, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMaximum(5000.0)
        self.doubleSpinBox_2.setProperty("value", 440.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_7.addWidget(self.doubleSpinBox_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_7.addWidget(self.comboBox, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox.setMaximum(8)
        self.spinBox.setProperty("value", 4)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_7.addWidget(self.spinBox, 0, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_6)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_1.setChecked(False)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout_9.addWidget(self.radioButton_1, 1, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_9.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_9.addWidget(self.radioButton_3, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_1.setMinimum(0.1)
        self.doubleSpinBox_1.setMaximum(5.0)
        self.doubleSpinBox_1.setSingleStep(0.1)
        self.doubleSpinBox_1.setProperty("value", 0.5)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.gridLayout_4.addWidget(self.doubleSpinBox_1, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 2, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_synth = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_synth.setObjectName("pushButton_synth")
        self.verticalLayout_6.addWidget(self.pushButton_synth)
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.verticalLayout_6.addWidget(self.pushButton_reset)
        self.verticalLayout_5.addWidget(self.groupBox_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_6.setSpacing(-1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_str11 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str11.sizePolicy().hasHeightForWidth())
        self.pushButton_str11.setSizePolicy(sizePolicy)
        self.pushButton_str11.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str11.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str11.setText("")
        self.pushButton_str11.setObjectName("pushButton_str11")
        self.gridLayout_6.addWidget(self.pushButton_str11, 0, 2, 1, 1)
        self.pushButton_str12 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str12.sizePolicy().hasHeightForWidth())
        self.pushButton_str12.setSizePolicy(sizePolicy)
        self.pushButton_str12.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str12.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str12.setStyleSheet("background-color:rgb(0, 128, 0)")
        self.pushButton_str12.setText("")
        self.pushButton_str12.setObjectName("pushButton_str12")
        self.gridLayout_6.addWidget(self.pushButton_str12, 0, 3, 1, 1)
        self.pushButton_str31 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str31.sizePolicy().hasHeightForWidth())
        self.pushButton_str31.setSizePolicy(sizePolicy)
        self.pushButton_str31.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str31.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str31.setText("")
        self.pushButton_str31.setObjectName("pushButton_str31")
        self.gridLayout_6.addWidget(self.pushButton_str31, 2, 2, 1, 1)
        self.pushButton_str22 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str22.sizePolicy().hasHeightForWidth())
        self.pushButton_str22.setSizePolicy(sizePolicy)
        self.pushButton_str22.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str22.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str22.setText("")
        self.pushButton_str22.setObjectName("pushButton_str22")
        self.gridLayout_6.addWidget(self.pushButton_str22, 1, 3, 1, 1)
        self.pushButton_str21 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str21.sizePolicy().hasHeightForWidth())
        self.pushButton_str21.setSizePolicy(sizePolicy)
        self.pushButton_str21.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str21.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str21.setText("")
        self.pushButton_str21.setObjectName("pushButton_str21")
        self.gridLayout_6.addWidget(self.pushButton_str21, 1, 2, 1, 1)
        self.pushButton_str13 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str13.sizePolicy().hasHeightForWidth())
        self.pushButton_str13.setSizePolicy(sizePolicy)
        self.pushButton_str13.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str13.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str13.setText("")
        self.pushButton_str13.setObjectName("pushButton_str13")
        self.gridLayout_6.addWidget(self.pushButton_str13, 0, 4, 1, 1)
        self.pushButton_str33 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str33.sizePolicy().hasHeightForWidth())
        self.pushButton_str33.setSizePolicy(sizePolicy)
        self.pushButton_str33.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str33.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str33.setText("")
        self.pushButton_str33.setObjectName("pushButton_str33")
        self.gridLayout_6.addWidget(self.pushButton_str33, 2, 4, 1, 1)
        self.pushButton_str32 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str32.sizePolicy().hasHeightForWidth())
        self.pushButton_str32.setSizePolicy(sizePolicy)
        self.pushButton_str32.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str32.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str32.setText("")
        self.pushButton_str32.setObjectName("pushButton_str32")
        self.gridLayout_6.addWidget(self.pushButton_str32, 2, 3, 1, 1)
        self.pushButton_str23 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str23.sizePolicy().hasHeightForWidth())
        self.pushButton_str23.setSizePolicy(sizePolicy)
        self.pushButton_str23.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str23.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str23.setText("")
        self.pushButton_str23.setObjectName("pushButton_str23")
        self.gridLayout_6.addWidget(self.pushButton_str23, 1, 4, 1, 1)
        self.pushButton_str41 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str41.sizePolicy().hasHeightForWidth())
        self.pushButton_str41.setSizePolicy(sizePolicy)
        self.pushButton_str41.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str41.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str41.setText("")
        self.pushButton_str41.setObjectName("pushButton_str41")
        self.gridLayout_6.addWidget(self.pushButton_str41, 3, 2, 1, 1)
        self.pushButton_str42 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str42.sizePolicy().hasHeightForWidth())
        self.pushButton_str42.setSizePolicy(sizePolicy)
        self.pushButton_str42.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str42.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str42.setText("")
        self.pushButton_str42.setObjectName("pushButton_str42")
        self.gridLayout_6.addWidget(self.pushButton_str42, 3, 3, 1, 1)
        self.pushButton_str43 = QtWidgets.QPushButton(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_str43.sizePolicy().hasHeightForWidth())
        self.pushButton_str43.setSizePolicy(sizePolicy)
        self.pushButton_str43.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_str43.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_str43.setText("")
        self.pushButton_str43.setObjectName("pushButton_str43")
        self.gridLayout_6.addWidget(self.pushButton_str43, 3, 4, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_1.setCheckable(True)
        self.pushButton_1.setChecked(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_3.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_3.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_3.addWidget(self.pushButton_13)
        self.verticalLayout_2.addWidget(self.groupBox)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        self.actionExit.triggered.connect(mainWindow.close)
        self.verticalSlider_1.valueChanged['int'].connect(self.lcdNumber_1.display)
        self.verticalSlider_6.valueChanged['int'].connect(self.lcdNumber_6.display)
        self.verticalSlider_7.valueChanged['int'].connect(self.lcdNumber_7.display)
        self.verticalSlider_8.valueChanged['int'].connect(self.lcdNumber_8.display)
        self.verticalSlider_5.valueChanged['int'].connect(self.lcdNumber_5.display)
        self.verticalSlider_3.valueChanged['int'].connect(self.lcdNumber_3.display)
        self.verticalSlider_4.valueChanged['int'].connect(self.lcdNumber_4.display)
        self.verticalSlider_2.valueChanged['int'].connect(self.lcdNumber_2.display)
        self.verticalSlider_9.valueChanged['int'].connect(self.lcdNumber_9.display)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "orQanon"))
        self.groupBox_2.setTitle(_translate("mainWindow", "Draw Bars"))
        self.label_2.setText(_translate("mainWindow", "5 1/3\'"))
        self.label_7.setText(_translate("mainWindow", "1 3/5\'"))
        self.label_8.setText(_translate("mainWindow", "1 1/3\'"))
        self.label_1.setText(_translate("mainWindow", "16\'"))
        self.label_4.setText(_translate("mainWindow", "4\'"))
        self.label_5.setText(_translate("mainWindow", "2 2/3\'"))
        self.label_3.setText(_translate("mainWindow", "8\'"))
        self.label_6.setText(_translate("mainWindow", "2\'"))
        self.label_9.setText(_translate("mainWindow", "1\'"))
        self.groupBox_6.setTitle(_translate("mainWindow", "Tonic (Piano Key)"))
        self.label.setText(_translate("mainWindow", "Tuning Fork [Hz]"))
        self.groupBox_4.setTitle(_translate("mainWindow", "12 Tone Interval Ratios"))
        self.radioButton_1.setText(_translate("mainWindow", "Pythagorean"))
        self.radioButton_2.setText(_translate("mainWindow", "Tempered"))
        self.radioButton_3.setText(_translate("mainWindow", "Just"))
        self.groupBox_5.setTitle(_translate("mainWindow", "Tone"))
        self.label_10.setText(_translate("mainWindow", "Duration [s]"))
        self.checkBox.setText(_translate("mainWindow", "ADSR"))
        self.groupBox_8.setTitle(_translate("mainWindow", "Misc"))
        self.pushButton_synth.setText(_translate("mainWindow", "Synth"))
        self.pushButton_reset.setText(_translate("mainWindow", "Reset"))
        self.groupBox_7.setTitle(_translate("mainWindow", "Stradella"))
        self.groupBox_3.setTitle(_translate("mainWindow", "Hilbert Plot"))
        self.groupBox.setTitle(_translate("mainWindow", "Chord Intervals"))
        self.pushButton_1.setText(_translate("mainWindow", "P1"))
        self.pushButton_2.setText(_translate("mainWindow", "m2"))
        self.pushButton_3.setText(_translate("mainWindow", "M2"))
        self.pushButton_4.setText(_translate("mainWindow", "m3"))
        self.pushButton_5.setText(_translate("mainWindow", "M3"))
        self.pushButton_6.setText(_translate("mainWindow", "P4"))
        self.pushButton_7.setText(_translate("mainWindow", "d5"))
        self.pushButton_8.setText(_translate("mainWindow", "P5"))
        self.pushButton_9.setText(_translate("mainWindow", "m6"))
        self.pushButton_10.setText(_translate("mainWindow", "M6"))
        self.pushButton_11.setText(_translate("mainWindow", "m7"))
        self.pushButton_12.setText(_translate("mainWindow", "M7"))
        self.pushButton_13.setText(_translate("mainWindow", "P8"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
        self.actionAbout.setText(_translate("mainWindow", "About"))

