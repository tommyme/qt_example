# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\27564\Desktop\projects\pyqt\gui4str.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 384)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.string = QtWidgets.QWidget()
        self.string.setObjectName("string")
        self.layoutWidget_2 = QtWidgets.QWidget(self.string)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 221, 201))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.space = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.space.setObjectName("space")
        self.verticalLayout_2.addWidget(self.space)
        self.number = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.number.setObjectName("number")
        self.verticalLayout_2.addWidget(self.number)
        self.line = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.mulselect = QtWidgets.QComboBox(self.layoutWidget_2)
        self.mulselect.setObjectName("mulselect")
        self.mulselect.addItem("")
        self.mulselect.addItem("")
        self.mulselect.addItem("")
        self.mulselect.addItem("")
        self.mulselect.addItem("")
        self.verticalLayout_2.addWidget(self.mulselect)
        self.code = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.code.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.code.setText("")
        self.code.setAlignment(QtCore.Qt.AlignCenter)
        self.code.setObjectName("code")
        self.verticalLayout_2.addWidget(self.code)
        self.exec = QtWidgets.QPushButton(self.layoutWidget_2)
        self.exec.setObjectName("exec")
        self.verticalLayout_2.addWidget(self.exec)
        self.layoutWidget_3 = QtWidgets.QWidget(self.string)
        self.layoutWidget_3.setGeometry(QtCore.QRect(240, 10, 281, 301))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.origin = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.origin.setObjectName("origin")
        self.verticalLayout.addWidget(self.origin)
        self.res = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.res.setInputMethodHints(QtCore.Qt.ImhNone)
        self.res.setObjectName("res")
        self.verticalLayout.addWidget(self.res)
        self.tabWidget.addTab(self.string, "")
        self.chick = QtWidgets.QWidget()
        self.chick.setObjectName("chick")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.chick)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 321, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.oct = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.oct.setObjectName("oct")
        self.verticalLayout_3.addWidget(self.oct)
        self.hex = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.hex.setObjectName("hex")
        self.verticalLayout_3.addWidget(self.hex)
        self.str = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.str.setObjectName("str")
        self.verticalLayout_3.addWidget(self.str)
        self.ansi = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.ansi.setObjectName("ansi")
        self.verticalLayout_3.addWidget(self.ansi)
        self.unicode = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.unicode.setObjectName("unicode")
        self.verticalLayout_3.addWidget(self.unicode)
        self.trans = QtWidgets.QPushButton(self.chick)
        self.trans.setGeometry(QtCore.QRect(430, 10, 91, 311))
        self.trans.setObjectName("trans")
        self.label = QtWidgets.QLabel(self.chick)
        self.label.setGeometry(QtCore.QRect(330, 30, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.chick)
        self.label_2.setGeometry(QtCore.QRect(330, 100, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.chick)
        self.label_3.setGeometry(QtCore.QRect(330, 160, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.chick)
        self.label_4.setGeometry(QtCore.QRect(330, 220, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.chick)
        self.label_5.setGeometry(QtCore.QRect(330, 280, 54, 12))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.chick, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.exec.clicked.connect(Form.Exec)
        self.trans.clicked.connect(Form.Trans)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ybw_Tool"))
        self.space.setText(_translate("Form", "空格转换"))
        self.number.setText(_translate("Form", "去掉行数前缀"))
        self.line.setText(_translate("Form", "按行执行代码"))
        self.mulselect.setItemText(0, _translate("Form", "无"))
        self.mulselect.setItemText(1, _translate("Form", "空格转换"))
        self.mulselect.setItemText(2, _translate("Form", "去掉行数前缀"))
        self.mulselect.setItemText(3, _translate("Form", "辣鸡题目检测"))
        self.mulselect.setItemText(4, _translate(
            "Form", "\'$\'.join(c.split(\'$\'))"))
        self.exec.setText(_translate("Form", "执行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.string), _translate("Form", "字符串"))
        self.trans.setText(_translate("Form", "转换"))
        self.label.setText(_translate("Form", "oct"))
        self.label_2.setText(_translate("Form", "hex"))
        self.label_3.setText(_translate("Form", "str"))
        self.label_4.setText(_translate("Form", "ansi"))
        self.label_5.setText(_translate("Form", "unicode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.chick), _translate("Form", "转换"))
