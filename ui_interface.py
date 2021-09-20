# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceytmFyu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1171, 677)
        font = QFont()
        font.setFamily(u"Noto Sans Mono Light")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	background-color: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	border: none;\n"
"	color: #fff;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgba(14, 14, 22, 100);\n"
"	border: 2px solid rgb(24, 24, 36);\n"
"	border-radius: 5px;\n"
"}\n"
"#centralwidget{\n"
"	background-color: rgb(24, 24, 36);\n"
"	text-align: left;\n"
"}\n"
"#footer{	\n"
"	background-color: rgb(9, 5, 13);\n"
"	padding: 10px;\n"
"}\n"
"#messages_widget,\n"
"#menu_widget,\n"
"#right_menu,\n"
"#search_widget,\n"
"#notifications_widget,\n"
"#bottom_menu,\n"
"#login_widget,\n"
"#header_search_widget{	\n"
"	background-color: rgb(9, 5, 13);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_widget = QCustomSlideMenu(self.centralwidget)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setMinimumSize(QSize(0, 0))
        self.menu_widget.setMaximumSize(QSize(250, 16777215))
        self.menu_widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.menu_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.menu_widget)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(250, 0))
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.slide_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u":/fonts/fonts/PlayfairDisplay-VariableFont_wght.ttf")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.RichText)

        self.horizontalLayout_8.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/icons/gitlab.svg"))

        self.horizontalLayout_8.addWidget(self.label_3, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_8 = QFrame(self.slide_menu)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_8)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"	background-color: rgb(24, 24, 36);\n"
"	text-align: left;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgba(14, 14, 22, 100);\n"
"	border: 2px solid rgb(24, 24, 36);\n"
"	padding: 10px 5px;\n"
"	border-radius: 5px;\n"
"	text-align: left;\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 250, 547))
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon = QIcon()
        icon.addFile(u":/icons/icons/alert-triangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setIconSize(QSize(16, 16))

        self.verticalLayout_8.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_10)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)

        self.verticalLayout_8.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_10)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)

        self.verticalLayout_8.addWidget(self.pushButton_12)


        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)

        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon3, u"Drop Menu 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 250, 547))
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_11)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)

        self.verticalLayout_10.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_11)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/phone-incoming.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon5)

        self.verticalLayout_10.addWidget(self.pushButton_14)


        self.verticalLayout_9.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignTop)

        self.toolBox.addItem(self.page_2, icon3, u"Drop Menu 2")

        self.verticalLayout_6.addWidget(self.toolBox)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.slide_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.frame_9)
        self.exit_button.setObjectName(u"exit_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon6)
        self.exit_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.exit_button, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.frame_9, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.menu_widget)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 48))
        self.header_frame.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.frame_6 = QFrame(self.header_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.frame_6)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon7)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(24, 24, 36);\n"
