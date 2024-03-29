from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class Ui_Youtube(object):
    def setupUi(self, Youtube):
        Youtube.setObjectName("Youtube")
        Youtube.setWindowIcon(QtGui.QIcon('icon.ico'))
        Youtube.resize(600, 750)
        self.centralwidget = QtWidgets.QWidget(Youtube)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        Youtube.setFont(font)

        """--------------   Main Menu   ---------------------"""
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(5, 5, 590, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.MenuSSButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.MenuSSButton.setObjectName("MenuSSButton")
        self.MenuSSButton.setEnabled(False)
        self.horizontalLayout.addWidget(self.MenuSSButton)
        self.MenuDownloadButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.MenuDownloadButton.setObjectName("MenuDownloadButton")
        self.horizontalLayout.addWidget(self.MenuDownloadButton)
        self.MenuyYtPlanButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.MenuyYtPlanButton.setObjectName("MenuyYtPlanButton")
        self.horizontalLayout.addWidget(self.MenuyYtPlanButton)

        """--------------   ScreenShoot  ---------------------"""
        self.groupBoxSS = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSS.setGeometry(QtCore.QRect(5, 60, 590, 350))
        self.groupBoxSS.setObjectName("groupBoxSS")
        self.groupBoxSS.show()

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBoxSS)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 570, 240))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")


        # Video File Path
        self.SSLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SSLabel.setObjectName("SSLabel")
        self.verticalLayout.addWidget(self.SSLabel)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
                     
        self.SSGetPathLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SSGetPathLine.setObjectName("SSGetPathLine")
        self.horizontalLayout_2.addWidget(self.SSGetPathLine)

        self.SSGetPathButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SSGetPathButton.setObjectName("SSGetPathButton")
        self.horizontalLayout_2.addWidget(self.SSGetPathButton)

        # Save File Path
        self.SSLabel_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SSLabel_2.setObjectName("SSLabel_2")
        self.verticalLayout.addWidget(self.SSLabel_2)
        # self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.SSGetSavePathLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SSGetSavePathLine.setObjectName("SSGetSavePathLine")
        self.horizontalLayout_3.addWidget(self.SSGetSavePathLine)

        self.SSGetSavePathButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SSGetSavePathButton.setObjectName("SSGetSavePathButton")
        self.horizontalLayout_3.addWidget(self.SSGetSavePathButton)

        # Resulation
        self.SSLabel_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SSLabel_3.setObjectName("SSLabel_3")
        self.verticalLayout.addWidget(self.SSLabel_3)
        # self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        
        self.SSLabel_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SSLabel_5.setObjectName("SSLabel_5")
        self.horizontalLayout_4.addWidget(self.SSLabel_5)

        self.SSWidthLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SSWidthLine.setObjectName("SSWidthLine")
        self.horizontalLayout_4.addWidget(self.SSWidthLine)

        self.SSLabel_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SSLabel_4.setObjectName("SSLabel_4")
        self.horizontalLayout_4.addWidget(self.SSLabel_4)

        self.SSHeightLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SSHeightLine.setObjectName("SSHeightLine")
        self.horizontalLayout_4.addWidget(self.SSHeightLine)

        self.SSLabel_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SSLabel_6.setObjectName("SSLabel_6")
        self.horizontalLayout_4.addWidget(self.SSLabel_6)

        self.SSOutroCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.SSOutroCheckBox.setObjectName("SSOutroCheckBox")
        self.verticalLayout.addWidget(self.SSOutroCheckBox)
        
            # SS BUTTON
        self.SSRunButton = QtWidgets.QPushButton(self.groupBoxSS)
        self.SSRunButton.setGeometry(QtCore.QRect(40, 300, 500, 30))
        self.SSRunButton.setObjectName("SSRunButton")

        """--------------   Download Video  ---------------------"""
        
        self.groupBoxDownload = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDownload.setGeometry(QtCore.QRect(5, 60, 590, 350))
        self.groupBoxDownload.setObjectName("groupBoxDownload")
        self.groupBoxDownload.hide()

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxDownload)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 570, 240))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_4")
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.DownloadLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.DownloadLabel.setObjectName("DownloadLabel")
        self.horizontalLayout_5.addWidget(self.DownloadLabel)

        self.DownloadTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.DownloadTextEdit.setObjectName("DownloadTextEdit")
        self.horizontalLayout_5.addWidget(self.DownloadTextEdit)

        self.PlayListCheck = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.PlayListCheck.setObjectName("PlayListCheck")
        self.verticalLayout_2.addWidget(self.PlayListCheck)

        self.FullHdRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.FullHdRadio.setObjectName("FullHdRadio")
        self.verticalLayout_2.addWidget(self.FullHdRadio)
        self.FullHdRadio.setChecked(True)
        
        self.HdRadio = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.HdRadio.setObjectName("HdRadio")
        self.verticalLayout_2.addWidget(self.HdRadio)

        self.DownloadLabel_1 = QtWidgets.QLabel()
        self.DownloadLabel_1.setObjectName("DownloadLabel_1")
        self.verticalLayout_2.addWidget(self.DownloadLabel_1)
        # self.label_6.setAlignment(QtCore.Qt.AlignCenter)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.DownloadGetSavePathLine = QtWidgets.QLineEdit()
        self.DownloadGetSavePathLine.setObjectName("DownloadGetSavePathLine")
        self.horizontalLayout_6.addWidget(self.DownloadGetSavePathLine)

        self.DownloadGetSavePathButton = QtWidgets.QPushButton()
        self.DownloadGetSavePathButton.setObjectName("DownloadGetSavePathButton")
        self.horizontalLayout_6.addWidget(self.DownloadGetSavePathButton)

         #Download Button
        
        self.DownloadRun = QtWidgets.QPushButton(self.groupBoxDownload)
        self.DownloadRun.setGeometry(QtCore.QRect(40, 300, 500, 30))
        self.DownloadRun.setObjectName("DownloadRun")


        """--------------   Youtube Plan   ---------------------"""
            # Manin
        self.YtPlanGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.YtPlanGroupBox.setGeometry(QtCore.QRect(5, 60, 590, 465))
        self.YtPlanGroupBox.setObjectName("YtPlanGroupBox")
        self.YtPlanGroupBox.hide()

        self.YtPlanWidgets = QtWidgets.QWidget(self.YtPlanGroupBox)
        self.YtPlanWidgets.setGeometry(QtCore.QRect(10, 20, 570, 30))
        self.YtPlanWidgets.setObjectName("YtPlanWidgets")

        self.YtPlanMenuHLayout = QtWidgets.QHBoxLayout(self.YtPlanWidgets)
        self.YtPlanMenuHLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.YtPlanMenuHLayout.setContentsMargins(0, 0, 0, 0)
        self.YtPlanMenuHLayout.setObjectName("YtPlanMenuHLayout")

        self.YtPlanMenuShareButton = QtWidgets.QPushButton(self.YtPlanWidgets)
        self.YtPlanMenuShareButton.setObjectName("YtPlanMenuShareButton")
        self.YtPlanMenuHLayout.addWidget(self.YtPlanMenuShareButton)
        self.YtPlanMenuShareButton.setEnabled(False)

        self.YtPlanMenuInputSettingsButton = QtWidgets.QPushButton(self.YtPlanWidgets)
        self.YtPlanMenuInputSettingsButton.setObjectName("YtPlanMenuInputSettingsButton")
        self.YtPlanMenuHLayout.addWidget(self.YtPlanMenuInputSettingsButton)

        """-------------- Share And Planning  -----------------------"""
        
        self.YtPlanShareGroupBox = QtWidgets.QGroupBox(self.YtPlanGroupBox)
        self.YtPlanShareGroupBox.setGeometry(QtCore.QRect(10, 50, 570, 400))
        self.YtPlanShareGroupBox.setObjectName("YtPlanShareGroupBox")

        self.YtPlanShareWidgets = QtWidgets.QWidget(self.YtPlanShareGroupBox)
        self.YtPlanShareWidgets.setGeometry(QtCore.QRect(5, 20, 560, 375))
        self.YtPlanShareWidgets.setObjectName("YtPlanShareWidgets")

        self.YtPlanShareVLayout = QtWidgets.QVBoxLayout(self.YtPlanShareWidgets)
        self.YtPlanShareVLayout.setContentsMargins(0, 0, 0, 0)
        self.YtPlanShareVLayout.setObjectName("YtPlanShareVLayout")

        """---------- Browser Select Menu ---------------"""

        self.BrowserMenuHLayout = QtWidgets.QHBoxLayout()
        self.BrowserMenuHLayout.setContentsMargins(0, 0, 0, 0)
        self.BrowserMenuHLayout.setObjectName("BrowserMenuHLayout")
        self.OperaButton = QtWidgets.QPushButton()
        self.OperaButton.setObjectName("OperaButton")
        self.BrowserMenuHLayout.addWidget(self.OperaButton)
        self.OperaButton.setVisible(False)
        self.BraveButton = QtWidgets.QPushButton()
        self.BraveButton.setObjectName("BraveButton")
        self.BrowserMenuHLayout.addWidget(self.BraveButton)
        self.BraveButton.setVisible(False)
        self.ChromeButton = QtWidgets.QPushButton()
        self.ChromeButton.setObjectName("ChromeButton")
        self.BrowserMenuHLayout.addWidget(self.ChromeButton)
        self.ChromeButton.setVisible(False)
        self.YtPlanShareVLayout.addLayout(self.BrowserMenuHLayout)

        """------------------- Studio Link ------------------------------"""

        self.LinkHLayout = QtWidgets.QHBoxLayout()
        self.LinkHLayout.setContentsMargins(0, 0, 0, 0)
        self.LinkHLayout.setObjectName("LinkHLayout")
        self.LinkLabel = QtWidgets.QLabel()
        self.LinkLabel.setObjectName("LinkLabel")
        self.LinkHLayout.addWidget(self.LinkLabel)
        self.LinkLineEdit = QtWidgets.QLineEdit()
        self.LinkLineEdit.setObjectName("LinkLineEdit")
        self.LinkHLayout.addWidget(self.LinkLineEdit)
        self.YtPlanShareVLayout.addLayout(self.LinkHLayout)
        
        """---------------- Channel Lang Check ------------------------"""

        self.RadioBtnHLayout = QtWidgets.QHBoxLayout()
        self.RadioBtnHLayout.setContentsMargins(0, 0, 0, 0)
        self.RadioBtnHLayout.setObjectName("RadioBtnHLayout")
        self.TrChannelRadioButton = QtWidgets.QRadioButton()
        self.TrChannelRadioButton.setObjectName("TrChannelRadioButton")
        self.TrChannelRadioButton.setChecked(True)
        self.RadioBtnHLayout.addWidget(self.TrChannelRadioButton)
        self.EnChannelRadioButton = QtWidgets.QRadioButton()
        self.EnChannelRadioButton.setObjectName("EnChannelRadioButton")
        self.RadioBtnHLayout.addWidget(self.EnChannelRadioButton)

        self.YtPlanShareVLayout.addLayout(self.RadioBtnHLayout)

        """------------------- Input Check ---------------------------"""

        self.RadioBtnHLayout_2 = QtWidgets.QHBoxLayout()
        self.RadioBtnHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.RadioBtnHLayout_2.setObjectName("RadioBtnHLayout_2")
        self.HeadCbox = QtWidgets.QCheckBox()
        self.HeadCbox.setObjectName("HeadCbox")
        self.RadioBtnHLayout_2.addWidget(self.HeadCbox)
        self.CommentCbox = QtWidgets.QCheckBox()
        self.CommentCbox.setObjectName("CommentCbox")
        self.RadioBtnHLayout_2.addWidget(self.CommentCbox)
        self.TagCbox = QtWidgets.QCheckBox()
        self.TagCbox.setObjectName("TagCbox")
        self.RadioBtnHLayout_2.addWidget(self.TagCbox)
        self.PicCbox = QtWidgets.QCheckBox()
        self.PicCbox.setObjectName("PicCbox")
        self.RadioBtnHLayout_2.addWidget(self.PicCbox)
        self.MonyCbox = QtWidgets.QCheckBox()
        self.MonyCbox.setObjectName("MonyCbox")
        self.RadioBtnHLayout_2.addWidget(self.MonyCbox)
        self.YtPlanShareVLayout.addLayout(self.RadioBtnHLayout_2)

        """---------------- Post Menu Select (Shorts/Normal) -----------------------"""

        self.YtPlanMenu = QtWidgets.QHBoxLayout()
        self.YtPlanMenu.setContentsMargins(0, 0, 0, 0)
        self.YtPlanMenu.setObjectName("YtPlanMenu")
        self.NormalMenuButton = QtWidgets.QPushButton()
        self.NormalMenuButton.setObjectName("NormalMenuButton")
        self.YtPlanMenu.addWidget(self.NormalMenuButton)
        self.NormalMenuButton.setEnabled(False)
        self.ShortsMenuButton = QtWidgets.QPushButton()
        self.ShortsMenuButton.setObjectName("ShortsMenuButton")
        self.YtPlanMenu.addWidget(self.ShortsMenuButton)
        self.YtPlanShareVLayout.addLayout(self.YtPlanMenu)

        """-------------- Normal Post Form ---------------"""

        self.PGroupBox = QtWidgets.QGroupBox()
        self.PGroupBox.setGeometry(QtCore.QRect(10, 10, 500,50))
        self.PGroupBox.setObjectName("PGroupBox")
        self.PGroupBoxWidget = QtWidgets.QWidget(self.PGroupBox)
        self.PGroupBoxWidget.setGeometry(QtCore.QRect(10, 20, 545, 200))
        self.PGroupBoxWidget.setObjectName("PGroupBoxWidget")
        self.PFormVLayout = QtWidgets.QVBoxLayout(self.PGroupBoxWidget)
        self.PFormVLayout.setContentsMargins(0, 0, 0, 0)
        self.PFormVLayout.setObjectName("PFormVLayout")
        self.PostFormLayout = QtWidgets.QFormLayout()
        self.PostFormLayout.setObjectName("PostFormLayout")
        self.PMenuLabel = QtWidgets.QLabel(self.PGroupBoxWidget)
        self.PMenuLabel.setObjectName("PMenuLabel")
        self.PostFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.PMenuLabel)
        self.PPerDay = QtWidgets.QSpinBox(self.PGroupBoxWidget)
        self.PPerDay.setObjectName("PPerDay")
        self.PostFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.PPerDay)
        self.PMenuLabel_2 = QtWidgets.QLabel(self.PGroupBoxWidget)
        self.PMenuLabel_2.setObjectName("PMenuLabel_2")
        self.PostFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PMenuLabel_2)
        self.PDayLimit = QtWidgets.QSpinBox(self.PGroupBoxWidget)
        self.PDayLimit.setObjectName("PDayLimit")
        self.PostFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.PDayLimit)
        self.PMenuLabel_3 = QtWidgets.QLabel(self.PGroupBoxWidget)
        self.PMenuLabel_3.setObjectName("PMenuLabel_3")
        self.PostFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.PMenuLabel_3)
        self.PPerMin = QtWidgets.QSpinBox(self.PGroupBoxWidget)
        self.PPerMin.setObjectName("PPerMin")
        self.PostFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.PPerMin)
        self.PMenuLabel_4 = QtWidgets.QLabel(self.PGroupBoxWidget)
        self.PMenuLabel_4.setObjectName("PMenuLabel_4")
        self.PostFormLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.PMenuLabel_4)
        self.PDateTime = QtWidgets.QDateTimeEdit(self.PGroupBoxWidget)
        self.PDateTime.setObjectName("PDateTime")
        self.PDateTime.setDateTime(datetime.datetime.now())
        self.PostFormLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.PDateTime)

        self.PLimit = QtWidgets.QSpinBox(self.PGroupBoxWidget)
        self.PLimit.setObjectName("PLimit")
        self.PostFormLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.PLimit)
        self.PMenuLabel_5 = QtWidgets.QLabel(self.PGroupBoxWidget)
        self.PMenuLabel_5.setObjectName("PMenuLabel_5")
        self.PostFormLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.PMenuLabel_5)

        self.PFormVLayout.addLayout(self.PostFormLayout)
        self.YtPlanShareVLayout.addWidget(self.PGroupBox)

        self.YtPlanRunButton = QtWidgets.QPushButton()
        self.YtPlanRunButton.setObjectName("YtPlanRunButton")
        self.YtPlanShareVLayout.addWidget(self.YtPlanRunButton)

        """-------------- Head / Tag / Comment / Browser..... Menu -----------------------"""

        self.YtPlanItemGroupBox = QtWidgets.QGroupBox(self.YtPlanGroupBox)
        self.YtPlanItemGroupBox.setGeometry(QtCore.QRect(10, 50, 570, 400))
        self.YtPlanItemGroupBox.setObjectName("YtPlanItemGroupBox")
        self.YtPlanItemGroupBox.hide()

        self.YtPlanItemWidgets = QtWidgets.QWidget(self.YtPlanItemGroupBox)
        self.YtPlanItemWidgets.setGeometry(QtCore.QRect(5, 20, 560, 375))
        self.YtPlanItemWidgets.setObjectName("YtPlanItemWidgets")

        self.SettingsVLayout = QtWidgets.QVBoxLayout(self.YtPlanItemWidgets)
        self.SettingsVLayout.setContentsMargins(0, 0, 0, 0)
        self.SettingsVLayout.setObjectName("SettingsVLayout")

        self.InputButtonMenuHLayout = QtWidgets.QHBoxLayout()
        self.InputButtonMenuHLayout.setObjectName("InputButtonMenuHLayout")
        self.HeadButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.HeadButton.setObjectName("HeadPushButton")
        self.InputButtonMenuHLayout.addWidget(self.HeadButton)
        self.CommentButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.CommentButton.setObjectName("CommentButton")
        self.InputButtonMenuHLayout.addWidget(self.CommentButton)
        self.TagButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.TagButton.setObjectName("TagButton")
        self.InputButtonMenuHLayout.addWidget(self.TagButton)
        self.BrowserButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.BrowserButton.setObjectName("BrowserButton")
        self.InputButtonMenuHLayout.addWidget(self.BrowserButton)
        self.PicturesButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.PicturesButton.setObjectName("PicturesButton")
        self.InputButtonMenuHLayout.addWidget(self.PicturesButton)
        self.SettingsVLayout.addLayout(self.InputButtonMenuHLayout)
        self.InputRadioButtonHLayout = QtWidgets.QHBoxLayout()
        self.InputRadioButtonHLayout.setObjectName("InputRadioButtonHLayout")
        self.TrRadioButton = QtWidgets.QRadioButton(self.YtPlanItemWidgets)
        self.TrRadioButton.setObjectName("TrRadioButton")
        self.TrRadioButton.setChecked(True)
        self.InputRadioButtonHLayout.addWidget(self.TrRadioButton)
        self.EngRadioButton = QtWidgets.QRadioButton(self.YtPlanItemWidgets)
        self.EngRadioButton.setObjectName("EngRadioButton")
        self.InputRadioButtonHLayout.addWidget(self.EngRadioButton)
        self.SettingsVLayout.addLayout(self.InputRadioButtonHLayout)

        self.tableWidget = QtWidgets.QTableWidget(self.YtPlanItemWidgets)
        self.tableWidget.setGeometry(QtCore.QRect(140, 80, 400, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.SettingsVLayout.addWidget(self.tableWidget)

        self.InputLabel = QtWidgets.QLabel(self.YtPlanItemWidgets)
        self.InputLabel.setObjectName("InputLabel")
        self.InputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SettingsVLayout.addWidget(self.InputLabel)

        self.InputAddHLayout = QtWidgets.QHBoxLayout()
        self.InputAddHLayout.setObjectName("InputAddHLayout")
        self.SettingsVLayout.addLayout(self.InputAddHLayout)

        self.InputlineLabel = QtWidgets.QLabel(self.YtPlanItemWidgets)
        self.InputlineLabel.setObjectName("InputlineLabel")
        self.InputAddHLayout.addWidget(self.InputlineLabel)

        self.InputlineEdit = QtWidgets.QLineEdit(self.YtPlanItemWidgets)
        self.InputlineEdit.setObjectName("InputlineEdit")
        self.InputAddHLayout.addWidget(self.InputlineEdit)

        self.InputlineLabel2 = QtWidgets.QLabel(self.YtPlanItemWidgets)
        self.InputlineLabel2.setObjectName("InputlineLabel2")
        self.InputAddHLayout.addWidget(self.InputlineLabel2)

        self.InputlineEdit2 = QtWidgets.QLineEdit(self.YtPlanItemWidgets)
        self.InputlineEdit2.setObjectName("InputlineEdit2")
        self.InputAddHLayout.addWidget(self.InputlineEdit2)
               
        self.InputButtonHlayout = QtWidgets.QHBoxLayout()
        self.InputButtonHlayout.setObjectName("InputButtonHlayout")
        self.SettingsVLayout.addLayout(self.InputButtonHlayout)

        self.InputAddButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.InputAddButton.setObjectName("InputAddButton")
        self.InputAddButton.setStyleSheet("background-color : green;color: white")
        self.InputButtonHlayout.addWidget(self.InputAddButton)

        self.InputUpdateButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.InputUpdateButton.setObjectName("InputUpdateButton")
        self.InputUpdateButton.setStyleSheet("background-color : blue;color: white")
        self.InputButtonHlayout.addWidget(self.InputUpdateButton)

        self.InputDeleteButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.InputDeleteButton.setObjectName("InputDeleteButton")
        self.InputDeleteButton.setStyleSheet("background-color : red;color: white") 
        self.InputButtonHlayout.addWidget(self.InputDeleteButton)
        

        """--------------- --------------------- -------------------- ---------------"""

        self.BrowserLabel = QtWidgets.QLabel(self.YtPlanItemWidgets)
        self.BrowserLabel.setObjectName("BrowserLabel")
        self.BrowserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SettingsVLayout.addWidget(self.BrowserLabel)

        self.BrowserHLayout = QtWidgets.QHBoxLayout()
        self.BrowserHLayout.setObjectName("InputAddHLayout")
        self.SettingsVLayout.addLayout(self.BrowserHLayout)
        
        self.BrowserLabel_2 = QtWidgets.QLabel(self.YtPlanItemWidgets)
        self.BrowserLabel_2.setObjectName("BrowserLabel_2")
        self.BrowserLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.BrowserHLayout.addWidget(self.BrowserLabel_2)

        self.BrowserExelineEdit = QtWidgets.QLineEdit(self.YtPlanItemWidgets)
        self.BrowserExelineEdit.setObjectName("BrowserExelineEdit")
        self.BrowserHLayout.addWidget(self.BrowserExelineEdit)
        
        self.BrowserExeButton = QtWidgets.QPushButton(self.YtPlanItemWidgets)
        self.BrowserExeButton.setObjectName("BrowserExeButton")
        self.BrowserHLayout.addWidget(self.BrowserExeButton)

        
        
        """ ----------------------- Log Screen ------------------------"""

        # SS Log
        self.groupBoxSSLog = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSSLog.setGeometry(QtCore.QRect(5, 410, 590, 235))
        self.groupBoxSSLog.setObjectName("groupBoxSSLog")

        self.SSLogWidgets = QtWidgets.QWidget(self.groupBoxSSLog)
        self.SSLogWidgets.setGeometry(QtCore.QRect(10, 20, 570, 210))
        self.SSLogWidgets.setObjectName("SSLogWidgets")

        self.SSLogVLayout = QtWidgets.QVBoxLayout(self.SSLogWidgets)
        self.SSLogVLayout.setContentsMargins(0, 0, 0, 0)
        self.SSLogVLayout.setObjectName("SSLogLayout")

        self.SSLogtextBrowser = QtWidgets.QTextBrowser(self.SSLogWidgets)
        self.SSLogtextBrowser.setObjectName("SSLogtextBrowser")
        self.SSLogVLayout.addWidget(self.SSLogtextBrowser)

        # Download Log
        self.groupBoxDownloadLog = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDownloadLog.setGeometry(QtCore.QRect(5, 410, 590, 235))
        self.groupBoxDownloadLog.setObjectName("groupBoxDownloadLog")
        self.groupBoxDownloadLog.hide()

        self.DownloadLogWidget = QtWidgets.QWidget(self.groupBoxDownloadLog)
        self.DownloadLogWidget.setGeometry(QtCore.QRect(10, 20, 570, 210))
        self.DownloadLogWidget.setObjectName("DownloadLogWidget")

        self.DownloadLogVLayout = QtWidgets.QVBoxLayout(self.DownloadLogWidget)
        self.DownloadLogVLayout.setContentsMargins(0, 0, 0, 0)
        self.DownloadLogVLayout.setObjectName("DownloadLogVLayout")

        self.DownloadLogtextBrowser = QtWidgets.QTextBrowser(self.DownloadLogWidget)
        self.DownloadLogtextBrowser.setObjectName("DownloadLogtextBrowser")
        self.DownloadLogVLayout.addWidget(self.DownloadLogtextBrowser)

        # YT Plan Log

        self.groupBoxYtPlanLog = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxYtPlanLog.setGeometry(QtCore.QRect(5, 530, 590, 210))
        self.groupBoxYtPlanLog.setObjectName("groupBoxYtPlanLog")
        self.groupBoxYtPlanLog.hide()
        
        self.YtPlanLogWidgets = QtWidgets.QWidget(self.groupBoxYtPlanLog)
        self.YtPlanLogWidgets.setGeometry(QtCore.QRect(10, 20, 570, 180))
        self.YtPlanLogWidgets.setObjectName("YtPlanLogWidgets")

        self.YtPlanLogVLayout = QtWidgets.QVBoxLayout(self.YtPlanLogWidgets)
        self.YtPlanLogVLayout.setContentsMargins(0, 0, 0, 0)
        self.YtPlanLogVLayout.setObjectName("SSLogLayout")

        self.YtPlanLogtextBrowser = QtWidgets.QTextBrowser(self.YtPlanLogWidgets)
        self.YtPlanLogtextBrowser.setObjectName("YtPlanLogtextBrowser")
        self.YtPlanLogVLayout.addWidget(self.YtPlanLogtextBrowser)

        Youtube.setCentralWidget(self.centralwidget)

        self.retranslateUi(Youtube)
        QtCore.QMetaObject.connectSlotsByName(Youtube)

    def retranslateUi(self, Youtube):
        _translate = QtCore.QCoreApplication.translate
        Youtube.setWindowTitle(_translate("Youtube", "Youtube APP"))
        
        # Menu Buttons
        self.MenuDownloadButton.setText(_translate("Youtube", "Video Indirme"))
        self.MenuSSButton.setText(_translate("Youtube", "SS Alma"))
        self.MenuyYtPlanButton.setText(_translate("Youtube", "Video Planlama"))
        
        # SS ALMA GROUP
        self.groupBoxSS.setTitle(_translate("Youtube", "SS ALMA"))
        self.SSLabel.setText(_translate("Youtube", "Videoların Dosya Yolu"))
        self.SSLabel_2.setText(_translate("Youtube", "Kayıt Edilecek Dosya Yolu"))
        self.SSLabel_3.setText(_translate("Youtube", "Çözünürlük"))
        self.SSLabel_4.setText(_translate("Youtube", "X"))
        self.SSLabel_5.setText(_translate("Youtube", "Genişlik"))
        self.SSLabel_6.setText(_translate("Youtube", "Yükseklik"))
        self.SSOutroCheckBox.setText(_translate("Youtube", "Video Sonunda Outro Var"))

        self.SSGetPathButton.setText(_translate("Youtube", "Dosya Seç"))
        self.SSGetSavePathButton.setText(_translate("Youtube", "Dosya Seç"))
        self.SSRunButton.setText(_translate("Youtube", "Başlat"))

        # Download Group
        self.groupBoxDownload.setTitle(_translate("Youtube", "Youtube Download"))
        self.DownloadLabel.setText(_translate("Youtube", "Linkler"))
        self.DownloadLabel_1.setText(_translate("Youtube", "Kayıt Edilecek Yer"))
        self.PlayListCheck.setText(_translate("Youtube", "Oynatma Listesi"))
        self.FullHdRadio.setText(_translate("Youtube", "1080p Olarak İndir"))
        self.HdRadio.setText(_translate("Youtube", "720p Olarak İndir"))

        self.DownloadGetSavePathButton.setText(_translate("Youtube", "Dosya Seç"))
        self.DownloadRun.setText(_translate("Youtube", "İndirmeyi Başlat"))
        
        # YT Plan
        self.YtPlanGroupBox.setTitle(_translate("Youtube", "Youtube Plan"))
        self.YtPlanMenuInputSettingsButton.setText(_translate("MainWindow", "Veri Girişi ve Ayarlar"))
        self.YtPlanMenuShareButton.setText(_translate("MainWindow", "Planlama"))
       
        # Share 
        self.YtPlanShareGroupBox.setTitle(_translate("Youtube", "Planlama"))
        
        self.PGroupBox.setTitle(_translate("MainWindow", "Normal Post"))
        self.PMenuLabel.setText(_translate("MainWindow", "Kaç Günde Bir"))
        self.PMenuLabel_2.setText(_translate("MainWindow", "Günde Kaç Tane"))
        self.PMenuLabel_3.setText(_translate("MainWindow", "Paylaşımlar Arası Beklenicek Süre (Dk)"))
        self.PMenuLabel_4.setText(_translate("MainWindow", "Paylaşım Başlangıç Tarihi"))
        self.PMenuLabel_5.setText(_translate("MainWindow", "Paylaşım Limiti"))
        self.NormalMenuButton.setText(_translate("MainWindow", "Normal"))
        self.ShortsMenuButton.setText(_translate("MainWindow", "Reels"))
        self.TrChannelRadioButton.setText(_translate("MainWindow", "Türkçe"))
        self.EnChannelRadioButton.setText(_translate("MainWindow", "English"))
        self.HeadCbox.setText(_translate("MainWindow", "Başlık"))
        self.CommentCbox.setText(_translate("MainWindow", "Açıklama"))
        self.TagCbox.setText(_translate("MainWindow", "Etiket"))
        self.PicCbox.setText(_translate("MainWindow", "Resim"))
        self.MonyCbox.setText(_translate("MainWindow", "Para Kazanma"))
        self.LinkLabel.setText(_translate("MainWindow", "Studio Link"))
        self.OperaButton.setText(_translate("MainWindow", "Opera"))
        self.BraveButton.setText(_translate("MainWindow", "Brave"))
        self.ChromeButton.setText(_translate("MainWindow", "Google"))

        self.YtPlanRunButton.setText(_translate("MainWindow", "Başlat"))
        

        # HEAD/COMMENTS/TAGS ITEM INPUT 
        self.YtPlanItemGroupBox.setTitle(_translate("Youtube", "Veri Girişi"))

        self.HeadButton.setText(_translate("MainWindow", "Başlıklar"))
        self.CommentButton.setText(_translate("MainWindow", "Açıklamalar"))
        self.TagButton.setText(_translate("MainWindow", "Etiketler"))
        self.BrowserButton.setText(_translate("MainWindow", "Browser"))
        self.PicturesButton.setText(_translate("MainWindow", "Resimler"))
        self.TrRadioButton.setText(_translate("MainWindow", "Türkçe"))
        self.EngRadioButton.setText(_translate("MainWindow", "English"))

        self.InputLabel.setText(_translate("MainWindow", "Düzenleme İşlemleri"))
        self.InputlineLabel.setText(_translate("MainWindow", "1.Alan"))
        self.InputlineLabel2.setText(_translate("MainWindow", "2.Alan"))
        self.BrowserLabel.setText(_translate("MainWindow", "Browser Ayarları"))
        self.BrowserLabel_2.setText(_translate("MainWindow", "Dosya Yolu Bul :"))
        self.InputAddButton.setText(_translate("MainWindow", "Ekle"))
        self.InputDeleteButton.setText(_translate("MainWindow", "Seçileni Sil"))
        self.InputUpdateButton.setText(_translate("MainWindow", "Güncelle"))
        self.BrowserExeButton.setText(_translate("MainWindow", "Dosya Seç"))
        
        # Log Group
        self.groupBoxSSLog.setTitle(_translate("Youtube", "SS LOG"))
        self.groupBoxDownloadLog.setTitle(_translate("Youtube", "YT DOWNLOAD LOG"))
        self.groupBoxYtPlanLog.setTitle(_translate("Youtube", "YT Plan LOG"))
