
# 安装PySide2 : pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyside2
from PySide2.QtWidgets import QApplication, QMessageBox, QLineEdit, QAction
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon

# word
from docx import Document
from docx.shared import Inches

class MyBase:
    def __init__(self):
        # 从文件中加载UI定义
        qfile_base = QFile('ui/mybase.ui')
        qfile_base.open(QFile.ReadOnly)
        qfile_base.close()

        # 从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如self.ui.button, self.ui.textEdit
        self.ui = QUiLoader().load(qfile_base)
        self.ui.searchBtn1.clicked.connect(self.searchParagraphs)

        # openAction = QAction()
        # openAction.setShortcut('Ctrl+o')
        # openAction.triggered.connect(self.exit)
        # self.ui.searchBtn1.addAction(openAction)

    def exit(self):
        print('ctrl+o')

    def searchBtnClick(self):
        keyWords = self.ui.lineEdit.text()
        print(keyWords)
        self.searchParagraphs()

    # 从关键字获取句子
    def searchParagraphs(self):
        print('清除内容')
        self.ui.textEdit3.clear()

        # pip3 install python-docx
        # 创建word文档对象
        document1 = Document()
        document = Document("book/docxs/择天记.docx")
        # 添加标题
        document1.add_heading('择天记', 0)

        # 前一行
        lastLine = ''
        count = 0
        nextLine = ''
        readNextLine = False

        all_paragraphs = document.paragraphs
        keyWords = self.ui.lineEdit.text()
        print(keyWords)

        for paragraph in all_paragraphs:
            line = paragraph.text
            if line in '\n' \
                    or '.com' in line \
                    or 'http:' in line \
                    or '----' in line:
                continue

            if readNextLine == True:
                nextLine = line
                readNextLine = False
                continue

            wrod = keyWords
            if wrod in line:
                linnn = line.split(wrod)
                newLine = linnn[0] + '__' + wrod + '__' + linnn[1]
                print('下一行：', nextLine)
                # self.ui.textEdit3.insertPlainText(nextLine)
                print('-------')
                print('上一行：', lastLine)
                print('拆分后：', newLine)
                self.ui.textEdit3.insertPlainText(nextLine)
                self.ui.textEdit3.insertPlainText('\n\n')
                self.ui.textEdit3.insertPlainText(lastLine)
                self.ui.textEdit3.insertPlainText('\n')
                self.ui.textEdit3.insertPlainText(newLine)
                self.ui.textEdit3.insertPlainText('\n')
                # 记录下一行
                readNextLine = True
                # print('当前行：', paragraph.text)
                # document1.add_paragraph(paragraph.text)

            lastLine = line
            count += 1
            if count == 100000:
                break

        # document1.save("book/docxs/择天季笔录.docx")

if __name__ == "__main__":
    app = QApplication([])
    mybase1 = MyBase()
    mybase1.ui.show()
    # mybase1.searchBtnClick()

    app.exec_()