"padding: 3px;\n"
"border-radius: 3px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(135, 0))
        self.lineEdit.setStyleSheet(u"border-bottom: 3px solid rgb(230, 5, 64);")

        self.horizontalLayout_6.addWidget(self.lineEdit, 0, Qt.AlignLeft)

        self.search_btn = QPushButton(self.frame_3)
        self.search_btn.setObjectName(u"search_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.search_btn, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.account_btn = QPushButton(self.frame_2)
        self.account_btn.setObjectName(u"account_btn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.account_btn.setIcon(icon9)

        self.horizontalLayout_5.addWidget(self.account_btn)

        self.notification_btn = QPushButton(self.frame_2)
        self.notification_btn.setObjectName(u"notification_btn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notification_btn.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.notification_btn)

        self.messages_btn = QPushButton(self.frame_2)
        self.messages_btn.setObjectName(u"messages_btn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/message-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.messages_btn.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.messages_btn)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setStyleSheet(u"QPushButton, QLineEdit{\n"
"	padding: 5px;\n"
"}\n"
"QLineEdit{\n"
"	border-bottom:  2px solid rgb(24, 24, 36);\n"
"}")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.header_search_widget = QCustomSlideMenu(self.main_body_contents)
        self.header_search_widget.setObjectName(u"header_search_widget")
        self.verticalLayout_13 = QVBoxLayout(self.header_search_widget)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.header_search_widget)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_18)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_14.addWidget(self.label_7)


        self.verticalLayout_13.addWidget(self.frame_18, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.header_search_widget, 0, Qt.AlignTop)

        self.frame_14 = QFrame(self.main_body_contents)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.messages_widget = QCustomSlideMenu(self.frame_14)
        self.messages_widget.setObjectName(u"messages_widget")
        self.verticalLayout_15 = QVBoxLayout(self.messages_widget)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.messages_widget)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(212, 433))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_34)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_34)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_15 = QLabel(self.frame_19)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/icons/icons/message-circle.svg"))

        self.horizontalLayout_23.addWidget(self.label_15, 0, Qt.AlignRight)

        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_16.setFont(font2)
        self.label_16.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.verticalLayout_28.addWidget(self.frame_19, 0, Qt.AlignHCenter)

        self.label_17 = QLabel(self.frame_34)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u":/icons/icons/message-square.svg"))

        self.verticalLayout_28.addWidget(self.label_17, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_18 = QLabel(self.frame_34)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_18, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.frame_34)


        self.horizontalLayout_10.addWidget(self.messages_widget)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(300, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 60))
        self.label_5.setMaximumSize(QSize(60, 60))
        self.label_5.setStyleSheet(u"border: 5px solid rgb(230, 5, 64);\n"
"border-radius: 30px;")
        self.label_5.setPixmap(QPixmap(u":/icons/icons/github.svg"))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.login_widget = QCustomSlideMenu(self.frame_16)
        self.login_widget.setObjectName(u"login_widget")
        self.login_widget.setStyleSheet(u"background-color: rgb(9, 5, 13);")
        self.verticalLayout_3 = QVBoxLayout(self.login_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.login_widget)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy2)
        self.frame_21.setMinimumSize(QSize(250, 115))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_21)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_9)

        self.lineEdit_2 = QLineEdit(self.frame_21)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_18.addWidget(self.lineEdit_2, 0, Qt.AlignHCenter)

        self.lineEdit_3 = QLineEdit(self.frame_21)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout_18.addWidget(self.lineEdit_3, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.frame_21)
        self.pushButton.setObjectName(u"pushButton")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon15)

        self.verticalLayout_18.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_21, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.login_widget)


        self.horizontalLayout_10.addWidget(self.frame_16, 0, Qt.AlignHCenter)

        self.notifications_widget = QCustomSlideMenu(self.frame_14)
        self.notifications_widget.setObjectName(u"notifications_widget")
        self.notifications_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_19 = QVBoxLayout(self.notifications_widget)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.notifications_widget)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(212, 433))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_22)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_15 = QFrame(self.frame_22)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.frame_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/icons/icons/bell.svg"))

        self.horizontalLayout_16.addWidget(self.label_8, 0, Qt.AlignRight)

        self.label_10 = QLabel(self.frame_15)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.label_10, 0, Qt.AlignLeft)


        self.verticalLayout_20.addWidget(self.frame_15, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.frame_22)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/icons/icons/bell-off.svg"))

        self.verticalLayout_20.addWidget(self.label_11, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_14 = QLabel(self.frame_22)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_14, 0, Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.frame_22, 0, Qt.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.notifications_widget)

        self.right_menu = QCustomSlideMenu(self.frame_14)
        self.right_menu.setObjectName(u"right_menu")
        self.verticalLayout_21 = QVBoxLayout(self.right_menu)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.right_menu)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 10, -1, 12)
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u":/icons/icons/settings.svg"))

        self.horizontalLayout_14.addWidget(self.label_13, 0, Qt.AlignRight)

        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        font4 = QFont()
        font4.setPointSize(20)
        self.label_12.setFont(font4)
        self.label_12.setStyleSheet(u"color: rgb(230, 5, 64)")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_12, 0, Qt.AlignLeft)


        self.verticalLayout_21.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.right_menu)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.search_widget = QCustomSlideMenu(self.frame_12)
        self.search_widget.setObjectName(u"search_widget")
        self.verticalLayout_22 = QVBoxLayout(self.search_widget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_24 = QFrame(self.search_widget)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(150, 100))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_24)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(129, 0))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_25)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.lineEdit_4 = QLineEdit(self.frame_25)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_24.addWidget(self.lineEdit_4)


        self.verticalLayout_23.addWidget(self.frame_25)


        self.verticalLayout_22.addWidget(self.frame_24, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.search_widget)

        self.pushButton_2 = QPushButton(self.frame_12)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/camera-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon16)

        self.verticalLayout_16.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_12)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/git-branch.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon17)

        self.verticalLayout_16.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon18)

        self.verticalLayout_16.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_12)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/folder-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon19)

        self.verticalLayout_16.addWidget(self.pushButton_5)


        self.verticalLayout_21.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.frame_26 = QFrame(self.right_menu)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.search_menu_btn = QPushButton(self.frame_26)
        self.search_menu_btn.setObjectName(u"search_menu_btn")
        self.search_menu_btn.setIcon(icon8)

        self.horizontalLayout_11.addWidget(self.search_menu_btn, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_26, 0, Qt.AlignBottom)


        self.horizontalLayout_10.addWidget(self.right_menu)


        self.verticalLayout_11.addWidget(self.frame_14)

        self.bottom_menu = QCustomSlideMenu(self.main_body_contents)
        self.bottom_menu.setObjectName(u"bottom_menu")
        self.bottom_menu.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.bottom_menu)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.bottom_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.frame_20 = QFrame(self.frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(221, 16777215))
        self.frame_20.setStyleSheet(u"background-color: rgb(24, 24, 36);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(15, -1, 15, -1)
        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(self.frame_23)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(42, 32))
        self.label_19.setStyleSheet(u"border: 2px solid rgb(230, 5, 64);\n"
"border-radius: 10px;")
        self.label_19.setPixmap(QPixmap(u":/icons/icons/facebook.svg"))
        self.label_19.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label_19, 0, Qt.AlignLeft)

        self.pushButton_7 = QPushButton(self.frame_23)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/more-vertical.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon20)

        self.horizontalLayout_17.addWidget(self.pushButton_7, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_23)

        self.label_20 = QLabel(self.frame_20)
        self.label_20.setObjectName(u"label_20")
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        self.label_20.setFont(font5)

        self.verticalLayout_25.addWidget(self.label_20)

        self.frame_27 = QFrame(self.frame_20)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_21 = QLabel(self.frame_27)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_18.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_27)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_18.addWidget(self.label_22)


        self.verticalLayout_25.addWidget(self.frame_27)


        self.horizontalLayout_15.addWidget(self.frame_20)

        self.frame_31 = QFrame(self.frame_5)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(222, 16777215))
        self.frame_31.setStyleSheet(u"background-color: rgb(24, 24, 36);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_31)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(15, -1, 15, -1)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_27 = QLabel(self.frame_32)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(36, 32))
        self.label_27.setStyleSheet(u"border: 2px solid rgb(230, 5, 64);\n"
"border-radius: 10px;")
        self.label_27.setPixmap(QPixmap(u":/icons/icons/twitter.svg"))
        self.label_27.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_27, 0, Qt.AlignLeft)

        self.pushButton_9 = QPushButton(self.frame_32)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon20)

        self.horizontalLayout_21.addWidget(self.pushButton_9, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.frame_32)

        self.label_28 = QLabel(self.frame_31)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font5)

        self.verticalLayout_27.addWidget(self.label_28)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_29 = QLabel(self.frame_33)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_22.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_33)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_22.addWidget(self.label_30)


        self.verticalLayout_27.addWidget(self.frame_33)


        self.horizontalLayout_15.addWidget(self.frame_31)

        self.frame_28 = QFrame(self.frame_5)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(221, 16777215))
        self.frame_28.setStyleSheet(u"background-color: rgb(24, 24, 36);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_28)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(15, -1, 15, -1)
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_23 = QLabel(self.frame_29)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(36, 32))
        self.label_23.setStyleSheet(u"border: 2px solid rgb(230, 5, 64);\n"
"border-radius: 10px;")
        self.label_23.setPixmap(QPixmap(u":/icons/icons/twitch.svg"))
        self.label_23.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.pushButton_8 = QPushButton(self.frame_29)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon20)

        self.horizontalLayout_19.addWidget(self.pushButton_8, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_29)

        self.label_24 = QLabel(self.frame_28)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_24)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_25 = QLabel(self.frame_30)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_20.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_30)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_20.addWidget(self.label_26)


        self.verticalLayout_26.addWidget(self.frame_30)


        self.horizontalLayout_15.addWidget(self.frame_28)


        self.horizontalLayout_13.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.bottom_menu, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.footer_2 = QFrame(self.footer)
        self.footer_2.setObjectName(u"footer_2")
        self.footer_2.setFrameShape(QFrame.StyledPanel)
        self.footer_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.footer_2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.bottom_menu_button = QPushButton(self.footer_2)
        self.bottom_menu_button.setObjectName(u"bottom_menu_button")
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bottom_menu_button.setIcon(icon21)

        self.horizontalLayout_12.addWidget(self.bottom_menu_button, 0, Qt.AlignHCenter)

        self.right_menu_toggle_btn = QPushButton(self.footer_2)
        self.right_menu_toggle_btn.setObjectName(u"right_menu_toggle_btn")
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.right_menu_toggle_btn.setIcon(icon22)

        self.horizontalLayout_12.addWidget(self.right_menu_toggle_btn, 0, Qt.AlignRight)

        self.size_grip = QFrame(self.footer_2)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.footer_2, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">APP NAME</span></p></body></html>", None))
        self.label_3.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"ITEM 1", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"ITEM 2", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"ITEM 3", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Drop Menu 1", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"SUB MENU", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"SUB MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Some text you would like to fill here", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Drop Menu 2", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.open_close_side_bar_btn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_btn.setText("")
        self.account_btn.setText("")
        self.notification_btn.setText("")
        self.messages_btn.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Searching Your Word...", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:rgb(230, 5, 64);\">MESSAGES</span></p></body></html>", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"No Messages. Please login", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"GITHUB", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"YOU ARE NOT LOGGED IN", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_8.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:rgb(230, 5, 64);\">NOTIFICATIONS</span></p></body></html>", None))
        self.label_11.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"OOPS! No new notifications", None))
        self.label_13.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:rgb(230, 5, 64);\">SETTINGS</span></p></body></html>", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Something", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Some settings", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Another Settings", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Additional Settings", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Final Settings", None))
        self.search_menu_btn.setText("")
        self.label_19.setText("")
        self.pushButton_7.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Connect With Facebook", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"SignUp", None))
        self.label_27.setText("")
        self.pushButton_9.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Connect With Twitter", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"SignUp", None))
        self.label_23.setText("")
        self.pushButton_8.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Connect With Twitch", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"SignUp", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Modern UI v 7.7.7", None))
        self.bottom_menu_button.setText("")
        self.right_menu_toggle_btn.setText("")
    # retranslateUi

