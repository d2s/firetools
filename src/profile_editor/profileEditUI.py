# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fj1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 30, 181, 509))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.capsDropLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.capsDropLabel.setObjectName("capsDropLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.capsDropLabel)
        self.capsDropSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.capsDropSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.capsDropSlider.setMaximum(1)
        self.capsDropSlider.setPageStep(1)
        self.capsDropSlider.setTracking(False)
        self.capsDropSlider.setOrientation(QtCore.Qt.Horizontal)
        self.capsDropSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.capsDropSlider.setObjectName("capsDropSlider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.capsDropSlider)
        self.ipcLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ipcLabel.setObjectName("ipcLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ipcLabel)
        self.ipcSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.ipcSlider.setMaximum(1)
        self.ipcSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ipcSlider.setObjectName("ipcSlider")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ipcSlider)
        self.netfilterLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.netfilterLabel.setObjectName("netfilterLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.netfilterLabel)
        self.netfilterSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.netfilterSlider.setMaximum(1)
        self.netfilterSlider.setOrientation(QtCore.Qt.Horizontal)
        self.netfilterSlider.setObjectName("netfilterSlider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.netfilterSlider)
        self.machineIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.machineIDLabel.setObjectName("machineIDLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.machineIDLabel)
        self.machineIDSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.machineIDSlider.setMaximum(1)
        self.machineIDSlider.setOrientation(QtCore.Qt.Horizontal)
        self.machineIDSlider.setObjectName("machineIDSlider")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.machineIDSlider)
        self.nodvdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nodvdLabel.setObjectName("nodvdLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.nodvdLabel)
        self.nodvdSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.nodvdSlider.setMaximum(1)
        self.nodvdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nodvdSlider.setObjectName("nodvdSlider")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.nodvdSlider)
        self.nomountLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nomountLabel.setObjectName("nomountLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.nomountLabel)
        self.nomountSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.nomountSlider.setMaximum(1)
        self.nomountSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nomountSlider.setObjectName("nomountSlider")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.nomountSlider)
        self.notvLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.notvLabel.setObjectName("notvLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.notvLabel)
        self.notvSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.notvSlider.setMaximum(1)
        self.notvSlider.setOrientation(QtCore.Qt.Horizontal)
        self.notvSlider.setObjectName("notvSlider")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.notvSlider)
        self.nosoundLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nosoundLabel.setObjectName("nosoundLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.nosoundLabel)
        self.nosoundSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.nosoundSlider.setMaximum(1)
        self.nosoundSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nosoundSlider.setObjectName("nosoundSlider")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.nosoundSlider)
        self.novideoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.novideoLabel.setObjectName("novideoLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.novideoLabel)
        self.novideoSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.novideoSlider.setMaximum(1)
        self.novideoSlider.setOrientation(QtCore.Qt.Horizontal)
        self.novideoSlider.setObjectName("novideoSlider")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.novideoSlider)
        self.nogroupsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nogroupsLabel.setObjectName("nogroupsLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.nogroupsLabel)
        self.nogroupsSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.nogroupsSlider.setMaximum(1)
        self.nogroupsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nogroupsSlider.setObjectName("nogroupsSlider")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.nogroupsSlider)
        self.nonewprivsLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nonewprivsLabel.setObjectName("nonewprivsLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.nonewprivsLabel)
        self.nonewprivsSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.nonewprivsSlider.setMaximum(1)
        self.nonewprivsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nonewprivsSlider.setObjectName("nonewprivsSlider")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.nonewprivsSlider)
        self.norootLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.norootLabel.setObjectName("norootLabel")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.norootLabel)
        self.norootSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.norootSlider.setMaximum(1)
        self.norootSlider.setOrientation(QtCore.Qt.Horizontal)
        self.norootSlider.setObjectName("norootSlider")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.norootSlider)
        self.noshellLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.noshellLabel.setObjectName("noshellLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.noshellLabel)
        self.noshellSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.noshellSlider.setMaximum(1)
        self.noshellSlider.setOrientation(QtCore.Qt.Horizontal)
        self.noshellSlider.setObjectName("noshellSlider")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.noshellSlider)
        self.seccompLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.seccompLabel.setObjectName("seccompLabel")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.seccompLabel)
        self.seccompSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.seccompSlider.setMaximum(1)
        self.seccompSlider.setOrientation(QtCore.Qt.Horizontal)
        self.seccompSlider.setObjectName("seccompSlider")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.seccompSlider)
        self.mdweLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.mdweLabel.setObjectName("mdweLabel")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.mdweLabel)
        self.mdweSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.mdweSlider.setMaximum(1)
        self.mdweSlider.setOrientation(QtCore.Qt.Horizontal)
        self.mdweSlider.setObjectName("mdweSlider")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.mdweSlider)
        self.tracelogLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.tracelogLabel.setObjectName("tracelogLabel")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.tracelogLabel)
        self.tracelogSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.tracelogSlider.setMaximum(1)
        self.tracelogSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tracelogSlider.setObjectName("tracelogSlider")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.tracelogSlider)
        self.noexecHomeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.noexecHomeLabel.setObjectName("noexecHomeLabel")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.noexecHomeLabel)
        self.noexecHomeSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.noexecHomeSlider.setMaximum(1)
        self.noexecHomeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.noexecHomeSlider.setObjectName("noexecHomeSlider")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.noexecHomeSlider)
        self.noexecTmpLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.noexecTmpLabel.setObjectName("noexecTmpLabel")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.noexecTmpLabel)
        self.noexecTmpSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.noexecTmpSlider.setMaximum(1)
        self.noexecTmpSlider.setOrientation(QtCore.Qt.Horizontal)
        self.noexecTmpSlider.setObjectName("noexecTmpSlider")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.noexecTmpSlider)
        self.quietLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.quietLabel.setObjectName("quietLabel")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.quietLabel)
        self.quietSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.quietSlider.setMaximum(1)
        self.quietSlider.setOrientation(QtCore.Qt.Horizontal)
        self.quietSlider.setObjectName("quietSlider")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.quietSlider)
        self.genOptionsLabel = QtWidgets.QLabel(self.centralwidget)
        self.genOptionsLabel.setGeometry(QtCore.QRect(300, 10, 111, 17))
        self.genOptionsLabel.setObjectName("genOptionsLabel")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(630, 40, 161, 482))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.homeLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.homeLabel.setObjectName("homeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.homeLabel)
        self.horizontalSlider_24 = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_24.setMaximum(1)
        self.horizontalSlider_24.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_24.setObjectName("horizontalSlider_24")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_24)
        self.devLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.devLabel.setObjectName("devLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.devLabel)
        self.horizontalSlider_19 = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_19.setMaximum(1)
        self.horizontalSlider_19.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_19.setObjectName("horizontalSlider_19")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_19)
        self.tmpLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.tmpLabel.setObjectName("tmpLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.tmpLabel)
        self.horizontalSlider_20 = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_20.setMaximum(1)
        self.horizontalSlider_20.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_20.setObjectName("horizontalSlider_20")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_20)
        self.etcLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.etcLabel.setObjectName("etcLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.etcLabel)
        self.horizontalSlider_21 = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_21.setMaximum(1)
        self.horizontalSlider_21.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_21.setObjectName("horizontalSlider_21")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_21)
        self.etcBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.etcBrowser.setObjectName("etcBrowser")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.etcBrowser)
        self.binLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.binLabel.setObjectName("binLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.binLabel)
        self.horizontalSlider_23 = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_23.setMaximum(1)
        self.horizontalSlider_23.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_23.setObjectName("horizontalSlider_23")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_23)
        self.binBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.binBrowser.setObjectName("binBrowser")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.binBrowser)
        self.libLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.libLabel.setObjectName("libLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.libLabel)
        self.horizontalSlider_22 = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_22.setMaximum(1)
        self.horizontalSlider_22.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_22.setObjectName("horizontalSlider_22")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_22)
        self.libBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.libBrowser.setObjectName("libBrowser")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.libBrowser)
        self.optLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.optLabel.setObjectName("optLabel")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.optLabel)
        self.horizontalSlider_25 = QtWidgets.QSlider(self.formLayoutWidget_2)
        self.horizontalSlider_25.setMaximum(1)
        self.horizontalSlider_25.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_25.setObjectName("horizontalSlider_25")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_25)
        self.optBrowser = QtWidgets.QTextBrowser(self.formLayoutWidget_2)
        self.optBrowser.setObjectName("optBrowser")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.optBrowser)
        self.privateLabel = QtWidgets.QLabel(self.centralwidget)
        self.privateLabel.setGeometry(QtCore.QRect(660, 20, 121, 20))
        self.privateLabel.setObjectName("privateLabel")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(460, 260, 160, 80))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.x11Slider = QtWidgets.QSlider(self.formLayoutWidget_3)
        self.x11Slider.setMaximum(1)
        self.x11Slider.setPageStep(1)
        self.x11Slider.setOrientation(QtCore.Qt.Horizontal)
        self.x11Slider.setObjectName("x11Slider")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.x11Slider)
        self.xephyrButton = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.xephyrButton.setObjectName("xephyrButton")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.xephyrButton)
        self.xorgButton = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.xorgButton.setObjectName("xorgButton")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xorgButton)
        self.xpraButton = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.xpraButton.setObjectName("xpraButton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.xpraButton)
        self.xvfbButton = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.xvfbButton.setObjectName("xvfbButton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.xvfbButton)
        self.x11Label = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.x11Label.setObjectName("x11Label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.x11Label)
        self.graphicsLabel = QtWidgets.QLabel(self.centralwidget)
        self.graphicsLabel.setGeometry(QtCore.QRect(480, 240, 121, 20))
        self.graphicsLabel.setObjectName("graphicsLabel")
        self.auditProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.auditProgressBar.setGeometry(QtCore.QRect(460, 490, 118, 23))
        self.auditProgressBar.setProperty("value", 24)
        self.auditProgressBar.setObjectName("auditProgressBar")
        self.auditPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.auditPushButton.setGeometry(QtCore.QRect(470, 520, 101, 25))
        self.auditPushButton.setObjectName("auditPushButton")
        self.programListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.programListWidget.setGeometry(QtCore.QRect(10, 30, 211, 501))
        self.programListWidget.setObjectName("programListWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.capsDropLabel.setText(_translate("MainWindow", "Drop all capabilities"))
        self.ipcLabel.setText(_translate("MainWindow", "IPC restriction"))
        self.netfilterLabel.setText(_translate("MainWindow", "Network filter"))
        self.machineIDLabel.setText(_translate("MainWindow", "Random machine ID"))
        self.nodvdLabel.setText(_translate("MainWindow", "Hide DVDs"))
        self.nomountLabel.setText(_translate("MainWindow", "Hide external drives"))
        self.notvLabel.setText(_translate("MainWindow", "Hide TV devices"))
        self.nosoundLabel.setText(_translate("MainWindow", "No audio/microphone"))
        self.novideoLabel.setText(_translate("MainWindow", "No webcam"))
        self.nogroupsLabel.setText(_translate("MainWindow", "No groups"))
        self.nonewprivsLabel.setText(_translate("MainWindow", "No new privileges"))
        self.norootLabel.setText(_translate("MainWindow", "No root"))
        self.noshellLabel.setText(_translate("MainWindow", "No shell"))
        self.seccompLabel.setText(_translate("MainWindow", "Use seccomp filter"))
        self.mdweLabel.setText(_translate("MainWindow", "Hardened seccomp"))
        self.tracelogLabel.setText(_translate("MainWindow", "Log violation attempts"))
        self.noexecHomeLabel.setText(_translate("MainWindow", "Noexec home folder"))
        self.noexecTmpLabel.setText(_translate("MainWindow", "Noexec /tmp"))
        self.quietLabel.setText(_translate("MainWindow", "Disable output"))
        self.genOptionsLabel.setText(_translate("MainWindow", "General Options"))
        self.homeLabel.setText(_translate("MainWindow", "Private /home"))
        self.devLabel.setText(_translate("MainWindow", "Private /dev"))
        self.tmpLabel.setText(_translate("MainWindow", "Private /tmp"))
        self.etcLabel.setText(_translate("MainWindow", "Private /etc"))
        self.binLabel.setText(_translate("MainWindow", "Private /bin"))
        self.libLabel.setText(_translate("MainWindow", "Private /lib"))
        self.optLabel.setText(_translate("MainWindow", "Private /opt"))
        self.privateLabel.setText(_translate("MainWindow", "Private Filesystem"))
        self.xephyrButton.setText(_translate("MainWindow", "xephyr"))
        self.xorgButton.setText(_translate("MainWindow", "xorg"))
        self.xpraButton.setText(_translate("MainWindow", "xpra"))
        self.xvfbButton.setText(_translate("MainWindow", "xvfb"))
        self.x11Label.setText(_translate("MainWindow", "X11 Isolation"))
        self.graphicsLabel.setText(_translate("MainWindow", "Graphics Sandbox"))
        self.auditPushButton.setText(_translate("MainWindow", "Audit Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

