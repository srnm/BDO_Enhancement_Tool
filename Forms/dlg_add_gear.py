# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rammc\Documents\PyCharm3\BDO_Enhancement_Tool\Forms\dlg_add_gear.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgSearchGear(object):
    def setupUi(self, dlgSearchGear):
        dlgSearchGear.setObjectName("dlgSearchGear")
        dlgSearchGear.resize(683, 477)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlgSearchGear)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(dlgSearchGear)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtSearch = QtWidgets.QLineEdit(self.widget)
        self.txtSearch.setObjectName("txtSearch")
        self.horizontalLayout.addWidget(self.txtSearch)
        self.cmdSearch = QtWidgets.QPushButton(self.widget)
        self.cmdSearch.setObjectName("cmdSearch")
        self.horizontalLayout.addWidget(self.cmdSearch)
        self.cmbGearType = QtWidgets.QComboBox(self.widget)
        self.cmbGearType.setObjectName("cmbGearType")
        self.cmbGearType.addItem("")
        self.cmbGearType.addItem("")
        self.cmbGearType.addItem("")
        self.cmbGearType.addItem("")
        self.horizontalLayout.addWidget(self.cmbGearType)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(dlgSearchGear)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.spinResultsPerPage = QtWidgets.QSpinBox(self.widget_2)
        self.spinResultsPerPage.setMinimum(1)
        self.spinResultsPerPage.setMaximum(999999999)
        self.spinResultsPerPage.setProperty("value", 20)
        self.spinResultsPerPage.setObjectName("spinResultsPerPage")
        self.horizontalLayout_2.addWidget(self.spinResultsPerPage)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.spinPages = QtWidgets.QSpinBox(self.widget_2)
        self.spinPages.setMinimum(1)
        self.spinPages.setMaximum(999999999)
        self.spinPages.setProperty("value", 1)
        self.spinPages.setObjectName("spinPages")
        self.horizontalLayout_2.addWidget(self.spinPages)
        self.cmdPrev = QtWidgets.QPushButton(self.widget_2)
        self.cmdPrev.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.cmdPrev.setFont(font)
        self.cmdPrev.setObjectName("cmdPrev")
        self.horizontalLayout_2.addWidget(self.cmdPrev)
        self.cmdNext = QtWidgets.QPushButton(self.widget_2)
        self.cmdNext.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.cmdNext.setFont(font)
        self.cmdNext.setObjectName("cmdNext")
        self.horizontalLayout_2.addWidget(self.cmdNext)
        self.verticalLayout.addWidget(self.widget_2)
        self.lstGear = QtWidgets.QTableWidget(dlgSearchGear)
        self.lstGear.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lstGear.setObjectName("lstGear")
        self.lstGear.setColumnCount(4)
        self.lstGear.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lstGear.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lstGear.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lstGear.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.lstGear.setHorizontalHeaderItem(3, item)
        self.lstGear.horizontalHeader().setCascadingSectionResizes(True)
        self.lstGear.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.lstGear)

        self.retranslateUi(dlgSearchGear)
        QtCore.QMetaObject.connectSlotsByName(dlgSearchGear)

    def retranslateUi(self, dlgSearchGear):
        _translate = QtCore.QCoreApplication.translate
        dlgSearchGear.setWindowTitle(_translate("dlgSearchGear", "Add Gear"))
        self.txtSearch.setPlaceholderText(_translate("dlgSearchGear", "Search..."))
        self.cmdSearch.setText(_translate("dlgSearchGear", "Search"))
        self.cmbGearType.setItemText(0, _translate("dlgSearchGear", "Any"))
        self.cmbGearType.setItemText(1, _translate("dlgSearchGear", "Weapon"))
        self.cmbGearType.setItemText(2, _translate("dlgSearchGear", "Armor"))
        self.cmbGearType.setItemText(3, _translate("dlgSearchGear", "Accessory"))
        self.label.setText(_translate("dlgSearchGear", "Results Per Page: "))
        self.cmdPrev.setText(_translate("dlgSearchGear", "<"))
        self.cmdNext.setText(_translate("dlgSearchGear", ">"))
        item = self.lstGear.horizontalHeaderItem(0)
        item.setText(_translate("dlgSearchGear", "Name"))
        item = self.lstGear.horizontalHeaderItem(1)
        item.setText(_translate("dlgSearchGear", "Class"))
        item = self.lstGear.horizontalHeaderItem(2)
        item.setText(_translate("dlgSearchGear", "Grade"))
        item = self.lstGear.horizontalHeaderItem(3)
        item.setText(_translate("dlgSearchGear", "ID"))

