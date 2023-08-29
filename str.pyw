import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Ui_gui4str import Ui_Form
from PyQt5 import QtCore
import base64
# self.exec.clicked.connect(Form.Exec())


def execCode(c, code, ptn='c', i=0):
    lc = locals()
    try:
        exec(ptn+' = '+code)
        c = lc['c']
    except:
        c = '语法格式错误'
    return c


def replace(a, b):  # a:字符串 b:待替换的字符列表
    i = 0
    while(1):
        try:
            id = a.index('$')
            a = a[:id]+b[i]+a[id+1:]
            i += 1
        except:
            break
    return a


def Hex(inp):  # 列表元素都转int再hex
    inp = int(inp) if type(inp) == str else inp
    return fmt(hex(inp)[2:])


def Str(inp, pat=' '):  # 列表元素都转成字符串
    return pat.join([str(i) for i in inp])


def fmt(s):
    return '0'+s if len(s) < 2 else s


def str2U(inp):
    res = []
    for i in inp:
        if ord(i) in range(128):
            u = Hex(ord(i))+' 00'
        else:
            u = i.encode('unicode-escape')[-4:].decode()
            u = Str([u[-2:], u[:2]])
        res.append(u)
    return Str(res)


def str2ansi(inp):
    res = []
    for i in inp:
        if ord(i) in range(128):
            u = Hex(ord(i))+' 00'
        else:
            u = bytearray(i.encode('gb2312'))
            u = Str([Hex(i) for i in u], pat='')
        res.append(u)
    return Str(res)


def ansi2str(inp):
    res = []
    for i in inp.split():
        if len(i) == 4:
            ch = bytearray([int(i, 16)
                            for i in [i[:2], i[2:]]]).decode('gb2312')
            res.append(ch)
        else:
            res.append(chr(int(i, 16)))
    return Str(res)


def oct2hex(inp):
    data = [Hex(i) for i in inp.split()]
    return Str(data)


def hex2oct(inp):
    data = [int(i, 16) for i in inp.split()]
    return Str(data)


def U2str(inp):
    res = []
    data = inp.split()
    a = iter(data)
    for i in range(len(data)//2):
        n, m = next(a), next(a)
        res.append(chr(int(m+n, 16)))
    return Str(res, pat='')


def findFlag(path, pattern):
    if pattern == '':
        pattern = 'flag'
    with open(path[8:], 'rb') as f:
        content = f.read()
        try:
            flag = content.split(
                bytes(pattern, encoding='utf-8')+b'{')[1].split(b'}')[0]
            return pattern+"{"+flag.decode()+"}"
        except:
            return '没有检测到flag QAQ'


class MyWin(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.setupUi(self)

    def Trans(self):
        boxs = [self.oct, self.hex, self.ansi, self.unicode, self.str]
        contents = [i.toPlainText() for i in boxs]
        if sum([i != '' for i in contents]) > 1:
            [i.setPlainText('') for i in boxs]
        else:
            if contents[0]:
                tmpHex = oct2hex(contents[0])
                boxs[1].setPlainText(tmpHex)
            elif contents[1]:
                boxs[0].setPlainText(hex2oct(contents[1]))
            elif contents[3]:
                boxs[4].setPlainText(U2str(contents[3]))
            elif contents[2]:
                boxs[4].setPlainText(ansi2str(contents[2]))
            elif contents[4]:
                boxs[2].setPlainText(str2ansi(contents[4]))
                boxs[3].setPlainText(str2U(contents[4]))

    def Exec(self):
        checkBoxs = [self.number, self.space]
        content = self.origin.toPlainText()
        code = self.code.text() if self.code.text() != '' else 'c'
        # ptn = '\n' if self.line.isChecked() else ' '
        if self.mulselect.currentText() == '辣鸡题目检测':
            self.res.setPlainText(findFlag(content, code))
        if '$' in self.mulselect.currentText():
            new_code = replace(self.mulselect.currentText(), code.split('&'))
            c = execCode(content, new_code)
            self.res.setPlainText(c)

        else:
            if self.number.isChecked():
                content = content.split('\n')
                for i in range(len(content)):
                    content[i] = content[i][i//10+1:]
                content = '\n'.join(content)
            if self.space.isChecked():
                for i in ['\xa0']:
                    content.replace(i, ' ')
            if self.line.isChecked():
                c = content.split('\n')
                for i in range(len(c)):
                    c = execCode(c, code, 'c[i]', i)
                    self.res.setPlainText('\n'.join(c))
            else:
                c = execCode(content, code)
                if type(c) == list:
                    self.res.setPlainText(' '.join(c))
                else:
                    self.res.setPlainText(c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWin()
    # myWin.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    myWin.show()
    sys.exit(app.exec_())

# 分行处理
