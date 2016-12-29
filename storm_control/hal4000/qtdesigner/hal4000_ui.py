# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hal4000.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 676)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(10000, 10000))
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../HAL-4000.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(10000, 10000))
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, -1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.paramsWidget = QtWidgets.QWidget(self.centralwidget)
        self.paramsWidget.setMinimumSize(QtCore.QSize(210, 0))
        self.paramsWidget.setMaximumSize(QtCore.QSize(210, 16777215))
        self.paramsWidget.setObjectName("paramsWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.paramsWidget)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsGroupBox = QtWidgets.QGroupBox(self.paramsWidget)
        self.settingsGroupBox.setMinimumSize(QtCore.QSize(50, 40))
        self.settingsGroupBox.setObjectName("settingsGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout_5.setContentsMargins(2, 2, 2, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.settingsScrollArea = QtWidgets.QScrollArea(self.settingsGroupBox)
        self.settingsScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settingsScrollArea.setWidgetResizable(True)
        self.settingsScrollArea.setObjectName("settingsScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 194, 141))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.settingsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.settingsScrollArea)
        self.verticalLayout_4.addWidget(self.settingsGroupBox)
        self.filmGroupBox = QtWidgets.QGroupBox(self.paramsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filmGroupBox.sizePolicy().hasHeightForWidth())
        self.filmGroupBox.setSizePolicy(sizePolicy)
        self.filmGroupBox.setMinimumSize(QtCore.QSize(150, 261))
        self.filmGroupBox.setObjectName("filmGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.filmGroupBox)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, -1)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shuttersLabels = QtWidgets.QLabel(self.filmGroupBox)
        self.shuttersLabels.setObjectName("shuttersLabels")
        self.verticalLayout_2.addWidget(self.shuttersLabels)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget = QtWidgets.QWidget(self.filmGroupBox)
        self.widget.setMaximumSize(QtCore.QSize(5, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout_9.addWidget(self.widget)
        self.shuttersText = QtWidgets.QLabel(self.filmGroupBox)
        self.shuttersText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shuttersText.setObjectName("shuttersText")
        self.horizontalLayout_9.addWidget(self.shuttersText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.directoryLabel = QtWidgets.QLabel(self.filmGroupBox)
        self.directoryLabel.setObjectName("directoryLabel")
        self.verticalLayout_2.addWidget(self.directoryLabel)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget_2 = QtWidgets.QWidget(self.filmGroupBox)
        self.widget_2.setMaximumSize(QtCore.QSize(5, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_10.addWidget(self.widget_2)
        self.directoryText = QtWidgets.QLabel(self.filmGroupBox)
        self.directoryText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.directoryText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.directoryText.setObjectName("directoryText")
        self.horizontalLayout_10.addWidget(self.directoryText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.autoIncCheckBox = QtWidgets.QCheckBox(self.filmGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoIncCheckBox.sizePolicy().hasHeightForWidth())
        self.autoIncCheckBox.setSizePolicy(sizePolicy)
        self.autoIncCheckBox.setChecked(True)
        self.autoIncCheckBox.setObjectName("autoIncCheckBox")
        self.verticalLayout_2.addWidget(self.autoIncCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filenameEdit = QtWidgets.QLineEdit(self.filmGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameEdit.sizePolicy().hasHeightForWidth())
        self.filenameEdit.setSizePolicy(sizePolicy)
        self.filenameEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.filenameEdit.setObjectName("filenameEdit")
        self.horizontalLayout.addWidget(self.filenameEdit)
        self.indexSpinBox = QtWidgets.QSpinBox(self.filmGroupBox)
        self.indexSpinBox.setMaximumSize(QtCore.QSize(55, 16777215))
        self.indexSpinBox.setMinimum(1)
        self.indexSpinBox.setMaximum(9999)
        self.indexSpinBox.setObjectName("indexSpinBox")
        self.horizontalLayout.addWidget(self.indexSpinBox)
        self.extensionComboBox = QtWidgets.QComboBox(self.filmGroupBox)
        self.extensionComboBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.extensionComboBox.setObjectName("extensionComboBox")
        self.horizontalLayout.addWidget(self.extensionComboBox)
        self.filetypeComboBox = QtWidgets.QComboBox(self.filmGroupBox)
        self.filetypeComboBox.setMaximumSize(QtCore.QSize(45, 16777215))
        self.filetypeComboBox.setObjectName("filetypeComboBox")
        self.horizontalLayout.addWidget(self.filetypeComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_3 = QtWidgets.QWidget(self.filmGroupBox)
        self.widget_3.setMaximumSize(QtCore.QSize(5, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_11.addWidget(self.widget_3)
        self.filenameLabel = QtWidgets.QLabel(self.filmGroupBox)
        self.filenameLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filenameLabel.setObjectName("filenameLabel")
        self.horizontalLayout_11.addWidget(self.filenameLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.modeLabel = QtWidgets.QLabel(self.filmGroupBox)
        self.modeLabel.setObjectName("modeLabel")
        self.horizontalLayout_4.addWidget(self.modeLabel)
        self.modeComboBox = QtWidgets.QComboBox(self.filmGroupBox)
        self.modeComboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.modeComboBox.setObjectName("modeComboBox")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.modeComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lengthLabel = QtWidgets.QLabel(self.filmGroupBox)
        self.lengthLabel.setObjectName("lengthLabel")
        self.horizontalLayout_5.addWidget(self.lengthLabel)
        self.lengthSpinBox = QtWidgets.QSpinBox(self.filmGroupBox)
        self.lengthSpinBox.setMaximum(1000000)
        self.lengthSpinBox.setObjectName("lengthSpinBox")
        self.horizontalLayout_5.addWidget(self.lengthSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.framesLabel = QtWidgets.QLabel(self.filmGroupBox)
        self.framesLabel.setObjectName("framesLabel")
        self.horizontalLayout_6.addWidget(self.framesLabel)
        self.framesText = QtWidgets.QLabel(self.filmGroupBox)
        self.framesText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.framesText.setObjectName("framesText")
        self.horizontalLayout_6.addWidget(self.framesText)
        self.sizeLabel = QtWidgets.QLabel(self.filmGroupBox)
        self.sizeLabel.setObjectName("sizeLabel")
        self.horizontalLayout_6.addWidget(self.sizeLabel)
        self.sizeText = QtWidgets.QLabel(self.filmGroupBox)
        self.sizeText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sizeText.setObjectName("sizeText")
        self.horizontalLayout_6.addWidget(self.sizeText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.autoShuttersCheckBox = QtWidgets.QCheckBox(self.filmGroupBox)
        self.autoShuttersCheckBox.setChecked(True)
        self.autoShuttersCheckBox.setObjectName("autoShuttersCheckBox")
        self.horizontalLayout_7.addWidget(self.autoShuttersCheckBox)
        self.saveMovieCheckBox = QtWidgets.QCheckBox(self.filmGroupBox)
        self.saveMovieCheckBox.setChecked(True)
        self.saveMovieCheckBox.setObjectName("saveMovieCheckBox")
        self.horizontalLayout_7.addWidget(self.saveMovieCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.filmGroupBox)
        self.cameraParamsFrame = QtWidgets.QFrame(self.paramsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraParamsFrame.sizePolicy().hasHeightForWidth())
        self.cameraParamsFrame.setSizePolicy(sizePolicy)
        self.cameraParamsFrame.setMinimumSize(QtCore.QSize(50, 50))
        self.cameraParamsFrame.setMaximumSize(QtCore.QSize(1000, 151))
        self.cameraParamsFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cameraParamsFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cameraParamsFrame.setObjectName("cameraParamsFrame")
        self.verticalLayout_4.addWidget(self.cameraParamsFrame)
        self.liveModeGroupBox = QtWidgets.QGroupBox(self.paramsWidget)
        self.liveModeGroupBox.setObjectName("liveModeGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.liveModeGroupBox)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.liveModeCheckBox = QtWidgets.QCheckBox(self.liveModeGroupBox)
        self.liveModeCheckBox.setChecked(True)
        self.liveModeCheckBox.setObjectName("liveModeCheckBox")
        self.horizontalLayout_8.addWidget(self.liveModeCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4.addWidget(self.liveModeGroupBox)
        self.mosaicGroupBox_2 = QtWidgets.QGroupBox(self.paramsWidget)
        self.mosaicGroupBox_2.setObjectName("mosaicGroupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.mosaicGroupBox_2)
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.objectiveLabel = QtWidgets.QLabel(self.mosaicGroupBox_2)
        self.objectiveLabel.setObjectName("objectiveLabel")
        self.horizontalLayout_12.addWidget(self.objectiveLabel)
        self.objectiveText = QtWidgets.QLabel(self.mosaicGroupBox_2)
        self.objectiveText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.objectiveText.setObjectName("objectiveText")
        self.horizontalLayout_12.addWidget(self.objectiveText)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4.addWidget(self.mosaicGroupBox_2)
        self.horizontalLayout_2.addWidget(self.paramsWidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cameraFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraFrame.sizePolicy().hasHeightForWidth())
        self.cameraFrame.setSizePolicy(sizePolicy)
        self.cameraFrame.setMinimumSize(QtCore.QSize(588, 540))
        self.cameraFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cameraFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cameraFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cameraFrame.setObjectName("cameraFrame")
        self.verticalLayout_3.addWidget(self.cameraFrame)
        self.notesGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesGroupBox.sizePolicy().hasHeightForWidth())
        self.notesGroupBox.setSizePolicy(sizePolicy)
        self.notesGroupBox.setMinimumSize(QtCore.QSize(0, 70))
        self.notesGroupBox.setMaximumSize(QtCore.QSize(16777215, 140))
        self.notesGroupBox.setObjectName("notesGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.notesGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.notesEdit = QtWidgets.QTextEdit(self.notesGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notesEdit.sizePolicy().hasHeightForWidth())
        self.notesEdit.setSizePolicy(sizePolicy)
        self.notesEdit.setMinimumSize(QtCore.QSize(20, 37))
        self.notesEdit.setMaximumSize(QtCore.QSize(10000, 10000))
        self.notesEdit.setObjectName("notesEdit")
        self.horizontalLayout_3.addWidget(self.notesEdit)
        self.verticalLayout_3.addWidget(self.notesGroupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionShutter = QtWidgets.QAction(MainWindow)
        self.actionShutter.setObjectName("actionShutter")
        self.actionDirectory = QtWidgets.QAction(MainWindow)
        self.actionDirectory.setObjectName("actionDirectory")
        self.actionIllumination = QtWidgets.QAction(MainWindow)
        self.actionIllumination.setObjectName("actionIllumination")
        self.actionStage = QtWidgets.QAction(MainWindow)
        self.actionStage.setObjectName("actionStage")
        self.actionFocus_Lock = QtWidgets.QAction(MainWindow)
        self.actionFocus_Lock.setObjectName("actionFocus_Lock")
        self.actionSpot_Counter = QtWidgets.QAction(MainWindow)
        self.actionSpot_Counter.setObjectName("actionSpot_Counter")
        self.actionSwitch_Test = QtWidgets.QAction(MainWindow)
        self.actionSwitch_Test.setObjectName("actionSwitch_Test")
        self.actionMisc_Controls = QtWidgets.QAction(MainWindow)
        self.actionMisc_Controls.setObjectName("actionMisc_Controls")
        self.actionProgression = QtWidgets.QAction(MainWindow)
        self.actionProgression.setObjectName("actionProgression")
        self.actionDisconnect = QtWidgets.QAction(MainWindow)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionShutter)
        self.menuFile.addAction(self.actionDirectory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HAL-4000"))
        self.settingsGroupBox.setTitle(_translate("MainWindow", "Settings"))
        self.filmGroupBox.setTitle(_translate("MainWindow", "Film"))
        self.shuttersLabels.setText(_translate("MainWindow", "Shutter Sequence:"))
        self.shuttersText.setText(_translate("MainWindow", "asdf"))
        self.directoryLabel.setText(_translate("MainWindow", "Directory:"))
        self.directoryText.setText(_translate("MainWindow", "asdf"))
        self.autoIncCheckBox.setText(_translate("MainWindow", "Increment Automatically"))
        self.filenameLabel.setText(_translate("MainWindow", "asdf"))
        self.modeLabel.setText(_translate("MainWindow", "Mode:"))
        self.modeComboBox.setItemText(0, _translate("MainWindow", "Run Till Abort"))
        self.modeComboBox.setItemText(1, _translate("MainWindow", "Fixed Length"))
        self.lengthLabel.setText(_translate("MainWindow", "Length:"))
        self.framesLabel.setText(_translate("MainWindow", "Frames:"))
        self.framesText.setText(_translate("MainWindow", "asdf"))
        self.sizeLabel.setText(_translate("MainWindow", "Size:"))
        self.sizeText.setText(_translate("MainWindow", "asdf"))
        self.autoShuttersCheckBox.setText(_translate("MainWindow", "Run Shutters"))
        self.saveMovieCheckBox.setText(_translate("MainWindow", "Save Movie"))
        self.liveModeGroupBox.setTitle(_translate("MainWindow", "Live Mode"))
        self.liveModeCheckBox.setText(_translate("MainWindow", "Run Live Mode"))
        self.mosaicGroupBox_2.setTitle(_translate("MainWindow", "Mosaic"))
        self.objectiveLabel.setText(_translate("MainWindow", "Objective:"))
        self.objectiveText.setText(_translate("MainWindow", "asdf"))
        self.notesGroupBox.setTitle(_translate("MainWindow", "Notes"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionSettings.setText(_translate("MainWindow", "New Settings"))
        self.actionShutter.setText(_translate("MainWindow", "New Shutter Sequence"))
        self.actionDirectory.setText(_translate("MainWindow", "Set Working Directory"))
        self.actionIllumination.setText(_translate("MainWindow", "Illumination"))
        self.actionStage.setText(_translate("MainWindow", "Stage"))
        self.actionFocus_Lock.setText(_translate("MainWindow", "Focus Lock"))
        self.actionSpot_Counter.setText(_translate("MainWindow", "Spot Counter"))
        self.actionSwitch_Test.setText(_translate("MainWindow", "Switch Test"))
        self.actionMisc_Controls.setText(_translate("MainWindow", "Misc. Controls"))
        self.actionProgression.setText(_translate("MainWindow", "Progressions"))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect"))

