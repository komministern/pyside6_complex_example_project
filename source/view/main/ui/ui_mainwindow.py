# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from ...main.widgets.mycalendarwidget import MyCalendarWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(921, 636)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.calendarWidget = MyCalendarWidget(self.groupBox_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textEdit_Post = QTextEdit(self.groupBox_4)
        self.textEdit_Post.setObjectName(u"textEdit_Post")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.textEdit_Post.sizePolicy().hasHeightForWidth())
        self.textEdit_Post.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.textEdit_Post, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(158, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pushButton_Commit = QPushButton(self.groupBox_4)
        self.pushButton_Commit.setObjectName(u"pushButton_Commit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_Commit.sizePolicy().hasHeightForWidth())
        self.pushButton_Commit.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.pushButton_Commit, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(158, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_4, 0, 1, 5, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy6)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_LoadDB = QPushButton(self.groupBox)
        self.pushButton_LoadDB.setObjectName(u"pushButton_LoadDB")

        self.horizontalLayout.addWidget(self.pushButton_LoadDB)

        self.pushButton_SaveDB = QPushButton(self.groupBox)
        self.pushButton_SaveDB.setObjectName(u"pushButton_SaveDB")

        self.horizontalLayout.addWidget(self.pushButton_SaveDB)


        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy6.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy6)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_NumberOfPosts = QLabel(self.groupBox_2)
        self.label_NumberOfPosts.setObjectName(u"label_NumberOfPosts")
        sizePolicy6.setHeightForWidth(self.label_NumberOfPosts.sizePolicy().hasHeightForWidth())
        self.label_NumberOfPosts.setSizePolicy(sizePolicy6)
        self.label_NumberOfPosts.setMinimumSize(QSize(75, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_NumberOfPosts.setFont(font)
        self.label_NumberOfPosts.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_NumberOfPosts, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_NumberOfChars = QLabel(self.groupBox_2)
        self.label_NumberOfChars.setObjectName(u"label_NumberOfChars")
        sizePolicy6.setHeightForWidth(self.label_NumberOfChars.sizePolicy().hasHeightForWidth())
        self.label_NumberOfChars.setSizePolicy(sizePolicy6)
        self.label_NumberOfChars.setMinimumSize(QSize(75, 0))
        self.label_NumberOfChars.setFont(font)
        self.label_NumberOfChars.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_NumberOfChars, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy6.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy6)
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_ChangesMadeToCurrentPost = QLabel(self.groupBox_5)
        self.label_ChangesMadeToCurrentPost.setObjectName(u"label_ChangesMadeToCurrentPost")
        sizePolicy6.setHeightForWidth(self.label_ChangesMadeToCurrentPost.sizePolicy().hasHeightForWidth())
        self.label_ChangesMadeToCurrentPost.setSizePolicy(sizePolicy6)
        self.label_ChangesMadeToCurrentPost.setMinimumSize(QSize(75, 0))
        self.label_ChangesMadeToCurrentPost.setFont(font)
        self.label_ChangesMadeToCurrentPost.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_ChangesMadeToCurrentPost, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_ChangesMadeToDatabase = QLabel(self.groupBox_5)
        self.label_ChangesMadeToDatabase.setObjectName(u"label_ChangesMadeToDatabase")
        sizePolicy6.setHeightForWidth(self.label_ChangesMadeToDatabase.sizePolicy().hasHeightForWidth())
        self.label_ChangesMadeToDatabase.setSizePolicy(sizePolicy6)
        self.label_ChangesMadeToDatabase.setMinimumSize(QSize(75, 0))
        self.label_ChangesMadeToDatabase.setFont(font)
        self.label_ChangesMadeToDatabase.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_ChangesMadeToDatabase, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_5, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 921, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PySide6 Example", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Editor", None))
        self.pushButton_Commit.setText(QCoreApplication.translate("MainWindow", u"Commit to memory", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Buttons", None))
        self.pushButton_LoadDB.setText(QCoreApplication.translate("MainWindow", u"Load DB", None))
        self.pushButton_SaveDB.setText(QCoreApplication.translate("MainWindow", u"Save DB", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Counters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of posts in database:", None))
        self.label_NumberOfPosts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Number of characters in current post:", None))
        self.label_NumberOfChars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"States", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Changes made to current post:", None))
        self.label_ChangesMadeToCurrentPost.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Changes made to database:", None))
        self.label_ChangesMadeToDatabase.setText(QCoreApplication.translate("MainWindow", u"False", None))
    # retranslateUi

